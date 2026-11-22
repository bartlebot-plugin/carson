#!/usr/bin/env python3
"""Carson's budget arithmetic.

Reads a budget file and a transactions file (both plain CSV), works out each
category's month-by-month figures, and writes one JSON file holding the
documents for the budget page's database. Standard library only. It reads two
files and writes one; it changes nothing else and uses no network.

Usage:
  python3 -I -B budget.py --budget budget-2026.csv --transactions transactions-2026.csv \
      --year 2026 --today 2026-11-21 --out budget-page.json [--name Pat] [--no-detail]

Budget CSV columns:  category,group,kind,rollover,jan,feb,...,dec
  kind is "expense" (default) or "income". rollover is "yes" or "no".
Transactions CSV columns:  date,description,amount,category,account,sorted_by,id
  date is YYYY-MM-DD. amount is negative for money going out and positive for
  money coming in. Rows whose category is "Transfer" are ignored. A blank or
  unknown category is not sorted yet: money going out is counted as
  "Uncategorized" spending; money coming in is kept out of spending and
  reported apart as "Money in, not sorted". sorted_by says who chose the
  category ("rule", "you", "guess", "tiller"); "guess" marks Carson's own
  guesses, which are counted so the user can review them. sorted_by and id
  are optional.

Totals mode (for a budget kept in a Google Sheet, where the sheet adds up the
transactions): pass --totals totals.csv, a copy of the sheet's Totals tab.
Its first column is a name and the next twelve are the months, January to
December, holding signed sums (money out negative). Rows named for a budget
category, and these special rows, are read; any other row is ignored:
  (not sorted, money out)   (not sorted, money in)
  (not sorted, count out)   (not sorted, count in)
  (guesses, count)          (everything, sum)          Transfer
In totals mode the figures come from the totals; --transactions is optional
and is used only to list individual transactions on the page.
"""
import argparse
import csv
import json
import sys
from datetime import date
from decimal import Decimal, InvalidOperation

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
MAX_DETAIL = 200  # transactions shown per category per month


def money(text):
    t = (text or "").strip().replace("$", "").replace(",", "")
    if t.startswith("(") and t.endswith(")"):
        t = "-" + t[1:-1]
    if t == "":
        return Decimal("0")
    return Decimal(t)


def cents(d):
    return float(d.quantize(Decimal("0.01")))


def fail(msg):
    print("PROBLEM: " + msg)
    sys.exit(1)


def read_budget(path):
    cats = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            name = row.get("category", "")
            if not name:
                continue
            kind = row.get("kind", "expense").lower() or "expense"
            if kind not in ("expense", "income"):
                fail("budget line %d: kind must be expense or income, not '%s'" % (n, kind))
            try:
                amounts = [money(row.get(m, "")) for m in MONTHS]
            except InvalidOperation:
                fail("budget line %d (%s): an amount is not a number" % (n, name))
            cats.append({
                "name": name,
                "group": row.get("group", "") or "Other",
                "kind": kind,
                "rollover": row.get("rollover", "no").lower() in ("yes", "y", "true", "1"),
                "amounts": amounts,
            })
    if not cats:
        fail("the budget file has no categories")
    seen = set()
    for c in cats:
        key = c["name"].lower()
        if key in seen:
            fail("the budget lists '%s' twice" % c["name"])
        seen.add(key)
    return cats


def read_transactions(path, year):
    rows, skipped = [], 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            d = row.get("date", "")
            if not d:
                continue
            try:
                y, m, dd = int(d[0:4]), int(d[5:7]), int(d[8:10])
                date(y, m, dd)
            except (ValueError, IndexError):
                fail("transactions line %d: '%s' is not a date written YYYY-MM-DD" % (n, d))
            if y != year:
                skipped += 1
                continue
            try:
                amt = money(row.get("amount", ""))
            except InvalidOperation:
                fail("transactions line %d: '%s' is not an amount" % (n, row.get("amount", "")))
            rows.append({"month": m, "date": d[:10], "desc": row.get("description", ""),
                         "amount": amt, "category": row.get("category", ""), "account": row.get("account", ""),
                         "guess": row.get("sorted_by", "").lower() == "guess"})
    return rows, skipped


