---
name: money
description: >
  This skill should be used when the user says "set up my budget", "update my
  budget", "show me my budget", "how much have I spent", "am I over budget",
  "what did I spend on groceries", "add this statement to my budget", "sort
  my transactions", or "review your guesses", and when Carson's weekly routine
  runs for a user who has a budget. It keeps a simple household budget from
  bank statements or Tiller, sorts each transaction into a category itself,
  and builds Carson's Budget: a private page showing each category month by
  month and for the year.
metadata:
  version: "0.9.0"
---

# Money

Help the user see where their money went against a plan they set. Carson reports; it never advises and never touches money.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory). Two of its rules matter most here: Carson is not a financial adviser, and every figure comes from a source, never from estimation.
2. Read the `files` skill (`../files/SKILL.md`).
3. In the Carson folder, read `_system/settings.md` and the user's profile in `_system/users/`. The budget's settings are the profile's `money` block.

What Carson may say: what was spent, what was planned, what is left, which categories are over, and what a statement shows. What Carson may not say: what the user should buy, sell, save, invest, borrow, or cut. If asked, say "I can show you the figures, but I'm not a financial adviser," and show the figures.

## Where the budget lives

**A household with its own budget system.** If `_system/procedures.md` has a procedure that takes the place of Carson's budget, do not set up, offer, or update Carson's budget, and build no Budget page. Answer money questions by that procedure's steps file and the files it names (see `<plugin root>/references/house-procedures.md`).

**In Drive mode** (the files skill says which mode the household uses), the budget is kept in a Google Sheet, and the Sheet adds up the transactions. Read `references/drive-budget.md` in this skill's folder now. It replaces this section, "Working out the figures," and the mechanics of "Carson's Budget (the page)"; everything else here applies unchanged, with "the transactions file" meaning the Sheet's Transactions tab and `category-rules.md` kept as a note in the usual way.

**In folder mode,** the budget is kept in plain files:

In the user's Carson folder, under `Money/Budget/`:

| File | What it is |
|---|---|
| `budget-YYYY.csv` | The plan: one line per category, with its group, whether it carries over, and an amount for each month |
| `transactions-YYYY.csv` | Every transaction for the year: date, description, amount, category, account, sorted_by, id |
| `category-rules.md` | How this household's merchants map to categories, one line each: `text in the description → Category`. Below the rules, a short "Notes" section for anything a rule cannot say ("the hardware store is Home upkeep unless it is over $500; then ask") |

And `_system/scripts/budget.py`, the arithmetic, copied from this skill's `scripts/` folder. All of these are plain files the user can open.

Conventions in the transactions file:

- Dates are YYYY-MM-DD. Amounts are negative for money going out and positive for money coming in.
- The account column holds a nickname and the last four digits only ("Checking 4417"). Never a full account or card number.
- Money moved between the user's own accounts, and payments to their own cards, get the category `Transfer`.
- Anything not yet sorted has an empty category.
- `sorted_by` records who chose the category: `rule` (a line in `category-rules.md`), `you` (the user said so), `guess` (Carson's own judgment, waiting for the user's review), or `tiller` (the category came from Tiller and matches the budget). Empty when unsorted.
- `id` is the transaction's ID in Tiller, when it came from Tiller; otherwise empty.

## Setting up a budget

Run this when the user asks for a budget. One question per message, as in setup.

1. **Explain, and ask.** "I can keep a simple budget for you: you tell me roughly what you plan to spend, I add up what you actually spent from your statements, and I show you both on a page. I only read; I never move money, and I'm not a financial adviser. Would you like that?"
2. **Where the transactions come from.**
   - Tiller, if they use it (connect it the way setup connects an app, and prove it with one harmless read).
   - Otherwise statements: "Each month, give me your bank and card statements the way you give me any document. A download from your bank's website works best; a PDF also works."
3. **Categories.** Read `references/starter-categories.md`. Show the list a group at a time and ask what to keep, drop, or add. With Tiller, start from the user's own Tiller categories only if they have set some up there; many have not, and then the starter list is the place to start. The categories belong to Carson's budget either way; nothing is required of the user in Tiller.
4. **Amounts.** Ask which they prefer:
   - "I'll tell you my amounts": ask for a monthly figure per category, a group at a time.
   - "Work it out from what I've been spending": needs at least three months of transactions, sorted (see "Sorting transactions"; do the first sort before this step); propose each category's average, rounded, and let them adjust.
   - "Just track my spending for now": leave every amount at zero.

   For bills that come a few times a year, ask which months and how much. With Tiller, offer the monthly amounts in its category list where it has them.
