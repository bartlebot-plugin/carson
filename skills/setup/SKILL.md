---
name: setup
description: >
  This skill should be used when the user says "set up Carson", "start Carson",
  "get started", "change my Carson settings", "add a folder", "change my email,
  calendar, or todo app", "turn on the email address for Carson", "stop Carson", "pause Carson", "turn
  Carson off", "remove Carson", "share Carson with", "add someone to Carson", or
  "join Carson", or asks to redo or continue setup. It runs the
  first-time setup interview that creates the Carson folder, reopens it later to
  change any choice, and pauses or stops Carson when asked.
metadata:
  version: "0.12.0"
---

# Setup

Walk a new user through setting up Carson, one question at a time, and build their Carson folder from the answers. The user may never have used Claude before and may be nervous. Success means they finish without having to understand anything technical.

**Plugin file paths.** This skill's base directory is shown when it loads. The plugin root is two levels above it. `references/…` in this file means this skill's own `references` folder; "plugin references" means `<plugin root>/references/`.

## Before anything else

1. Read `<plugin root>/references/house-rules.md` and follow it throughout.
2. Read the `files` skill (`../files/SKILL.md`). Every folder and file in setup is created the way it describes.
3. Read `references/interview.md`. It holds the exact words, choices, and what to record at each step.

## Step 0: Find out where things stand

Check the folder the user has chosen for this conversation.

| What is found | What to do |
|---|---|
| No folder is connected | Say: "First I need a folder to keep your paperwork in. Please choose a folder for this conversation, ideally a new empty one called Carson, and then say 'set up Carson' again." Stop. |
| The folder is empty, or holds only an empty `_inbox` | First-time setup: run Steps 1 to 10. |
| The folder has `_system/settings.md` with `set_up_on` empty | Setup was interrupted. Say "Welcome back. We stopped partway; let's pick up where we left off," and resume at the step after `carson.setup_step`. |
| The folder has `_system/settings.md` with `set_up_on` filled, `household.mode: shared`, and the person in this conversation has no profile | Someone is joining a shared household. Follow Part 2 of `references/sharing.md`. Work out who they are as `<plugin root>/references/shared-households.md` describes; never assume they are the owner. |
| The folder has `_system/settings.md` with `set_up_on` filled | Setup is done. Go to "Changing things later." If `carson.stopped_on` is also filled, Carson was paused or stopped: say "Welcome back. Your files are just as you left them," and ask whether to start the routines again before anything else (see "Pausing or stopping Carson"). |
| The folder has other files in it and no `_system` | The user may already keep their papers here. Run Steps 1 to 10; the question in "Papers the user already has" settles what to do with them. If they answer "starting fresh" there, say: "This folder already has things in it. I work best in a folder of my own." Ask whether to (a) use a new empty folder instead (recommended), or (b) set up here anyway. On (b), create Carson's folders alongside what is there and never move, rename, or change the existing files. |

Never run first-time setup over an existing Carson folder.

## Steps 1 to 10: The interview

Follow `references/interview.md` step by step:

1. Welcome and ground rules
2. You and your household
3. Your folders
4. Your apps
5. How Carson should behave
6. An email address for Carson (Gmail only in this version)
7. Your routines
8. File one thing together
9. Your desk
10. Wrap-up

Hold to these throughout:

- **One question per message.** Never stack two questions. Use tappable choices where the question tool is available.
- **Never show the machinery.** No paths, file names, setting names, or tool names in what is said to the user, except the names of their own folders.
- **Never guess an answer.** If the user skips a question, take the stated default and say which was taken.
- **Save as you go.** Write what was learned after each step and raise `carson.setup_step`.
- **Do not offer what this version cannot do.** First-time setup is for one person; sharing with others in the household comes afterwards ("share Carson with…", see "Sharing with the household"). A budget is not part of first-time setup; if asked, say "Once we're finished here, say 'set up my budget.'" If asked, say "That's coming in a later version."
- **Keep the pace gentle.** After Steps 3 and 5, say in one line how far along they are ("Halfway there").

## Where the papers will live (asked during Step 1)

Carson can keep the household's papers in one of two places. Settle this straight after the user acknowledges Step 1, before creating anything.

