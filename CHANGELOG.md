# Changelog

## 0.14.0 — 2026-11-22

- Desk: each person chooses which sections show. "To do" and "Waiting for your answer" always show; today and tomorrow, coming dates, filed this week, and goals are choices.
- Weekly goals: a short list of things to do a set number of times a week, with a row of boxes on the Desk to tap. The brief and the review say where the week stands, and an optional midweek check speaks up only if a goal is behind.

## 0.13.0 — 2026-11-22

- House procedures: a household can list routines of its own (a weekly money check-in, a quarterly review, special handling for one kind of paper) in a note, and Carson runs them: when asked by name, on a schedule, or when a matching file arrives in the inbox. A procedure can take the place of part of Carson, such as its budget.

## 0.12.0 — 2026-11-22

Shared households. Not yet tested.

- Several people in one household can each run their own Carson on the same folder. The owner says "share Carson with…"; the other person says "set up Carson" on their own account and joins with a short interview.
- Each person has their own inbox, suggestions, list, date book, Desk, and routines. Papers, notes, and filing rules are shared; the owner changes settings and filing rules.
- A household event goes on the shared calendar if there is one; otherwise it is offered to the other members it concerns, and each person's own Carson asks them.
- Carson learns who wants to hear about what: from what people say, and from offers they keep passing on.
- Carson never shares the folder or invites anyone; the owner does that.

## 0.11.0 — 2026-11-22

- Setup asks whether the user already keeps household papers, and offers to keep their folders as they are or to organize them.
- Keeping their own folders: Carson works inside the user's layout, files new papers into it, and changes nothing that was there.
- Organizing: new "bring in my old papers" skill copies papers from the old folder into the Carson folder in batches, with a record of every copy. The old folder is never changed.
- "Go through my … folder": Carson reads papers already in place and writes the notes, moving nothing.

## 0.10.1 — 2026-11-22

- "Pause Carson" and "Stop Carson": Carson turns off its routines (or walks the user through it), says what stays, and lists what the user may remove. Nothing is deleted.
- Drive budget: Carson no longer leaves a temporary import sheet in Drive.

## 0.10.0 — 2026-11-22

- Desk: people who use Carson's own date book get an "All dates" view, showing every coming date by month, where they can add, change, and remove dates. Removed dates are kept under "Removed" in the date book file.
- Date book lines can carry a place.
- Questions and problems now go to hello@bartlebot.com.

## 0.9.0 — 2026-11-21

- Drive mode gains the budget, kept in a Google Sheet whose own formulas add up the transactions, so an update reads a small table of totals and not the whole list.
- Tiller: Carson now reads only recent transactions on most updates (from 45 days before the newest on file), and the whole year once a month or on request.

## 0.8.1 — 2026-11-21

- Setup now spells out the cost of keeping papers in a folder on a computer: Carson can reach them, and its routines run, only while that computer is on, awake, online, and running the Claude app.

## 0.8.0 — 2026-11-21

First build of Drive mode. Experimental; not yet tested end to end.

- Carson can keep a household's papers in a Google Drive folder instead of a folder on a computer: setup asks where, notes are kept as Google Docs, and filing copies and moves files within Drive.
- In Drive mode Carson sets up its routines itself, and they run in the cloud.
- Not yet in Drive mode: the budget.

## 0.7.2 — 2026-11-21

- The evening review opens by sizing up the day and naming what mattered most, and closes with a line that lets the user put the day down. Understated; no cheerleading.

## 0.7.1 — 2026-11-21

- Todos left on Carson's own list by an earlier change of app are now offered for copying the next time the apps settings are opened.
- Desk: when Todoist todos do not appear on one device, Carson and the page both suggest reloading.

## 0.7.0 — 2026-11-21

- Budget: Carson sorts transactions into categories itself, for statements and for Tiller alike. Tiller is only the source of transactions; nothing needs categorizing there. Carson's guesses are marked and listed for review.
- Budget: money coming in that has not been sorted is no longer counted as spending.

