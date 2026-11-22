---
name: desk
description: >
  This skill should be used when the user says "show me my desk", "open my
  desk", "Carson's Desk", "my home page", "refresh my desk", "update my desk",
  or "build my desk", and after Carson files documents, gives a brief, or
  changes a todo, when the user has a Desk. It builds and refreshes Carson's
  Desk: a private page showing today's appointments, todos to tick off,
  suggestions to answer, coming dates, and recently filed documents.
metadata:
  version: "0.14.2"
---

# Carson's Desk

The Desk is a private page the user can open any time to see where things stand, tick off todos, and answer Carson's suggestions with Yes or No. For people who use Carson's own list, a second view on the same page, "All todos," shows the whole list and lets them add, change, and remove todos. For people who use Carson's own date book, a view called "All dates" does the same for every coming date. The page itself never changes; Carson fills it by writing to the page's own database.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory).
2. Read the `files` and `tasks-and-dates` skills (`../files/SKILL.md`, `../tasks-and-dates/SKILL.md`).
3. In the Carson folder, read `_system/settings.md` and the user's profile in `_system/users/`. The Desk's address is `desk.url` in the profile; empty means no Desk has been built.

## Tools this needs

- A tool that publishes an artifact page from a file, and sets what the page may use (its capabilities).
- A tool that reads and writes an artifact page's database.

Their names differ between Claude apps; look through the available tools for them. If either is missing in this conversation, do not improvise another kind of page. In a live conversation say "I can't update your desk from here," and carry on with the rest of the task. In a scheduled run, skip the Desk without comment.

## The source of truth

The Desk is a display, not the record. The records are the user's todo app (or `_system/todos.md`), their calendar (or `_system/dates.md`), `_system/pending.md`, `Reference/Key dates.md`, and the log. Every refresh first carries the user's ticks and answers from the Desk back into those records, then rewrites the Desk from them.

Replacing or removing entries in the Desk's database is not deleting anything of the user's: they are copies. The house rule against deleting applies to the user's files, mail, tasks, and events, not to these copies.

## Building the Desk (first time)

1. Publish `desk-template.html` from this skill's folder, exactly as it is, as a new private page titled "Carson's Desk".
2. Set the page's capabilities:
   - always `db`, with default rules;
   - when the profile's `todos.app` is `todoist`, also `mcp` for the Todoist connector, limited to the two tools `find-tasks` and `complete-tasks`, and a third, `find-activity`, when any weekly goal is tied to a Todoist task (the page reads that task's ticks with it). If a goal is tied later, set the page's capabilities again with all three before refreshing; the user may be asked once more to allow the page to use Todoist. Use the connector's display name exactly as it appears among the user's connectors.
3. Record the page's address in the profile as `desk.url`.
4. Refresh it (below), so it never opens empty.
5. Tell the user, briefly: "Your desk is ready. You can open it any time to see what's on, tick things off, and answer my suggestions." Suggest they keep it handy in whatever way their Claude app offers (a pin or favorite); do not invent menu names.

The page is private to the user. Never share it, publish it to the web, or change who can see it. If the user wants someone else to see it, sharing is theirs to do from the page.

With Todoist, the first time the user opens the page on each device, Claude asks them to allow the page to use Todoist. Tell them to choose Allow. If the todos do not appear on one device when they do on another, the cure is usually to reload the page there once; say so before trying anything else.

## Keeping the page itself up to date

The page is a copy of `desk-template.html` made when it was built, so a newer Carson may carry a newer template. The profile records which one the page has, as `desk.template` (the `version` at the top of this file when the page was last published). At each refresh, if `desk.template` is missing or differs from this file's version, publish `desk-template.html` again to the same page, exactly as it is, keep the page private, set its capabilities again as in step 2 above, and record the new `desk.template`. The page's database is untouched by this.

## Refreshing the Desk

### Step 1: Carry the user's answers and ticks back

Read the Desk's database before writing anything.

