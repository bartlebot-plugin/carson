# Drive mode: the Carson folder in Google Drive

In Drive mode the Carson folder is a folder in the user's Google Drive, and Carson reaches it through the Google Drive and Google Docs tools (and Google Sheets, for the budget). Nothing is kept on a computer, so Carson works from a phone as well as from a desk.

Everything the other Carson skills say still applies. Wherever a skill names a file or folder by its path (`_system/todos.md`, `Reference/Key dates.md`, `_inbox/needs-a-look/`), find the matching thing in Drive using the rules here. The house rule comes first, as always: **never delete, and in Drive, never move anything to the trash.**

## What becomes what

| In folder mode | In Drive mode |
|---|---|
| A folder | A Drive folder with the same name |
| A note (any `.md` file Carson writes) | A Google Doc with the same name, without `.md`: `Key dates`, `todos`, `2026-11-14 - Water bill (summary)` |
| `_system/settings.md` | A Google Doc named **`Carson settings`**, in `_system`. This exact name is how Carson finds the folder again |
| The user's documents (PDFs, photos, Word files) | The same files, unchanged, in Drive |
| `CLAUDE.md` | Not used. Leave it out |
| `_system/scripts/` | Not used. Scripts run from the plugin's own copy |

Write notes as plain text with Markdown marks (`#` headings, `-` lines), exactly as in folder mode, so the same note reads the same in either mode. Do not use Docs formatting, tables, or checkboxes; the plain marks are what Carson reads back.

## Finding the folder

1. Search Drive for a Google Doc whose title is exactly `Carson settings`, not in the trash.
   - One found: its parent is `_system`, and that folder's parent is the Carson folder.
   - None found, and setup is not running: say "I can't find your Carson folder in Google Drive. If you haven't set Carson up yet, say 'set up Carson.'" and stop.
   - More than one found: do not guess. Tell the user there are two Carson folders, name where each one is, and ask which to use.
2. Read `Carson settings`. Its `storage` block holds the Drive IDs of the Carson folder and each fixed folder (`_inbox`, `needs-a-look`, `_processed`, `_system`, `log`, `users`, `Reference`), recorded at setup. Use those IDs; do not search for these folders again.
3. For any other folder or note, look it up by name inside its parent folder (a search limited to that parent). Remember the IDs found during the conversation and reuse them.

If Drive cannot be reached, write nothing anywhere, tell the user plainly, and stop.

## Drive allows two things with the same name

A local folder cannot hold two files with one name. Drive can, and will, without complaint. So before creating any folder, note, or file, search its parent for that exact name. If it is there, use it; never make a second. If two are ever found, stop and tell the user rather than choosing.

## Reading

- **A note:** read the Doc's text.
- **A document (PDF, photo, scan, Word, spreadsheet):** read its content with the Drive tool that returns a file's text. For a photo or a scan this is text Drive has recognized, and it can be wrong or empty.
  - If a tool is available to bring the file itself into this conversation and the file is small (under about 3 MB), do that as well for a photo or scan, and look at the pages. Check dates, amounts, and names against what is seen.
  - If the text comes back empty or garbled and the pages cannot be looked at, do not file under a guess: treat the document as unreadable, as the files skill says.
  - A document saved with the Drive app's own "scan" button reads much better than a plain photo. When a photo reads badly, say so and suggest scanning it.
- Long codes and numbers read from a photo or scan are shown to the user for checking before use (house rules).

## Naming

The naming rules are unchanged. A document keeps its extension in its title (`2026-11-14 - Water bill.pdf`).

## Filing a document

1. Search the destination folder for the new name (see "two things with the same name").
2. Copy the item into the destination folder with its new title, in one step. Create the destination subfolder first if needed.
3. Confirm the copy: it exists in the destination, with the same size as the original.
4. Move the original, with its title unchanged, into `_processed` by changing its parent folder. If that title is already there, put the date and time in front of it first.
5. Never leave an item in both `_inbox` and its destination, and never move the original before the copy is confirmed.

## Writing and changing notes

- **Create a note** as a Google Doc in the right folder, giving the text in the same call. Then read it back once to confirm it was saved as written.
- **Change, don't retype** applies just as strongly. Change a Doc with small edits, never by replacing its whole text:
  - to change a line, replace that exact line with the new one (match the whole line, case included, so nothing else is touched);
  - to add at the end, insert at the end of the document;
  - to add under a heading in the middle, read the document's structure to find the position, then insert there.
  Put several edits to one Doc in a single request when possible; each request is slow.
- After changing a note, read it back when the change mattered (a date, an amount, a todo). If the text is not what was intended, fix it then, with another small edit.
- An exact-line replacement changes every line that matches. Before using it, make sure the line appears only once; if it appears twice, change it by position instead.
- The user's own files are not Carson's to edit, in Drive as anywhere. Carson changes only its own notes.

## The log

One Google Doc per month, titled `YYYY-MM`, in the `log` folder. Add each line at the end of the document. Never rewrite earlier lines.

## Saving a file that arrives in the conversation or by email

Upload it into `_inbox` in Drive, then file it from there in the usual way.

There is a size limit of about 3 MB on a single upload. If a file is larger, do not shrink it, split it, or try another route. Say: "That file is too large for me to save into your Drive. Please save it into the Carson inbox folder yourself, and tell me when it's there." On a phone, the Drive app's upload or scan button does this.

## Getting papers to Carson from a phone

Tell the user the three ways, whenever it helps:

- Scan a paper with the Drive app straight into the Carson `_inbox` folder (the best quality).
- Save or share any file into that folder.
- Attach it to a message to Carson.

## Unattended runs

A scheduled run works only if the Google Drive, Docs, and Sheets tools are allowed to act without asking each time. If a run stops because a tool asked for permission, say so in the run's reply; the user changes that setting themselves.

## What "never delete" means in Drive

- Never move anything to the trash, and never empty it. Moving to the trash is deleting.
- Moving between folders, renaming, and copying are allowed.
- Never change who a file or folder is shared with. Carson's folder is the user's; sharing is theirs to decide.
