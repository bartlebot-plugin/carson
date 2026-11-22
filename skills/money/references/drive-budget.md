# The budget in Drive mode

When the household keeps its papers in Google Drive, the budget lives in one Google Sheet and the Sheet does the adding up. Carson reads a small table of totals, never the whole list of transactions, so an update stays quick however long the list grows.

Everything in the money skill still applies: what Carson may say, how categories and amounts are chosen, how transactions are sorted, what the page shows. This file says only what is different.

It needs the Google Sheets tools. If they are missing, connect Google Sheets the way setup connects an app. If that fails, say the budget can't be kept in Drive without it, and stop.

## The Sheet

One Google Sheet named `Carson budget YYYY`, in the Carson folder under `Money/Budget`. Record its ID in the profile as `money.sheet_id`. Check for an existing one before creating it (Drive allows two files with one name).

It has three tabs. Freeze the first row of each.

This Sheet is the only budget file Carson makes in Drive. Never create a second spreadsheet, a helper sheet, or an import file there, even for a moment: put statement or Tiller rows straight into the Transactions tab, and keep any working copies in this conversation's own working space. If the Carson folder holds a sheet named "Carson budget import (temporary)" left by an earlier version, tell the user once that it is not needed and they may delete it; Carson does not delete it.

**Transactions** — one row per transaction. Columns A to H:

`date` · `description` · `amount` · `category` · `account` · `sorted_by` · `id` · `month`

The first seven are exactly the columns of the local transactions file, with the same conventions. `month` is a key Carson writes with every row so the Sheet can add things up: the year, `-M`, and the two-digit month of the date, as text (`2026-M11`). Write the date as text in the form YYYY-MM-DD, and the amount as a number.

**Budget** — the plan. Columns: `category` · `group` · `kind` · `rollover` · `jan` … `dec`. The same as the local budget file.

**Totals** — formulas only. Carson writes it; nobody types in it.

- A1 is `name`. B1 holds one formula that fills B1 to M1 with the twelve month keys: `=ARRAYFORMULA("YYYY-M"&TEXT(SEQUENCE(1,12),"00"))`, with the budget's year in place of YYYY.
- Each row below has a name in column A and one formula in column B that fills its twelve months.

| Row | Column A | Column B |
|---|---|---|
| 2 | `(not sorted, money out)` | `=MAP($B$1:$M$1,LAMBDA(k,SUMIFS(Transactions!$C:$C,Transactions!$D:$D,"",Transactions!$H:$H,k,Transactions!$C:$C,"<0")))` |
| 3 | `(not sorted, money in)` | the same, ending `">0"` |
| 4 | `(not sorted, count out)` | `=MAP($B$1:$M$1,LAMBDA(k,COUNTIFS(Transactions!$D:$D,"",Transactions!$H:$H,k,Transactions!$C:$C,"<0")))` |
| 5 | `(not sorted, count in)` | the same, ending `">0"` |
| 6 | `(guesses, count)` | `=MAP($B$1:$M$1,LAMBDA(k,COUNTIFS(Transactions!$F:$F,"guess",Transactions!$H:$H,k)))` |
| 7 | `(everything, sum)` | `=MAP($B$1:$M$1,LAMBDA(k,SUMIFS(Transactions!$C:$C,Transactions!$H:$H,k)))` |
| 8 | `(rows)` | `=COUNTA(Transactions!$A:$A)-1` |
| 9 | `Transfer` | `=MAP($B$1:$M$1,LAMBDA(k,SUMIFS(Transactions!$C:$C,Transactions!$D:$D,$A9,Transactions!$H:$H,k)))` |
| 10 on | one row for each category in the Budget tab, in the same order, its name typed in column A | the row-9 formula, with that row's number in place of the 9 |

Use these formulas exactly. Other ways of writing them do not fill across the months.

When a category is added, renamed, or removed in the Budget tab, bring the Totals rows from row 10 down into line with it straight away, and rename the category on its transactions if it was renamed.

## Each update

1. **Check the Totals tab.** Read A1 to M of the Totals tab (it is small). It must have the special rows, a row for every budget category, and numbers throughout. If a row is missing or a cell holds an error, the formulas have been disturbed: write them again as above, read again, and tell the user in one line that the totals were repaired.
2. **Bring in new transactions** (statements, or Tiller as the money skill describes) by adding rows at the end of the Transactions tab. To avoid duplicates, read only the rows that could overlap, never the whole tab: the `(rows)` figure says how many rows there are, and new transactions are recent, so read the last few hundred rows, or as far back as the earliest date being added.
3. **Sort what needs sorting.** The Totals tab says how many unsorted rows and guesses there are, and in which months. To find them, read columns D and F alone (one short cell each per row), note the row numbers, then read just those rows. Write a category and `sorted_by` back to that row's cells. When a rule is confirmed for a merchant, find that merchant's rows the same way and update them together.
4. **Work out the figures.** Save three small files in this conversation's own working space (not in Drive):
   - the Budget tab as `budget.csv`;
   - the Totals tab, A1 to M, as `totals.csv`, exactly as read;
   - the transactions of this month and last month as `recent.csv`, with the first seven columns, for the lists on the page.

   Then run the script from this skill's `scripts/` folder:

   `python3 -I -B <this skill's folder>/scripts/budget.py --budget budget.csv --totals totals.csv --transactions recent.csv --only-months 2 --year YYYY --today YYYY-MM-DD --out budget-page.json --name <what Carson calls the user> --source <statements or tiller>`

   Add `--no-detail` when `money.show_detail` is false. Read what it prints, as in folder mode. A line starting `NOT LISTED:` means some transactions carry a category name that is not in the budget (usually a spelling difference): find it in column D, correct it, read the totals again, and run the script again.
5. **Update the page.** Write `budget/meta`, `years/YYYY`, and the two `months/…` entries the script produced. Leave the page's earlier months as they are.

**A full rebuild** is the same, but with the whole year's transactions in `recent.csv` and without `--only-months`, so every month on the page is written again. Do one when the page is first built, when categories on transactions older than last month were changed (a rule confirmed, guesses reviewed), in the first update of each month, and whenever the user asks. Reading the whole tab is slow; say "This will take a few minutes" first.

## Setting up

Follow the money skill's "Setting up a budget." In its last step, create the Sheet and its three tabs, write the Budget tab from the user's answers, write the Totals tab, and build the page with a full rebuild.

## Numbers come back as text

Values read from a Sheet arrive as text, sometimes with a currency sign or commas if the user has formatted the column. The script copes with `$`, commas, and brackets for negatives. Do not tidy the numbers by hand before saving the files.

## What the user can do in the Sheet

The Sheet is theirs to look at, sort, and filter. Tell them once, when the budget is set up:

> Your budget is a Google Sheet called "Carson budget 2026" in your Carson folder. You can open it any time. Change a category on the Transactions tab if I got one wrong, and I'll learn from it. Please leave the Totals tab alone; it holds the sums.

If the user changed a category in the Transactions tab themselves, that row's `sorted_by` may still say `guess` or `rule`. When a row's category differs from what Carson last wrote for that merchant's rule, treat the user's as right: set `sorted_by` to `you`, and ask whether it should become the rule.

## In a scheduled run

As the money skill says, using the steps above. Never do a full rebuild in a scheduled run except the monthly one.