def read_totals(path):
    """The sheet's Totals tab: {lowercased name: [12 Decimals]}."""
    out = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for n, row in enumerate(csv.reader(f), start=1):
            if n == 1 or not row or not (row[0] or "").strip():
                continue
            vals = []
            for cell in (row[1:13] + [""] * 12)[:12]:
                try:
                    vals.append(money(cell))
                except InvalidOperation:
                    fail("totals line %d (%s): '%s' is not a number; a formula in the Totals tab may be broken" % (n, row[0], cell))
            out[row[0].strip().lower()] = vals
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", required=True)
    ap.add_argument("--transactions", default="")
    ap.add_argument("--totals", default="", help="a copy of the sheet's Totals tab; the figures then come from it")
    ap.add_argument("--only-months", type=int, default=0, help="write only the last N months' documents")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--today", required=True, help="YYYY-MM-DD, the user's local date")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", default="")
    ap.add_argument("--source", default="statements")
    ap.add_argument("--no-detail", action="store_true", help="leave individual transactions off the page")
    a = ap.parse_args()

    try:
        ty, tm, td = int(a.today[0:4]), int(a.today[5:7]), int(a.today[8:10])
        date(ty, tm, td)
    except (ValueError, IndexError):
        fail("--today must be written YYYY-MM-DD")

    cats = read_budget(a.budget)
    if not a.transactions and not a.totals:
        fail("give --transactions, or --totals, or both")
    rows, skipped = read_transactions(a.transactions, a.year) if a.transactions else ([], 0)
    by_name = {c["name"].lower(): c for c in cats}

    # Last month to show: the current month in the current year, December for a past year.
    if a.year < ty:
        last_month, days_frac = 12, Decimal(1)
    elif a.year == ty:
        import calendar
        last_month = tm
        days_frac = Decimal(td) / Decimal(calendar.monthrange(ty, tm)[1])
    else:
        fail("the year %d has not started" % a.year)

    # Spending per category per month. Expenses: money out counts as positive spending.
    spent = {c["name"]: [Decimal(0)] * 12 for c in cats}
    detail = {c["name"]: [[] for _ in range(12)] for c in cats}
    uncategorized = [Decimal(0)] * 12
    unc_detail = [[] for _ in range(12)]
    unc_count, transfers = 0, 0
    # Money coming in that has not been sorted is not spending. Keep it apart.
    money_in = [Decimal(0)] * 12
    in_detail = [[] for _ in range(12)]
    in_count, guess_count = 0, 0
    for r in rows:
        key = r["category"].lower()
        if key == "transfer":
            transfers += 1
            continue
        i = r["month"] - 1
        item = {"d": r["date"], "desc": r["desc"][:80], "amt": cents(r["amount"])}
        c = by_name.get(key)
        if c is None and r["amount"] > 0:
            in_count += 1
            money_in[i] += r["amount"]
            in_detail[i].append(item)
            continue
        if c is not None and r["guess"]:
            guess_count += 1
            item["g"] = True
        if c is None:
            unc_count += 1
            uncategorized[i] += -r["amount"]
            unc_detail[i].append(item)
            continue
        spent[c["name"]][i] += (r["amount"] if c["kind"] == "income" else -r["amount"])
        detail[c["name"]][i].append(item)

    not_listed = [Decimal(0)] * 12
    if a.totals:
        # The sheet has already added up the transactions. Take the figures from it;
        # the transactions read above are kept only for the lists on the page.
        t = read_totals(a.totals)
        zero = [Decimal(0)] * 12
        for c in cats:
            sums = t.get(c["name"].lower())
            if sums is None:
                fail("the Totals tab has no row for the category '%s'" % c["name"])
            spent[c["name"]] = [(v if c["kind"] == "income" else -v) for v in sums]
        out_sum = t.get("(not sorted, money out)", zero)
        in_sum = t.get("(not sorted, money in)", zero)
        uncategorized = [-v for v in out_sum]
        money_in = list(in_sum)
        unc_count = int(sum(t.get("(not sorted, count out)", zero)))
        in_count = int(sum(t.get("(not sorted, count in)", zero)))
        guess_count = int(sum(t.get("(guesses, count)", zero)))
        everything = t.get("(everything, sum)")
        if everything is not None:
            # Whatever the listed rows do not account for sits in a category the budget does not list.
            for i in range(12):
                listed = out_sum[i] + in_sum[i] + t.get("transfer", zero)[i]
                listed += sum((t[c["name"].lower()][i] for c in cats), Decimal(0))
                diff = everything[i] - listed
                if abs(diff) >= Decimal("0.005"):
                    not_listed[i] = diff
                    uncategorized[i] += -diff
        transfers = -1

    docs = {}
    month_ids = []
    summary_lines = []
    for i in range(last_month):
        mid = "%04d-%02d" % (a.year, i + 1)
        month_ids.append(mid)
        out_cats, tx = [], {}
        tot_budget = tot_spent = tot_rollin = Decimal(0)
        over = 0
        for c in cats:
            rollin = Decimal(0)
            if c["rollover"] and c["kind"] == "expense":
                for j in range(i):
                    rollin += c["amounts"][j] - spent[c["name"]][j]
            budget = c["amounts"][i]
            actual = spent[c["name"]][i]
            available = rollin + budget
            left = available - actual
            entry = {"name": c["name"], "group": c["group"], "kind": c["kind"], "rollover": c["rollover"],
                     "rollin": cents(rollin), "budget": cents(budget), "actual": cents(actual), "left": cents(left)}
            if i > 0:
                # Last month's figures, so the page can explain where the carried-over amount came from.
                p_budget, p_actual = c["amounts"][i - 1], spent[c["name"]][i - 1]
                carries = c["rollover"] and c["kind"] == "expense"
                p_rollin = rollin - (p_budget - p_actual) if carries else Decimal(0)
                entry["prior"] = {"rollin": cents(p_rollin), "budget": cents(p_budget), "actual": cents(p_actual),
                                  "left": cents(p_rollin + p_budget - p_actual)}
            out_cats.append(entry)
            if c["kind"] == "expense":
                tot_budget += budget
                tot_spent += actual
                tot_rollin += rollin
                # "Over" means more than 5% past what was available, the same line the page draws.
                if actual > 0 and (available <= 0 or actual / available > Decimal("1.05")):
                    over += 1
            if not a.no_detail and detail[c["name"]][i]:
                items = sorted(detail[c["name"]][i], key=lambda x: x["d"], reverse=True)
                tx[c["name"]] = items[:MAX_DETAIL]
        if uncategorized[i] != 0 or unc_detail[i]:  # noqa: one "Uncategorized" line per month
            out_cats.append({"name": "Uncategorized", "group": "Needs sorting", "kind": "expense", "rollover": False,
                             "rollin": 0.0, "budget": 0.0, "actual": cents(uncategorized[i]), "left": cents(-uncategorized[i])})
            tot_spent += uncategorized[i]
            if not a.no_detail:
                tx["Uncategorized"] = sorted(unc_detail[i], key=lambda x: x["d"], reverse=True)[:MAX_DETAIL]
        if in_detail[i] or money_in[i] != 0:
            out_cats.append({"name": "Money in, not sorted", "group": "Needs sorting", "kind": "income", "rollover": False,
                             "rollin": 0.0, "budget": 0.0, "actual": cents(money_in[i]), "left": 0.0})
            if not a.no_detail:
                tx["Money in, not sorted"] = sorted(in_detail[i], key=lambda x: x["d"], reverse=True)[:MAX_DETAIL]
        docs["months/" + mid] = {"month": mid, "categories": out_cats, "tx": tx,
                                 "total_budget": cents(tot_budget), "total_spent": cents(tot_spent), "over": over,
                                 "total_rollin": cents(tot_rollin), "total_left": cents(tot_rollin + tot_budget - tot_spent),
                                 "partial": (a.year == ty and i + 1 == tm)}
        summary_lines.append("%s  budget %10.2f  spent %10.2f  categories over: %d" % (mid, tot_budget, tot_spent, over))

    year_cats = []
    y_annual = y_spent = y_to_date = Decimal(0)
    for c in cats:
        annual = sum(c["amounts"], Decimal(0))
        ytd = sum(spent[c["name"]][:last_month], Decimal(0))
        to_date = sum(c["amounts"][:last_month - 1], Decimal(0)) + c["amounts"][last_month - 1] * days_frac
        by_month = [{"m": "%04d-%02d" % (a.year, j + 1), "budget": cents(c["amounts"][j]), "actual": cents(spent[c["name"]][j]),
                     "left": cents(c["amounts"][j] - spent[c["name"]][j])} for j in range(last_month)]
        year_cats.append({"name": c["name"], "group": c["group"], "kind": c["kind"],
                          "annual": cents(annual), "spent": cents(ytd), "to_date": cents(to_date), "left": cents(annual - ytd),
                          "months": by_month})
        if c["kind"] == "expense":
            y_annual += annual
            y_spent += ytd
            y_to_date += to_date
    unc_ytd = sum(uncategorized[:last_month], Decimal(0))
    if unc_ytd != 0:
        year_cats.append({"name": "Uncategorized", "group": "Needs sorting", "kind": "expense",
                          "annual": 0.0, "spent": cents(unc_ytd), "to_date": 0.0, "left": cents(-unc_ytd)})
    y_spent += unc_ytd
    in_ytd = sum(money_in[:last_month], Decimal(0))
    if in_ytd != 0:
        year_cats.append({"name": "Money in, not sorted", "group": "Needs sorting", "kind": "income",
                          "annual": 0.0, "spent": cents(in_ytd), "to_date": 0.0, "left": 0.0})
    year_elapsed = (Decimal(last_month - 1) + days_frac) / Decimal(12) * 100
    docs["years/%04d" % a.year] = {"year": a.year, "categories": year_cats, "through": month_ids[-1],
                                   "total_annual": cents(y_annual), "total_spent": cents(y_spent),
                                   "total_to_date": cents(y_to_date), "total_left": cents(y_annual - y_spent),
                                   "year_elapsed": float(year_elapsed.quantize(Decimal("0.1")))}
    docs["budget/meta"] = {"name": a.name, "year": a.year, "months": month_ids, "source": a.source,
                           "detail": not a.no_detail, "updated_on": a.today,
                           "unsorted_out": unc_count, "unsorted_in": in_count, "guesses": guess_count}

    if a.only_months > 0:
        keep = set("months/" + m for m in month_ids[-a.only_months:])
        docs = {k: v for k, v in docs.items() if not k.startswith("months/") or k in keep}

    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=1)

    print("Budget figures for %d, through %s" % (a.year, a.today))
    for line in summary_lines:
        print(line)
    if a.totals:
        print("Figures taken from the sheet's totals. Transactions read for the page's lists: %d" % len(rows))
        for i in range(last_month):
            if not_listed[i] != 0:
                print("NOT LISTED: %.2f in %04d-%02d sits in a category the budget does not list. It is counted under Uncategorized. Find the category name in the Transactions tab and correct it." % (not_listed[i], a.year, i + 1))
    else:
        print("Transactions read: %d (ignored as transfers: %d; from other years: %d)" % (len(rows), transfers, skipped))
    if unc_count:
        print("NEEDS SORTING: %d purchases or payments have no category or one the budget does not list." % unc_count)
    if in_count:
        print("MONEY IN, NOT SORTED: %d deposits or credits have no category. They are not counted as spending." % in_count)
    if guess_count:
        print("CARSON'S GUESSES: %d transactions were sorted by Carson's guess and are waiting for the user's review." % guess_count)
    print("Documents written to %s: %d" % (a.out, len(docs)))


if __name__ == "__main__":
    main()