Always put the choice to the user in plain words, and always say what the computer option costs. Most people do not realize that a folder on a computer ties Carson to that computer:

> Where shall I keep your papers? There are two ways, and the difference matters.
>
> **In your Google Drive.** I can reach your papers from anywhere, so you can use me from your phone, and my morning and evening routines run on their own. No computer has to be left on.
>
> **In a folder on this computer.** Your papers stay on your own machine. But I can only reach them, and my routines only run, while this computer is switched on, awake, and connected to the internet, with the Claude app open. If it is off or asleep, I can't file anything or brief you, from here or from your phone.
>
> Which would you like?

- If a folder on the user's computer is attached to this conversation, offer both, with the computer folder first. If they choose it, record `storage.mode: folder` and carry on. If they choose Google Drive, follow the Drive steps below and leave the attached folder alone.
- If no folder is attached (the usual case on a phone or in a browser), offer both, with Google Drive first.
  - **Google Drive:** connect Google Drive and Google Docs (see "Connecting an app"), and prove each with one harmless read. Then ask: "I'll make a folder called 'Carson' in your Drive for everything. Is that all right?" Creating it is a change to their account, so create it only after this yes. If a folder with that name is already there, ask whether to use it or choose another name; never create a second. Record `storage.mode: drive`.
  - **A folder on my computer:** say "Open the Claude desktop app on that computer, choose a folder for Carson with Add folder, and say 'set up Carson' there." Stop.

Do not steer the choice. Some people want their papers on their own machine and accept the cost; say the cost once, clearly, and respect the answer. If the user later asks why a brief did not arrive or why Carson can't see their folder, and they are in folder mode, the first thing to check and say is whether that computer was on, awake, and online.

In Drive mode, read the files skill's `references/drive-mode.md` before building anything. Everything below is built the same way, with these differences: notes are Google Docs; the settings note is the Doc named `Carson settings`; there is no `CLAUDE.md`; and when the fixed folders are created, their Drive IDs are recorded in the settings note's `storage.drive` block.

Tell the user once, in Drive mode: "For my routines to work on their own, the Google Drive and Docs tools need to be allowed to act without asking each time. You can change that in Claude's settings for each tool."

## Papers the user already has (asked straight after the storage choice)

