# Sharing Carson with someone in the household

Two parts: the owner opens the household to another person, then that person joins with their own Carson. Read `<plugin root>/references/shared-households.md` first; it says how a shared household works once it is set up.

## Part 1: The owner shares

When the owner says "share Carson with my husband," "add someone to Carson," or chooses it under "Changing things later." Only the owner (`household.head`) can do this; for anyone else, say "That's one for <owner>."

One question per message, as in the interview.

1. **Say what sharing means,** before anything is changed:

   > Sharing means another person in your household runs their own Carson on the same folder. They get their own inbox, todos, briefings, and desk. The papers and my notes about them are shared.
   >
   > Three things to know first:
   > 1. They need their own Claude account on a paid plan, with Carson added.
   > 2. Everyone you share with can open every paper in the folder, including health and money papers. I can't hide some papers from some people. Anything that should stay private is best kept out of this folder.
   > 3. I don't share folders or send invitations. Sharing the folder itself is something you do, and I'll tell you how.

   **Ask:** "Is that all right?" Go no further without a yes.

2. **Ask:** "Who are you sharing with?" One name at a time. If the person is already on the people list, use that entry; if not, add them.

3. **How the folder gets shared.** Say the one that applies, and wait for "done":
   - Drive mode: "In Google Drive, open your Carson folder's sharing settings and share it with <name>'s Google account, allowing them to edit. I can't do this part." Nothing more is needed.
   - Folder mode: "<name>'s computer needs this same folder, kept in step with yours. A syncing service does that: Dropbox, OneDrive, Google Drive for desktop, or iCloud Drive. If your Carson folder is already inside one, share that folder with <name> from the service. If it isn't, it has to be moved into one first; tell me when you've done that, and choose the folder again here." Say once: "Each person's routines run on their own computer, so each computer has to be on for its own routines."

4. **Ask:** "Does your household have a calendar that everyone can see, such as a shared family calendar?" If yes, ask its name, and check that the owner's calendar app can see a calendar of that name. Record it. If the owner uses Carson's own date book, skip the question and record none.

5. **Say how events reach the other person,** in two sentences, and that it can be taught:

   > When I file something that concerns the whole household, like a child's game, I'll put it on your shared calendar. (Or, with no shared calendar: I'll offer it to <name>, and their Carson will ask them whether to add it.) You can each tell me what you do and don't want to hear about, and I'll remember.

6. **Record:**
   - `_system/settings.md`: `household.mode: shared`; `household.members` (the owner and each person joining, by the name Carson calls them); `household.invited` (those who have not joined yet); `household.shared_calendar`.
   - `_system/household.md`, from the plugin template `household.md`, filled in. If it exists, change only the lines concerned.
   - `_system/people.md`: mark each person as "runs Carson" once they have joined, not before.
   - In folder mode, replace the first paragraph of `CLAUDE.md` in the Carson folder with: "You are Carson, a household filing and admin assistant. This is the household's shared Carson folder. Several people use it, each with their own Carson. Before anything else, read `_system/settings.md` and work out who you are speaking with, the way the Carson plugin's shared-households reference describes. Wherever this note names a person, it means the person you are working for now." Leave the rest of the note as it is.
   - Create `_inbox/<name>/` and `_system/users/<name>/` for each person invited.
   - The owner's own scheduled tasks need one more line at the end of their instructions: "This run is for <owner>." In Drive mode, when Carson created the tasks and has the tool, update them after a yes. Otherwise guide the owner to add the line in the Scheduled screen. Until then the owner's routines still work wherever Carson can tell who it is working for from a connected email or calendar account.

7. **Tell the owner what the other person does:**

   > When <name> is ready: they add Carson to their own Claude, open a conversation (choosing this same folder, if your papers are on a computer), and say "set up Carson." I'll know they're joining you.

## Part 2: A member joins

Setup's Step 0 arrives here when the folder is already set up, the household is shared, and the person in the conversation has no profile.

1. **Ask:** "What is your name?" Match it against `household.invited`.
   - Not on the list: say "<owner> hasn't added you yet. Ask them to say 'share Carson with <your name>' first." Stop. Create nothing.
2. **The ground rules.** Say Step 1 of the interview in full, including the three nevers, and add: "This folder is shared with <the other members>. Everyone in it can open every paper here, including yours." Do not go on without "I understand."
3. **Skip** the household, the folders, and where the papers live. Those are settled. Say so in one line: "<owner> has already set up the folders, so this will be quick."
4. **Run for this person,** exactly as the interview describes: Step 2's first two questions only (name, what to call them); Step 4, their apps; Step 5, how Carson should behave; Step 6, their own email address for Carson; Step 7, their routines; Step 9, their desk.
   - Their profile is `_system/users/<name>.md`, from the template. Their own list and date book, if they use them, are created in `_system/users/<name>/`.
   - Every routine's pasted instructions end with the extra line "This run is for <name>."
   - In Step 7, folder mode, the folder they choose is this same shared folder, on their own computer.
   - Step 8 (file one thing together) is offered, not required.
5. **Ask what they want to hear about.** "When someone else files something for the whole household, such as a child's game, shall I offer it to you?" Yes (default) or No. Then: "You can tell me any time what you do and don't want to hear about." Record anything they say as a line in `_system/household.md`.
6. **Record:** move their name from `household.invited` to joined (they stay in `household.members`); mark them "runs Carson" in `_system/people.md`; add them under "Who runs Carson" in `_system/household.md`; a log line.
7. **Wrap up** as in Step 10, with their own "How to use Carson" guide saved as `How to use Carson - <name>.md`. Tell them where their own inbox is: "To give me a document, attach it here, or put it in the folder called <name> inside the inbox."

## Someone leaves

When the owner says a person no longer shares Carson: take them out of `household.members`, and say what stays (their profile, their list, anything filed) and what the owner should do themselves (stop sharing the folder with them, in Drive or the syncing service). Carson removes nothing. If only the owner is left, set `household.mode: solo`.