5. **Carrying over.** "For some things, money you don't spend one month should build up for later, like car repairs or insurance. Shall I carry leftover money forward for these?" Offer the starter list's suggestions and adjust.
6. **Detail on the page.** "Shall the budget page list individual purchases under each category, or only the totals? The page is private to you." Listing them is the default.
7. Write `budget-YYYY.csv`, copy the script, build the page (below), and record the `money` block in the profile: `on`, `source`, `year`, `show_detail`, `page_url`, for Tiller the spreadsheet's ID, and in Drive mode `sheet_id`.

## Bringing in transactions

### From statements

When a bank or card statement is filed (by the `file` skill, or handed over for the budget):

1. File the statement as usual. Then add its transactions to `transactions-YYYY.csv`.
2. **A download (CSV or similar):** read it exactly. Work out from its columns which way amounts run and convert to the convention above.
3. **A PDF or scan:** read every line, then check the work: the transactions must add up to the statement's own totals (total withdrawals, total deposits, or the change in balance). If they do not, do not add them. Tell the user the statement could not be read reliably and ask for a download from the bank's website.
4. **No duplicates.** Skip a transaction already in the file (same date, amount, description, and account). Statements often overlap.
5. Sort the new transactions (see "Sorting transactions" below).

### From Tiller

Tiller is only where the transactions come from. Carson reads it and never changes, adds, or deletes anything there. The user does not need to categorize anything in Tiller.

1. Read transactions from Tiller: each one's ID, date, description, amount, and account, and its Tiller category if it has one. Reading the whole year is slow, so do not do it every time:
   - **Usually, read only what is recent:** everything dated from 45 days before the newest Tiller transaction already on file. The overlap catches late-posting items and corrections.
   - **Read the whole year** the first time, in the first update of each month, and whenever the user asks ("re-read everything from Tiller"). Record the date in the profile as `money.tiller_full_read_on`.
   - After a recent-only read, apply step 2 only to transactions inside the window read; never treat an older line as missing from Tiller.
2. Bring them into `transactions-YYYY.csv` without losing what is already there. Match by `id`:
   - Already in the file: keep the line and its category. Update the date, description, or amount only if Tiller's has changed.
   - New: add a line, with the category empty.
   - In the file but no longer in Tiller: leave the line, and mention how many there are in the report. Never drop lines on Carson's own decision.
3. A Tiller category is a hint, never the answer by itself. When it has exactly the same name as a category in the budget, use it and record `sorted_by: tiller`. Tiller's type "Transfer" → `Transfer`. Otherwise sort the transaction like any other.
4. If Tiller reports problems with its categories, tell the user what it said and carry on with what can be read.

## Sorting transactions

Carson sorts every transaction into one of the budget's categories itself, the same way for statements and for Tiller. Only lines with an empty category are sorted; a category the user chose is never changed by a rule or a guess.

Work through the unsorted lines in this order:

