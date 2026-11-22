---
name: tasks-and-dates
description: >
  This skill should be used whenever Carson suggests, adds, finds, completes, or
  changes a todo or a calendar event, and when the user says "add a todo",
  "remind me to", "put it on my calendar", "what's on my list", "what's due",
  "what is waiting for me", "mark that done", or "yes, add those". It tells every
  other Carson skill how to read and write todos and dates for whichever apps the
  user chose in setup.
metadata:
  version: "0.12.0"
---

# Todos and dates

One place for how Carson handles todos and calendar events, so other skills never deal with a particular app directly.

Read `<plugin root>/references/house-rules.md` first (the plugin root is two levels above this skill's base directory), then the user's profile in `_system/users/`. Three settings decide everything here:

- `todos.app`: `todoist`, `list`, or `none`
- `calendar.app`: `google`, `outlook`, or `datebook`
- `behavior.ask_first`: `true` or `false`

## Todo or event?

- **Event:** something that happens at a set time or on a set day, where the user needs to be somewhere or expects something. An appointment, a service visit, a delivery window, a hearing.
- **Todo:** something the user has to do, with or without a due date. Pay a bill, call the insurer, sign and return a form, gather tax papers.
- A deadline for an action is a **todo with a due date**, not an event. Do not create both for the same thing.
- A date worth knowing that needs no action on the day (a policy's renewal date, a passport's expiry, a warranty end date) goes in `Reference/Key dates.md` only. If it calls for an action beforehand, such as paying a premium, that action is a todo.

Suggest only what a document or the user actually calls for. No todo for a paid bill. No event for a date already past. Nothing for the other party's obligations.

## What every todo carries

| Field | Meaning |
|---|---|
| Title | The action, starting with a verb, with the amount or the party when it helps: "Pay water bill, $63.20" |
| Due | A date, or none |
| Project | The topic folder it belongs to (Home, Insurance, Taxes…), or a project the user named |
| Who | The person from the people list it is for. Leave empty in a one-person household |
| From | The filed document it came from |

Events carry a title, a day, a time if there is one, a place if there is one, and the document they came from.

## Asking first

When `behavior.ask_first` is `true` (the usual case), and the user is in the conversation:

1. Finish the filing or the answer first.
2. Then list the suggestions as short numbered lines, in plain words:

   > I'd suggest adding:
   > 1. Todo: Pay water bill, $63.20, due December 5
   > 2. Calendar: Furnace service visit, December 3 at 2:30
   >
   > Shall I add them?

3. Offer choices: **Yes, add them** · **Let me pick** · **No thanks**. On "Let me pick," ask about each one in turn.
4. Add only what was approved. Say what was added, in one line.
5. Anything declined is dropped. Do not suggest it again unless a new document raises it.

If the user does not answer and moves on, write the suggestions to `_system/pending.md` and leave them there.

When `behavior.ask_first` is `false`: add them, then say what was added, in one line.

**In a run nobody is watching:** never ask. With `ask_first: true`, add nothing and write each suggestion to `_system/pending.md`. With `ask_first: false`, add them and record each in the log.

## In a shared household

When the settings note says `household.mode: shared`, follow "Offering things to other members" and "Learning who hears about what" in `<plugin root>/references/shared-households.md`. In short: a household event goes on the shared calendar once, if there is one; otherwise it is offered to the other members concerned, by a line in their own pending list, and their own Carson asks them. Carson never writes to another person's calendar or todo list. Each person's pending list, own list, and date book are their own files, as that reference lists.

## Before adding anything: check for a twin

Look for an open todo or an upcoming event that already covers the same thing (same action and party, or same event and day). If one exists, do not add another. Say "That's already on your list," and update the existing one only if the new document changes its date or amount, after asking.

## The pending list

`_system/pending.md` holds suggestions that have not been answered. One line each:

`- [YYYY-MM-DD] Todo | Pay water bill, $63.20 | due 2026-12-05 | Home | from: 2026-11-14 - Water bill.pdf`

When the user asks "what is waiting for me?" or answers a suggestion later, read the list, present it as in "Asking first," add what is approved, and take answered lines out of the file (approved or declined). Lines whose date has passed are shown once more as "This one has passed. Shall I drop it?"

## Where todos live

### `todos.app: todoist`

- **Where a new task goes:**
  - With `todos.todoist_show: project` or `all` (or the setting missing): the Todoist project named in `todos.todoist_project`, always.
  - With `todos.todoist_show: chosen`: the project that plainly fits the todo, among Carson's project and the chosen projects and their sub-projects, judged by its name against the todo's person and topic (a todo for Skyla goes to a project named Skyla). If none plainly fits, or two fit equally, use Carson's project. Never create a project, and never use one the user did not choose.
  - Name the destination in the suggestion line whenever it is not Carson's project, so the user approves it with the todo: "Todo: Renew lease, due December 5 (in Skyla)". If the user names a different project, use that one, provided it is among the chosen ones.
  - In a run nobody is watching with `ask_first: false`, apply the same rule and record the project in the log.
- **What to read** when telling the user what is due, open, or done (briefs, reviews, "what's on my list?"), by `todos.todoist_show`:
  - `project`, or the setting missing: only tasks in Carson's project.
  - `chosen`: tasks in Carson's project and in each project listed in `todos.todoist_show_projects`. Where an entry says `with_subprojects: true`, look up that project's current sub-projects each time and include them, so one added later is picked up.
  - `all`: every task in the user's Todoist that is overdue or due in the period asked about, plus undated tasks in Carson's project.
  - Tasks Carson did not add are the user's own, whichever project they sit in: read them, complete one when the user says it is done, and otherwise never change them. A task Carson added to one of the user's projects is handled like any other Carson task. Name the Todoist project beside such a task when it helps ("Skyla: renew lease").
- Project → a label with the project's name. Who → a label with the person's name. (Carson's Desk reads both from the labels.)
- Record the Todoist project's ID in the profile as `todos.todoist_project_id` the first time it is used.
- Put the source document's name in the task's description. No account numbers or other private detail in titles.
- Find, complete, and reschedule with the Todoist tools. Reschedule with the tool meant for moving dates, not by rewriting the task.
- Never delete a task. To drop one, ask the user, then complete it or leave it.
- If the Todoist tools are not available in this conversation, add nothing; put the suggestions in `_system/pending.md` and tell the user their Todoist isn't reachable right now.

### `todos.app: list`

Carson's own list is the file `_system/todos.md`. One line per todo, under two headings, "Open" and "Done":

`- [ ] Pay water bill, $63.20 | due 2026-12-05 | Home | Pat | from: 2026-11-14 - Water bill.pdf`

- Add new lines under "Open," soonest due date first; undated ones last.
- To complete one, change `[ ]` to `[x]`, add ` | done YYYY-MM-DD`, and move the line to the top of "Done."
- Change lines in place. Never rebuild the file from memory.
- Carson never removes a todo on its own. When the user asks to remove one, or removes it on the Desk's "All todos" view, move the line under a third heading, "Removed," at the end of the file, adding ` | removed YYYY-MM-DD`.
- The Desk shows what is overdue or due this week, through the coming Sunday; its "All todos" view shows everything, and the user can add, change, and remove todos there. The desk skill carries those changes back into this file.
- This list sends no reminders. Say so once, when the first todo is added: "I'll tell you what's due whenever you ask."

### `todos.app: none`

Add nothing anywhere. Mention what needs doing in the filing report, once, and leave it at that. Do not write these to the pending list.

## Where events live

### `calendar.app: google`

- Add events to the calendar named in `calendar.calendar_name`.
- A day with no time → an all-day event. A time with no stated length → one hour.
- Put the source document's name in the event's description.
- Never delete an event, and never change one Carson did not create, without asking.

### `calendar.app: outlook`

- As for Google, through the Microsoft tools. If all-day events are not offered, use a short event at 9:00 in the morning and say so in its title: "(all day)".

### `calendar.app: datebook`

Carson's own date book is the file `_system/dates.md`. One line per event, soonest first:

`- 2027-01-15 | Auto policy renews | from: 2026-11-21 - Auto policy renewal.pdf`

with the time after the date when there is one (`2026-12-03 14:30`), and the place, when there is one, as a part beginning `at:` before the source (`- 2026-12-03 14:30 | Furnace service visit | at: home | from: …`).

- Leave past entries in place under a "Past" heading.
- Change lines in place. Never rebuild the file from memory.
- Carson never removes a date on its own. When the user asks to remove one, or removes it on the Desk's "All dates" view, move the line under a heading "Removed" at the end of the file, adding ` | removed YYYY-MM-DD`.
- The Desk shows today's and tomorrow's dates; its "All dates" view shows every coming date by month, and the user can add, change, and remove dates there. The desk skill carries those changes back into this file.
- The date book sends no alerts; say so once, when the first date is added.

## When the user changes apps

Do this in two situations, while the user is in the conversation:

- when setup changes `todos.app` or `calendar.app`, straight after the profile is updated;
- whenever setup's apps part is opened and Carson's own list or date book is no longer the app in use but still holds open items that were never offered (lines under "Open" in `_system/todos.md`, or coming dates in `_system/dates.md`, not under a "Moved to," "Left here," or "Removed" heading). This catches a change made before Carson knew to ask.

1. Count what is still open in the old place: open todos, or events dated today or later that Carson added (in Google or Outlook, only events whose description names a source document; never the user's other events). If the old app cannot be read now, say so and say the items are still there.
2. If there are none, say nothing about it.
3. If there are some, ask once, whatever `behavior.ask_first` says:

   > You have 3 open todos on your old list. Shall I copy them to Todoist?

   Offer **Yes, copy them** · **Show me first** · **No, leave them**. On "Show me first," list them in short lines and ask again.
4. On yes, add each one to the new place with its title, due date, project, person, and source document, checking for a twin first. Then deal with the old copies so nothing shows twice:
   - Old place was Carson's own list or date book: move those lines, unchanged, under a heading "Moved to <new app> on YYYY-MM-DD" in the same file. Do not mark them done.
   - Old place was Todoist, Google, or Outlook: leave them exactly as they are, and say so: "I copied them. The originals are still in Todoist; you can complete or remove them there." Carson never deletes or completes them for this.
5. On no, say where they still are, in one sentence, and that the Desk will no longer show them. When they are in Carson's own list or date book, move those lines, unchanged, under a heading "Left here on YYYY-MM-DD", so they are not offered again.
6. Say how many were copied, in one line. Record the move in the log. Refresh the Desk.

Completed todos and past events are never copied. When the new app is `none`, copy nothing; say where the open items still are.

## Keeping the Desk current

After adding, completing, or changing a todo or an event, or answering a suggestion, refresh Carson's Desk with the desk skill if the profile has a `desk.url`. `_system/todos.md` and `_system/dates.md` remain the records of Carson's own list and date book; the Desk shows copies and carries the user's changes back at each refresh.

## Answering "what's on my list?" and "what's due?"

Read the todo app and the calendar for the next seven days (or the period asked about), plus `Reference/Key dates.md` for the next thirty. Answer in short lines, most urgent first: overdue, due today, due this week, then dates coming up. If there is nothing, say "Nothing is due." Mention how many suggestions are waiting in the pending list, if any.

## Checking details

- Take every date and amount from the document. If the document gives a due date in an unusual way ("within 30 days of this notice"), work it out, say how, and ask the user to confirm before adding it.
- Dates are the user's local calendar dates. Never shift a date by converting time zones.
- A long reference or confirmation number read from a scan is not put in a todo or event until the user has checked it (house rules).
