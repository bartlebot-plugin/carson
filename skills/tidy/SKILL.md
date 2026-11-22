---
name: tidy
description: >
  This skill should be used when the user says "tidy up", "check my folders",
  "is everything filed properly", "clean up", "organize my Carson folder", or
  "what did the tidy find", and when Carson's scheduled weekly routine runs. It
  checks that the Carson folder is in order and accurate, fixes small things in
  Carson's own notes, and lists everything else for the user to decide.
metadata:
  version: "0.2.0"
---

# Tidy

Keep the Carson folder accurate, so what the notes say matches what is in the folders.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory). Tidying never deletes anything.
2. Read the `files` skill (`../files/SKILL.md`).
3. In the Carson folder, read `_system/settings.md`, the user's profile, `_system/filing-protocol.md`, `_system/people.md`, and `_system/notebook.md`.

If the Carson folder cannot be seen, write nothing, say so in one sentence, and stop.

## What to check

1. **The inbox.** Items sitting in `_inbox/` and in `_inbox/needs-a-look/`, and how long each has been there.
2. **Documents with no record.** Files in the topic folders that have no line in the log: the user probably put them there by hand. They are not wrong; they are simply not in the index notes yet.
3. **Names.** Files in the topic folders whose names do not follow the household's pattern.
4. **Misplaced documents.** A document whose kind plainly belongs to a different folder under the filing protocol.
5. **Index notes against folders.** A line in an index note that points to a file that is no longer there, and a filed document with no line in its topic's index note.
6. **Summary notes.** An important document (per the filing protocol) with no summary note beside it, and a summary note whose document is gone.
7. **Key dates.** Dates in `Reference/Key dates.md` that have passed.
8. **Suggestions.** Lines in `_system/pending.md` older than 30 days, or whose date has passed.
9. **Duplicates.** Two files in the topic folders that are the same document.
10. **Empty folders** created during filing and never used. Report only; they do no harm.
11. **Second copies made by a syncing service,** in a shared household: a note or paper whose name carries "conflicted copy" or a bracketed number beside an identical name. Never merge or remove one. List both names and say which is newer.
12. **Offers nobody answered,** in a shared household: lines in any member's pending list marked "offered by" that are older than 30 days or whose date has passed. Report the count only; each member's list is their own.

**When the household kept its own layout** (`storage.layout: own` in the settings note), papers that were there before Carson are not faults: skip checks 2, 3, and 4 for any file with no line in the log, and never list an old file's name or place as something to fix. Mention once, at most, how many papers have not been gone through, and that "go through my … folder" will note them.

**House procedures.** Anything listed under "Leave alone" in `_system/procedures.md` belongs to the household's own routines: never list it, move it, or rename it.

Do not open and reread every document. Work from names, the log, and the notes, and open a document only to settle a specific question.

## What tidy may fix by itself

Only Carson's own notes, and only these:

- Move passed dates in `Reference/Key dates.md` under a "Past" heading.
- Put each index note's lines in order and update its "Last updated" line.
- Add a line to an index note for a filed document that is in the log but missing from the index, taking the facts from the log line and the summary note. If neither has the facts, list it for the user instead.

Everything else is listed, not done: renaming, moving, indexing a hand-filed document, removing an index line, handling duplicates.

## In a live conversation

1. Say in one or two sentences how things stand: "Everything is in order," or "Mostly in order. Four things to look at."
2. Give the list, most useful first, as short numbered lines in plain words ("Two files in your Home folder aren't in my notes yet").
3. Ask about one group at a time: "Shall I add those two to my notes?" Do what is approved, the way the files skill and the file skill describe. A hand-filed document is indexed by reading it and writing its index line and, where the protocol calls for one, its summary note; it is not moved or renamed without a yes.
4. Finish with one line saying what was done.

## In a scheduled run

Never ask. Make the fixes allowed above. Write everything else to `_system/tidy-report.md`, replacing the previous report's contents with the new list and its date, under the heading "Tidy report." If there is nothing to report, write "Everything is in order" and the date. The morning brief tells the user a report is waiting.

End the run with a three-line summary: what was fixed, how many things need the user, and whether the inbox has items waiting.

## The processed folder

Carson never empties `_processed/`. When it holds more than about 200 items, mention once in the report that the user may delete old originals there themselves if they wish, since every one of them has a filed copy.