- **Answers.** For each entry in `waiting` whose `answer` is `yes` or `no`:
  - `yes`: add the todo or event with the tasks-and-dates skill, unless the entry says `added: true` (the page already added it to Carson's list; then make sure `_system/todos.md` has it). The user's Yes on the Desk is their approval; do not ask again.
  - `no`: drop the suggestion.
  - Either way, take its line out of `_system/pending.md`.
- **The user's changes to their list,** only when `todos.app` is `list`. On the page's "All todos" view the user can add, change, tick, and remove todos; each change they make stamps the entry with `changed_at`. `_system/todos.md` is the record, so bring it into line before rewriting anything. Find each entry's line in `todos.md` by the entry's `was` field (the title and due date Carson wrote at the last refresh), never by its current title, which the user may have changed. For each entry in `todos`:
  - `removed: true`: move its line in `todos.md`, unchanged, under a heading "Removed" at the end of the file, adding ` | removed YYYY-MM-DD`. Do not erase the line. Then delete the entry from the page's database. The user's click on the page is their decision; do not ask again.
  - `by: user` with no `was`: the user added it on the page. Add a line for it to `todos.md` under "Open" (or "Done" if they have already ticked it).
  - `changed_at` later than the Desk's last `updated_at`: the page is newer. Change the line in `todos.md` to match the entry's title, due date, project, person, and status (done, or open again).
  - Otherwise `todos.md` is newer or the same; leave the line alone.
  With Todoist, ticks go straight to Todoist and the page has no "All todos" view; there is nothing to carry back.
- **The user's changes to their date book,** only when `calendar.app` is `datebook`. On the page's "All dates" view the user can add, change, and remove dates, and each change stamps the entry with `changed_at`. `_system/dates.md` is the record. Work exactly as for the list above, on the entries in `book`: find each line by the entry's `was` field (the day, time, and title Carson wrote at the last refresh); `removed: true` moves the line, unchanged, under a heading "Removed" at the end of the file with ` | removed YYYY-MM-DD` added, and the entry is then deleted from the page's database; `by: user` with no `was` is a new line; a `changed_at` later than the Desk's last `updated_at` means the line is changed to match the entry's day, time (the entry's `sort`), title, and place. With Google or Outlook the page has no "All dates" view.

- **Goal taps,** only when `goals` is among the profile's `desk.sections`. `_system/goals.md` is the record (see the goals skill, `../goals/SKILL.md`). For each entry in `goal_log`: with `removed: true`, take the matching line (same goal and day) out of the Log if it is there, then delete the entry from the page's database; otherwise, if the Log has no line for it yet, add one (`YYYY-MM-DD | goal name`). Count entries, not days: two entries for one goal on one day are two lines. Entries dated before last Monday that are already in the record are deleted from the page's database.

Mention in one line what was carried back ("I've added the two you approved, and noted the three changes you made to your list and the date you added"), when in a live conversation.

### Step 2: Rewrite the Desk

Write these, replacing what was there. Give each entry a stable id made from its content (letters, digits, hyphens), so a refresh updates entries instead of piling up copies, and remove entries that are no longer current.

| Where | One entry per | Fields |
|---|---|---|
| `desk/meta` | (single) | `name` (what Carson calls the user), `todo_app`, `calendar_app`, `people` (names from the people list), `updated_at` (now, with the local time zone offset); with Todoist also `todoist_show` (`project`, `chosen`, or `all`, from the profile), `todoist_project_id`, when `chosen` also `todoist_projects` (a list of `id` and `name` for every project to show: each chosen project and, where the profile says so, its current sub-projects, looked up at this refresh; at most 20; the page shows tasks only when overdue or due through the coming Sunday, whatever project or list they come from), and `todoist_server` (the connector's display name) |
| `events` | only when `calendar.app` is `google` or `outlook`: event today, tomorrow, or the day after | `day` (YYYY-MM-DD), `time` ("2:30 pm", or empty), `sort` ("14:30"), `title`, `short` (two or three words), `where` |
| `dates` | key date in the next 60 days | `day`, `what` |
| `filed` | document filed in the last 7 days | `day`, `title` (what it was), `where` (folder words: "Home, Utilities") |
| `waiting` | unanswered suggestion in `_system/pending.md` | `kind` (`todo` or `event`), `title`, `detail` ("Due by Tue, Dec 15"; for something another member offered, add "Offered by Pat"), `from`, `answer` (empty); for a todo, also `todo`: `title`, `short`, `due`, `project`, `who`, `from` |
| `todos` | only when `todos.app` is `list`: every open todo, whatever its date, and each one done in the last 14 days. Nothing under "Removed" | `title`, `short`, `due` (YYYY-MM-DD or empty), `project`, `who`, `from`, `status` (`open` or `done`), `done_at`, and `was`: the `title` and `due` exactly as written now, so the line can be found again after the user edits the entry. Write no `changed_at`, `by`, or `removed`; those are the page's. Keep an entry's id the same from one refresh to the next, including ids the page made (they begin `u-`) |
| `book` | only when `calendar.app` is `datebook`: every date in `_system/dates.md` dated today or later. Nothing under "Past," "Removed," "Moved to," or "Left here" | `day` (YYYY-MM-DD), `sort` ("14:30", or empty when there is no time), `time` ("2:30 pm", or empty), `title`, `short`, `where`, `from`, and `was`: the `day`, `sort`, and `title` exactly as written now. Write no `changed_at`, `by`, or `removed`. Keep an entry's id the same from one refresh to the next, including ids the page made (they begin `u-`). The page takes "Today and tomorrow" from these, so write no `events` |
| `goals` | only when `goals` is among `desk.sections`: one per line under "Goals" in `_system/goals.md` | the document id is a short plain name for the goal that never changes ("cardio"); `name`, `target` (times a week, a number), `order`; and, for a goal tied to a Todoist task, `todoist_task_id` (the page then counts that task's ticks itself) |
| `goal_log` | only with goals: each Log line in `_system/goals.md` from this week | `goal` (the goal's document id), `day` (YYYY-MM-DD), `at` (the day again, or the time if known). Keep the ids of entries the page made (they begin `u-`); add entries only for Log lines the page does not already have. Never add an entry for a Log line ending `via Todoist`; the page counts those from Todoist itself, and an entry would count it twice. Write no `removed` or `by` |

**Which sections show.** `desk/meta` also carries `sections`: the list in the profile's `desk.sections`. "To do" and "Waiting for your answer" always show and are not in the list. The choices are `events` (today and tomorrow), `dates` (coming renewals and expirations), `filed` (filed this week), and `goals` (this week's goals). If the profile has no `desk.sections`, write `["events", "dates", "filed"]`. Do not write the collections for a section the user has turned off. When the user says "I don't need … on my desk" or "add … to my desk," change `desk.sections` and refresh.

Rules for what goes on the Desk:

- Dates are the user's local calendar dates, written as YYYY-MM-DD. Never convert them through another time zone.
- Keep text short and plain. No account, policy, or ID numbers, not even shortened ones; no health details; no amounts beyond what a todo's title needs.
- `short` is the two-or-three-word name used in the summary line: "water bill", "furnace visit".
- With `todos.app: none`, write no todos; the page hides that section.

## When to refresh

- When the user asks.
- At the end of a filing run, a brief, or any change to a todo, an event, or a suggestion, if the profile has a `desk.url`.
- In scheduled runs, if the tools are there.

Do not announce routine refreshes. If the user asks to see the Desk, refresh it and give them its address.

## If something is wrong with the page

If the user says the Desk looks broken or will not load, check that the page still exists and has its capabilities. Republish `desk-template.html` to the same page if it has been changed, set the capabilities again, and refresh. Never build a second Desk while `desk.url` points to a working one.