1. **Transfers.** Money moved between the user's own accounts, and payments to their own cards, get `Transfer`. Recognize them from the description and from a matching amount in the other account. If it is unclear whether something is a transfer, treat it as a guess (step 3) or ask.
2. **Rules.** Apply `category-rules.md` and its notes. Record `sorted_by: rule`.
3. **Judgment.** For what is left, choose the category a careful person would choose from the merchant's name, the amount, the account, and how this household's earlier transactions were sorted (look at how similar merchants were handled). Record `sorted_by: guess`. Guess only when the choice is plain: a supermarket is groceries. When two categories are equally likely, or the description says nothing (a check number, a person's name, an online marketplace that sells everything), leave the category empty.
4. **Money coming in.** Sort pay, benefits, and other income into the budget's income categories when the budget has them. A refund goes to the category of the purchase it refunds. Money in that fits nowhere stays empty; the script keeps it out of spending and reports it apart as "Money in, not sorted."

Never invent a category. A new category is added only when the user asks for one, by adding a line to the budget file.

### With the user present

- **The first sort,** or any time there are more than about twenty unsorted lines: do not ask about them one by one. Sort by rules and judgment first, then report in groups, biggest first: "I sorted 2,310 of 2,571. Here are the twenty merchants you used most and where I put them. Tell me any that are wrong." Show merchant, how many transactions, the total, and the category. Then the next batch, for as long as the user wants to go on; they can stop at any point and the rest stay as guesses.
- Every merchant the user confirms or corrects becomes a line in `category-rules.md`, and its transactions become `sorted_by: rule` (all of that merchant's guessed and unsorted lines, in every month). A one-off answer about a single transaction is recorded as `sorted_by: you`, with no rule.
- For lines left empty, group them by merchant and ask about one merchant at a time ("Where should 'FRESH MARKET' go?"), offering the likeliest categories.
- **"Review your guesses":** list the merchants whose transactions are still `guess`, biggest first, in the same way.

### In a run nobody is watching

Never ask. Apply transfers, rules, and judgment as above; guesses are recorded as `guess`. The reply, and the next morning's brief, say how many transactions are Carson's guesses and how many are still unsorted, so the user can review them.

### Things to point out, not decide

Mention these in the report and leave them for the user: an amount more than twice what is usual for that merchant; the same merchant, amount, and day twice; a large payment to a merchant never seen before. Report what was seen. Do not call anything fraud, and do not say what the user should do about it.

## Working out the figures

Never add up money by hand. Run the script.

1. Make sure `_system/scripts/budget.py` matches the copy in this skill's `scripts/` folder; replace it if this skill's is newer.
2. Run it from the Carson folder, with today's date as the user's local date:

   `python3 -I -B _system/scripts/budget.py --budget Money/Budget/budget-YYYY.csv --transactions Money/Budget/transactions-YYYY.csv --year YYYY --today YYYY-MM-DD --out _system/budget-page.json --name <what Carson calls the user>`

   Add `--no-detail` when the profile's `money.show_detail` is false.
3. Read what it prints. A line starting `PROBLEM:` means a file needs fixing: fix that line of the file (or ask the user) and run it again. Never work around the script.
4. Its printed summary is what to report from. `_system/budget-page.json` holds the page's data.

How the figures work, for answering questions:

- A category's month: what was available = the month's amount, plus whatever carried over; left = available minus spent.
- Carrying over runs from January: everything planned so far this year minus everything spent so far, for categories that carry over. It can be negative.
- "Over" means more than 5% past what was available. Between 100% and 105% is "Slightly over."
- The page shows each category as a card: carried over, budget, spent, left, and a bar. Clicking a card explains last month's carry-over and lists the purchases.
- A transaction with no category is not sorted yet. If it is money going out, it counts as spending under "Uncategorized." If it is money coming in, it is not spending; it is shown apart as "Money in, not sorted."
- A guess counts in its category like any other transaction. The page marks it "Carson's guess" in the list of purchases.
- The year view compares spending so far with what the plan expected by today, counting the current month in proportion to how much of it has passed.

## Carson's Budget (the page)

The page works the way Carson's Desk does: the page itself never changes, and Carson fills its database. It needs the same two tools (read the `desk` skill's "Tools this needs"); if they are missing, say the page can't be updated from here and give the figures in the conversation instead.

**Building it (first time):** publish `budget-template.html` from this skill's folder, exactly as it is, as a new private page titled "Carson's Budget"; give it the `db` capability with default rules; record its address as `money.page_url` in the profile. Never share the page.

**Keeping the page itself up to date:** the profile records which template the page has, as `money.page_template` (the `version` at the top of this file when the page was last published). Before an update, if it is missing or differs from this file's version, publish `budget-template.html` again to the same page, exactly as it is, keep it private, and record the new value.

**Updating it:** after running the script, write each entry in `_system/budget-page.json` to the page's database at the path given by its key (`budget/meta`, `months/YYYY-MM`, `years/YYYY`), replacing what was there.

## Reporting

After an update, say where things stand in two or three sentences, from the script's summary:

> November so far: $2,463 spent of $3,090 planned. Utilities is over. Two purchases need sorting, and thirteen are my guesses.

Then, if the user is present: when anything needs sorting, ask about the first merchant; when there are guesses, offer once: "Say 'review your guesses' whenever you'd like to check them." Do not comment on whether the spending is good or bad.

When the user asks a money question ("what did I spend on eating out this year?"), update the figures if the transactions have changed, then answer from them, naming the period. If the answer depends on transactions not yet brought in, say which statements are missing.

## In a scheduled run

Only if the profile's `money.on` is true. Bring in transactions (Tiller: read again; statements: whatever the filing run added), sort them as "In a run nobody is watching" says, run the script, update the page. Never ask. End the reply with one line the morning brief can read: how many transactions are still unsorted and how many are Carson's guesses.

## At the turn of the year

In January, offer to start the new year's budget by copying last year's plan into `budget-YYYY.csv` for the new year, with a new, empty transactions file. Carrying over starts again from zero. Last year's files stay as they are.