Read `references/existing-papers.md` and ask its one question before building anything. It has three answers: starting fresh (the ordinary interview); keep my folder as it is (Carson works inside the user's own layout and changes nothing in it); or organize it for me (Carson builds a new folder and later copies the old papers in with the bring-in skill, leaving the old folder untouched). The reference says how Steps 0, 3, and 10 change for each.

## Building the folder

**As soon as Step 1 is acknowledged,** create the fixed folders and `_system/settings.md` (from the plugin template), so every later step has somewhere to save:

1. The fixed folders: `_inbox`, `_inbox/needs-a-look`, `_processed`, `_system`, `_system/log`, `_system/users`, `_system/_queue`, `Reference`.

**During Step 3,** create the rest, in this order:

2. The topic folders the user chose, using `references/folder-menu.md` for each one's subfolders. Follow its "by person" and "one per thing" rules. Create only the folders it says to create at setup; filing creates the rest when they are first needed.
3. One index note in `Reference/` per chosen topic that has one, from `<plugin root>/references/templates/index-note.md`, plus `Reference/Key dates.md` with the heading "Key dates" and one line explaining that Carson lists renewals, expirations, and deadlines here, soonest first.
4. In `_system/`, from the plugin templates:
   - `filing-protocol.md`, with one "where things go" line for each kind of document in each chosen topic, written from the folder menu and using the user's actual folder and person names
   - `people.md` (if Step 2 has not already written it)
   - `notebook.md`, containing the heading "Carson's notebook" and one line: "Corrections and lasting preferences, one dated line each."
   - `pending.md`, containing the heading "Waiting for an answer" and one line: "Suggestions Carson has made that have not been answered yet."
   - `proposals.md`, containing the heading "Carson's suggestions" and the line "No suggestions."
   - `tidy-report.md`, containing the heading "Tidy report" and the line "No report yet."
   - `todos.md` and `dates.md`, each with a heading and no entries. Create them now even if another app is chosen later; they stay empty unless Carson's own list or date book is in use.
5. `CLAUDE.md` at the top of the Carson folder, from `<plugin root>/references/templates/claude-md.md`, with every `{GOES_BY}` replaced. If a `CLAUDE.md` is already there and Carson did not write it, do not replace it: tell the user and ask.

Fill every `{PLACEHOLDER}` in a template before saving it. No file may be left with a placeholder or an example line from the template in it.

## Connecting an app (during Step 4)

For Gmail, Outlook, Google Calendar, or Todoist:

1. Check whether tools for that app are already available in this conversation. If they are, go to step 3.
2. If not, search the connector registry for the app by name and show the user its connect card. Say: "Tap Connect and sign in. Tell me when you're done." Wait. If the tools still are not available after they say done, say so plainly, record the app as not chosen (`none`, `datebook`, or `list`), and move on. They can connect it later with "set up Carson."
3. Prove it works with one harmless read, as the interview describes. Never write anything to the app during setup, except creating the Todoist project the user has just approved.

Read only what the test needs. Do not browse the user's mail, calendar, or tasks.

## Setting up a routine (during Step 7)

**In folder mode,** Carson cannot create a scheduled task itself: a task made from a conversation does not keep hold of the user's folder. The user creates each one in the Claude desktop app, with Carson guiding. This is the most technical part of setup, so go slowly. The numbered steps below are for folder mode.

**In Drive mode,** no folder has to be attached, so Carson can create the task itself when this conversation has a tool for scheduling tasks. For each routine the user chose: say what it will do and when, ask "Shall I set that up?", and create it only after a yes, with the routine's instructions from `<plugin root>/references/scheduled-tasks/drive/` and the user's time and time zone. Save a copy of the instructions in `_system/scheduled-task-prompts/` as in folder mode. If there is no scheduling tool, say that routines can't be set up from here yet, record them as off, and move on. These routines run in the cloud; nothing has to be switched on.

For each routine the user chose:

1. Copy its instructions, unchanged, from `<plugin root>/references/scheduled-tasks/` (`morning.md`, `evening.md`, `weekly.md`, or `hourly-mail.md`) into `_system/scheduled-task-prompts/` in the Carson folder.
2. Guide the user through making the task, **one step per message**, waiting for "done" each time. The words on their screen may differ a little from these; if the user describes something different, go with what they see, and never insist on a label.
   1. "On the left side of the Claude window, find **Scheduled** and click it."
   2. "Click **New task**."
   3. "Click **Set up manually**."
   4. "Give it a name: **Carson morning**." (Or Carson evening, Carson weekly, Carson mail.)
   5. "In the box for instructions, paste the text below." Show the routine's instructions in a block they can copy, and nothing else in that message.
   6. "Set how often it runs:" daily at their time; weekly on their day; or hourly.
   7. "Click **Advanced options**, and turn on **Require this computer**." This must be done before the folder is chosen.
   8. "Now choose the folder: pick your Carson folder."
   9. "Save it."
   10. "Now open the task and run it once, so Claude can ask for any permission it needs. If it asks to use your folder or your computer, say yes."
3. Check that the run worked. Morning: `_system/log/briefs.md` has a new line. Weekly: `_system/tidy-report.md` carries today's date. Evening and hourly: ask the user what the run said. If the run could not see the folder, have the user open the task, confirm that Require this computer is on under Advanced options and that the Carson folder is chosen, and run it again. If it fails twice, have them remove the task and make it again from step 1; if it still fails, say plainly that this routine is not working yet, record it as off, and move on.
4. Record the routine in the profile's `routines` block.
5. Tell the user once: "This runs only when this computer is switched on, awake, and connected to the internet, with the Claude app open. If the computer is off or asleep at that time, the routine is skipped; the next one catches up."

Changing a routine's time later is done by the user in the same Scheduled screen; update the profile to match.

**Older instructions.** The instructions are one line naming the routine; the steps live in the routines skill, so they never need pasting again. Whenever setup is opened, compare each file in `_system/scheduled-task-prompts/` with the plugin's copy (in Drive mode, the copy under `drive/`). If one differs, the user's task still holds older, longer instructions that miss newer steps. Say so once: "Your Carson weekly task has older instructions. Replacing them takes a minute, and you won't need to do it again." Then replace the file, show the new text in a block, and guide them: open **Scheduled**, open the task, replace the instructions with the new text, save.

## Changing things later

When setup is already complete, ask: "What would you like to change?" and offer:

- My folders (add one, or tell Carson where a kind of paper should go)
- My apps (email, calendar, todo list)
- How Carson behaves (asking first; how much to say)
- The people, pets, home, or vehicles on file
- The email address for sending Carson documents
- My routines (the morning briefing, the evening look back, the weekly check)
- My desk (build it, if there isn't one yet)
- My budget (handled by the money skill)
- Share Carson with someone in my household (the owner only)
- Pause or stop Carson

Then run only the matching part of the interview, and update the matching files. When a todo or calendar app changes, follow "When the user changes apps" in the tasks-and-dates skill before finishing: open todos and coming events are never left behind without asking. Check the same section every time the apps part is opened, even if nothing is changed: it also covers items left behind by an earlier change.

Never recreate or overwrite existing folders or notes. Adding a folder adds its index note and its "where things go" lines; it changes nothing else.

## Sharing with the household

Several people in one household can each run their own Carson on the same folder. The owner opens it up ("share Carson with Sam"); the other person then says "set up Carson" on their own Claude account and joins with a short interview. Follow `references/sharing.md` for both parts, and `<plugin root>/references/shared-households.md` for how a shared household works afterwards. Carson never shares the folder or invites anyone itself; the owner does that in Google Drive or their syncing service.

In a shared household, "Changing things later" changes only this person's own choices, unless this person is the owner.

## Pausing or stopping Carson

When the user says "stop Carson," "pause Carson," "turn Carson off," or asks how to remove it. Be matter-of-fact; do not try to talk them out of it.

1. Ask which they mean, in plain words: **Pause for now** (the routines stop; everything else stays ready) or **Stop using Carson**.
2. Say first what will not change, whichever they choose: "Your documents and notes stay exactly where they are. Nothing is deleted. Your todos and calendar events stay in your apps."
3. **Turn off the routines.** List the routines the profile says are on.
   - Drive mode, when this conversation has a tool for scheduled tasks: find the tasks Carson created (their names begin "Carson"), name them, ask "Shall I turn these off?", and on a yes pause them (for a pause) or remove them (for a stop). Never touch a task Carson did not create.
   - Folder mode, or no such tool: guide the user, one step per message: "On the left side of the Claude window, find **Scheduled** and click it." Then, for each task whose name begins "Carson": open it, and pause it or delete it. Go with what they see on their screen; never insist on a label.
   - Until the tasks are off, Carson's routines keep running. Say so if the user stops partway.
4. Set every entry in the profile's `routines` block to off, and record the date in `_system/settings.md` as `carson.stopped_on`, with `carson.stopped_how: paused` or `stopped`. Add a line to the log.
5. **Only when stopping,** say what is left for them to do if they wish, and that none of it is required:
   - The Desk and the Budget page are private pages in their Claude account. They stay until the user deletes them; give their addresses.
   - The plugin can be removed where they added it, under Customize, then Plugins.
   - The contact named "Carson" in their address book, if they made one.
   - With Tiller or other apps connected for Carson alone, they can disconnect them in Claude's settings.
   - Their Carson folder is theirs to keep, move, or delete. The filed documents are ordinary files and need nothing from Carson to open.
6. Close in one sentence: "Carson is paused. Say 'set up Carson' whenever you'd like it back." (Or "Carson is stopped.")

**Starting again.** When the user returns and wants the routines back, set them up as in Step 7 for the routines they choose, then clear `carson.stopped_on` and `carson.stopped_how`.

## If something goes wrong

- A folder or file cannot be created: stop, say in one sentence what could not be done ("I wasn't able to create your folders"), and suggest closing and reopening the conversation with the folder chosen again. Do not carry on with half a folder.
- The user seems lost or tired: offer to stop. "We can stop here. Everything so far is saved. Say 'set up Carson' when you'd like to finish."
