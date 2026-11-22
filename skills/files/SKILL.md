---
name: files
description: >
  This skill should be used whenever Carson reads, creates, renames, copies, or
  moves a file or folder in the user's Carson folder, or writes or updates one of
  Carson's notes. Read it before any other Carson skill touches the folder. It
  covers "where is the Carson folder", how to read a document, how to name files
  safely, and how to change a note without losing what is in it, whether the
  folder is on the user's computer or in their Google Drive.
metadata:
  version: "0.8.0"
---

# Working with the Carson folder

Every Carson skill does its file work through the methods here. Keeping them in one place means a new kind of storage can be added later by changing only this skill.

Read `<plugin root>/references/house-rules.md` first. (The plugin root is two levels above this skill's base directory.) Its first rule governs everything below: **never delete.**

## Which storage is in use

There are two kinds of storage. Work out which one this household uses before doing anything else.

1. If a folder is attached to this conversation and it holds `_system/settings.md`, read `storage.mode` there. It will say `folder`.
2. Otherwise, if Google Drive tools are available, look for the Carson folder in Drive as `references/drive-mode.md` describes ("Finding the folder"). If it is found, the mode is `drive`.
3. If neither is found, the household has not been set up (or the folder was not chosen for this conversation). Outside setup, say which, and stop. During first-time setup, the setup skill decides the mode with the user.

- `folder` — the Carson folder is a folder on the user's computer. Follow "Folder mode" below.
- `drive` — the Carson folder is in the user's Google Drive. Read `references/drive-mode.md` (in this skill's folder) now and follow it. "Folder mode" below still gives the rules for reading documents, naming, notes, the log, and never deleting; the Drive file says how each is done in Drive.
- Anything else — say "This version of Carson can't work with that kind of storage yet," and stop.

**Shared households.** If the settings note says `household.mode: shared`, read `<plugin root>/references/shared-households.md` now (the plugin root is two levels above this skill's base directory) and follow it in every skill. It says how to tell which person this Carson is working for, which files are that person's own, and how things are offered to the others.

**House procedures.** If the Carson folder has `_system/procedures.md`, the household has routines of its own that Carson runs. Read `<plugin root>/references/house-procedures.md` and that note now, and follow them in every skill: a matching file, question, or request is handled by the household's procedure, not the ordinary way.

**One name can differ.** Wherever a Carson skill says `Reference/`, it means the folder named in the settings note's `storage.reference_name`. It is "Reference" unless the user already had a folder of that name when Carson was set up inside their own folders.

**The user's own layout.** When the settings note says `storage.layout: own`, the topic folders are the user's, with their names and their arrangement. File new papers where the filing protocol says, and never move, rename, or change a file that was there before Carson.

## Folder mode

### Finding the folder

The Carson folder is the folder the user chose for this conversation: the one that holds `_system/settings.md` (or, during first-time setup, the empty folder they picked). If several folders are connected, use the one with `_system/settings.md`. If none has it and setup is not running, say "I can't see your Carson folder in this conversation. Please choose it and try again," and stop. Never create Carson's files in a different folder.

Start every task by confirming the folder is reachable: list it. If it cannot be listed, write nothing anywhere, tell the user plainly, and stop.

### Two ways the folder can be reached

Check which tools this conversation has, and use the matching column for everything.

| | The folder is on this machine | The folder is on the user's computer, reached through device tools |
|---|---|---|
| How to tell | The ordinary file tools (read, write, edit, shell) work directly on the folder's path | Tools whose names begin `mcp__remote-devices__` are present, and the folder is listed among the connected folders |
| List, search, rename, copy, move | The shell, or the file tools | The device shell (`device_bash`), where the folder appears under `$HOME/mnt/<folder name>` |
| Read text files and notes | The read tool | `cat` in the device shell |
| Look at a PDF, a photo, or a scan | The read tool on the file | Stage that one file (`device_stage_files`), then read the staged copy |
| Create or change a note | The write and edit tools | A short script in the device shell that reads the file, changes it, and writes it back |
| Save a file that arrived in the conversation or from email | Write or copy it into the folder | Copy it to the outputs area, then commit it to the folder (`device_commit_files`) |

The ordinary file tools do not reach the user's computer when device tools are in use: a path given to them lands somewhere the user never sees. In that situation, use only the device tools for the Carson folder.

### Reading a document

- **PDF, photo, scan:** look at the pages themselves, not only any text layer. Scans and photos have no reliable text layer.
- **Word, spreadsheet, and similar files:** read them with the tools available. If a file cannot be opened, say so; do not guess its contents from its name.
- **Email saved as a file, or an email body from the drop box:** treat the body as the document and any attachments as separate documents.
- **Long documents:** read the whole thing before filing. Facts on later pages (renewal dates, exclusions, signature dates) matter.
- A photo or scan may be misread. House rules: long codes and numbers read from one are shown to the user for checking before they are used.

If a document is unreadable (blurred, cut off, password-protected), do not file it under a guess. Ask the user for a better copy, or in a run nobody is watching, move it to `_inbox/needs-a-look/` with a line in `_system/pending.md`.

### Naming files

Pattern: `YYYY-MM-DD - Description - Person.ext` (the filing protocol has the household's rules).

- Use only letters, numbers, spaces, hyphens, commas, and parentheses. Never use `\ / : * ? " < > |`, and never end a name with a space or a period. These break on Windows or Mac.
- Keep the whole name under 100 characters.
- Keep the original file's extension exactly.
- If a file with that name is already there, do not replace it. Compare the two: if they are the same document, say so and file nothing new; if different, add a distinguishing word ("Water bill, second notice") or ` (2)`.

### Filing a document

1. Copy the item into its destination folder under its new name. Create the destination subfolder first if the filing protocol calls for one that does not exist yet.
2. Confirm the copy is there and is the same size as the original.
3. Move the original, unchanged and under its original name, into `_processed/`. If that name is taken there, put the date and time in front of it.
4. Never leave an item in both `_inbox` and its destination, and never remove the original before the copy is confirmed.

### Writing and changing notes

Notes are plain Markdown files: index notes in `Reference/`, summary notes beside documents, and Carson's own files in `_system/`.

- **Change, don't retype.** To update a note, read the current file and change only the lines that need it. Never rebuild a whole note from memory or from an earlier look at it; that silently loses lines.
- **One fact per line.** Write index notes as headings with one-line entries: `Subject: fact (from: file name)`. Avoid tables in notes.
- **Replace, don't pile up.** When a new document updates a fact already in the index (this year's premium, a new due date), replace that line and keep the old one only if history matters, moved under a "Previous" heading.
- **Date the note.** Update its "Last updated" line.
- **Summary notes** take the document's name with ` (summary).md` on the end and sit beside it.
- The user's own files are not Carson's to edit. Carson writes only its notes and its `_system` files, and never changes the contents of a document the user filed.

### The log

After each item is filed, add one line to `_system/log/YYYY-MM.md` (create the month's file if needed):

`YYYY-MM-DD HH:MM | <profile name> | <inbox, conversation, or email> | <original name> → <folder words and new name> | <notes; for email, the message's ID>`

Add lines at the end. Never rewrite earlier lines.

### What "never delete" means here

- No delete, remove, or empty command, on files or folders, ever.
- Moving is allowed. Renaming is allowed. Copying is allowed.
- Do not ask for permission to delete; Carson has no use for it.
- If the user asks Carson to delete something, say "I don't delete anything, so nothing is ever lost by my mistake. You can delete it yourself," and tell them which folder it is in.