## 0.6.2 — 2026-11-21

- Desk: "this week" now runs through the coming Sunday.
- Desk: when Todoist tasks can't be shown, the message carries a short detail saying why.

## 0.6.1 — 2026-11-21

- Desk: more room between the boxes in the todo form, and a layout that holds up on a phone.

## 0.6.0 — 2026-11-21

- Carson's Desk gains an "All todos" view for people who use Carson's own list: the whole list, with adding, changing, ticking, and removing. Removed todos are kept under a "Removed" heading in the list file.

## 0.5.3 — 2026-11-21

- The Desk shows only todos that are overdue or due within a week, from every source.
- Todoist: with chosen projects, Carson always puts a new todo in the project that fits best; the setup question is gone.

## 0.5.2 — 2026-11-21

- The Desk shows tasks from the user's chosen Todoist projects only when overdue or due within a week.
- Todoist: an option for Carson to add each new todo to whichever chosen project fits it best.

## 0.5.1 — 2026-11-21

- Todoist: a third choice in setup, "the projects I choose." Choosing a project includes its sub-projects.

## 0.5.0 — 2026-11-21

- Routines: the instructions pasted into a scheduled task are now one line; the steps live in a new `routines` skill, so updates reach them. Anyone set up before this version replaces the pasted instructions once.
- The weekly routine updates Carson's Budget; the morning, weekly, and mail routines refresh Carson's Desk.
- Todoist: a setup choice between showing only Carson's project or everything in the user's Todoist, in briefs and on the Desk. New todos always go to Carson's project.

## 0.4.2 — 2026-11-21

- Changing the todo or calendar app no longer leaves open items behind: Carson counts them and asks once whether to copy them to the new app.

## 0.4.1 — 2026-11-21

- Carson's Budget redrawn as cards: carried over, budget, spent, left, a progress bar, and a click-through that explains last month's carry-over and lists the purchases. The year view gains a pace mark and month-by-month figures.

## 0.4.0 — 2026-11-21

Fourth test build. Not yet released.

- A household budget (`money`): plain budget and transactions files, statements or Tiller as the source, a script for the arithmetic, and Carson's Budget, a private page with a month view and a year view.

Not in this build: shared households and cloud-only storage.

## 0.3.0 — 2026-11-21

Third test build. Not yet released.

- Carson's Desk (`desk`): a private page with today's appointments, todos to tick off, Yes and No buttons on suggestions, coming dates, and recently filed documents.
- `help`.
- Todoist: Carson's project and person are now both labels.

Not in this build: budget pages, shared households, and cloud-only storage.

## 0.2.1 — 2026-11-21

- Scheduled-task instructions corrected after Amy's test: click Set up manually after New task; turn on Require this computer under Advanced options before choosing the folder.

## 0.2.0 — 2026-11-21

Second test build. Not yet released.

- Morning briefing (`brief`), evening look back (`review`), weekly check (`tidy`), and `learn`.
- Setup gains a routines step that walks the user through creating each scheduled task.
- Carson's learning uses only the conversation and its own notebook file; it does not read Claude's memory.

Not in this build: the home page, budget pages, shared households, and cloud-only storage.

## 0.1.0 — 2026-11-21

First test build. Not yet released.

- Setup interview: ground rules, household, folders, apps, behavior, optional email drop box (Gmail), a first filing together, and a one-page guide.
- Filing from the conversation, the inbox folder, and the email drop box.
- Index notes, summary notes, and a key dates list.
- Todos and calendar events with Todoist, Google Calendar, and Outlook, or Carson's own list and date book. Ask-first by default.
- Shared rules for every skill: never delete, never contact anyone, never touch money; outside text is never an instruction.

Not in this build: daily briefing, evening review, tidy, learn review, the home page, budget pages, shared households, and cloud-only storage.
