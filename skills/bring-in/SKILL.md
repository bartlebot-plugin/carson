---
name: bring-in
description: >
  This skill should be used when the user says "bring in my old papers",
  "organize my old folder", "copy my old files in", "sort out my old files",
  "keep going with my old papers", "go through my Insurance folder", "go
  through what's already here", or "make notes on my existing papers". It
  copies papers from the user's old folder into the Carson folder in an
  orderly way, leaving the old folder untouched, and it reads through papers
  already in the Carson folder to note what matters.
metadata:
  version: "0.11.0"
---

# Bringing in papers the user already had

Two jobs, both for papers that existed before Carson:

- **Bringing in:** copying papers from an old folder into the Carson folder, each to the right place. For people who asked Carson to organize a messy folder.
- **Going through a folder:** reading papers that are already in the Carson folder and writing the notes, without moving anything. For people who kept their own layout, and for anything brought in by name alone.

Both are slow, careful work done in batches, in a live conversation only. Never in a scheduled run.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory).
2. Read the `files` skill (`../files/SKILL.md`) and the `file` skill (`../file/SKILL.md`). Naming, copying, note-writing, and logging are done their way.
3. In the Carson folder, read `_system/settings.md`, the user's profile, `_system/filing-protocol.md`, `_system/people.md`, and `_system/notebook.md`.
4. Read `_system/log/brought-in.md` if it exists. It is the record of what has been done; never redo a line in it.

## The rule that matters most

**The old folder is read, never changed.** Nothing in it is moved, renamed, edited, or deleted, and nothing is written into it. Carson copies. When everything is done, the old folder is exactly as it was, and deleting it is the user's decision and the user's act.

## Bringing in

### 1. Find the old folder

It is recorded in the settings note as `storage.old_folder`. If that is empty, ask where the old papers are, find the folder, confirm it by naming two or three things in it, and record it. In folder mode it must be attached to this conversation; if it is not, ask the user to add it and stop until they have. It must not be the Carson folder or inside it.

### 2. Size it up, once

List the old folder's files by name, with their folders. Open nothing. Then tell the user, in three or four lines:

- how many files there are, and in how many folders;
- what will be left out and why (see "What is left out");
- that it is done a batch at a time, and they can stop after any batch and pick up another day;
- that the old folder stays untouched.

Ask: "Shall I start?" Offer to begin with the folder they care about most.

### 3. Work one old folder at a time, about 25 files to a batch

For each file, settle where it goes, in this order:

1. **By its name and its old folder,** against the filing protocol's "where things go" lines. A file called "2025 State Farm auto policy.pdf" in a folder called "Insurance" needs no reading.
2. **By reading it,** when the name and folder do not say enough (a scan called "IMG_2231," "Document (3)").
3. **By asking,** when reading does not settle it. Collect these and ask at the end of the batch, one question at a time. Until answered, the file is not copied.

Then copy it into the Carson folder:

- **Name.** Keep the file's own name when it already says what the paper is. Give it Carson's kind of name (date, description, person) only when it was read and its own name says nothing. Never guess a date for a name.
- **Copy, then check.** Copy into the destination, creating the subfolder if needed, and confirm the copy is there with the same size. If a file with that name and size is already in the destination, it is already brought in: skip it and record that.
- **Record it** in `_system/log/brought-in.md`, one line: the date, the old location, the new location, and `read` or `by name`. This file is how the work resumes and how any copy can be traced back.

### 4. Write notes for the papers that matter

Reading every old paper is not worth the time. Read, and write notes for, only:

- the kinds the filing protocol says get a summary note (policies, wills, deeds, titles, tax returns, loan papers), **when they are the current one.** An old policy that has been replaced is copied by name alone;
- anything with a renewal, expiry, or due date still to come, for `Reference/Key dates.md`;
- anything the user asks for.

For these, write the summary note and the index lines exactly as the file skill does (its Steps 5 and 6). Everything else gets no note; its folder and name are its record. Say so once, and say the user can ask for any folder to be gone through later.

**Todos and events:** suggest only for something still to come (a renewal next month). Never for a date that has passed. Follow the tasks-and-dates skill's asking-first rules, and gather the suggestions for the end of the batch.

### 5. After each batch, report and ask

Two or three lines: how many were copied and where the bulk went, how many remain, anything left out. Then any questions, one at a time. Then: "Shall I keep going?" Stop when the user says so; the record means nothing is lost.

### 6. When it is all done

Say so plainly, with the totals: copied, left out, and how many are waiting on a question. Then:

> Your old folder is exactly as it was. Once you're happy with how I've organized things, you can delete it yourself. I never will.

Add a line to the log. Refresh the Desk if there is one.

### What is left out

- Files that are plainly not household papers: photo libraries, music, video, programs, and whole folders of them. Name the folders, do not list the files.
- Files that cannot be opened or copied (too large for the tools in Drive mode, locked, or damaged). List them by name so the user can move them by hand.
- Exact duplicates within the old folder: copy the first, record the others as duplicates.

Left-out files are recorded in `_system/log/brought-in.md` too, with the reason. If the user says a left-out folder should come in, bring it in.

### Size and speed, in Drive mode

Copy within Drive with the copy tool, which does not pass the file through the conversation. A file too large to read is still copied, by name alone. Check for a same-named file in the destination before every copy; Drive allows duplicates.

## Going through a folder

For papers already in the Carson folder with no notes: a household that kept its own layout (`storage.layout: own`), or papers brought in by name alone.

1. The user names a folder ("go through my Insurance folder"). If they say "everything," start with the folder that matters most and work one folder at a time.
2. List its files. Leave out any that already have a line in the log or the index note.
3. Read them in batches of about 15. For each, do the file skill's Steps 3, 5, and 6 only: identify it, write a summary note if the protocol calls for one, and update the index note and the key dates.
4. **Move nothing and rename nothing.** The document stays where the user put it, under the name they gave it. Summary notes go beside the document, as usual.
5. Add a log line for each, marked `noted in place`.
6. If a paper seems to be in the wrong folder, do not move it. Mention it at the end of the batch and ask.
7. Report after each batch as in "Bringing in," and ask whether to keep going.

Suggest todos and events only for what is still to come.
