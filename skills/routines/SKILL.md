---
name: routines
description: >
  This skill should be used when a scheduled task says "Run Carson's morning
  routine", "Run Carson's evening routine", "Run Carson's weekly routine", or
  "Run Carson's mail check", and when the user asks to run one of Carson's
  routines now. It holds the steps of each routine, so the short instructions
  pasted into a scheduled task never need changing when Carson is updated.
metadata:
  version: "0.8.0"
---

# Carson's routines

A scheduled task carries only one line naming a routine. The steps live here. Follow the steps for the routine that was named, and no other.

Read `<plugin root>/references/house-rules.md` first (the plugin root is two levels above this skill's base directory).

## Rules for every routine

- In a scheduled run nobody is watching. Never ask a question; follow each skill's instructions for a scheduled run or "a run nobody is watching."
- The Carson folder is the folder attached to the task, or, for a household that keeps its papers in Google Drive, the Drive folder found the way the files skill describes. If the folder cannot be reached, change nothing anywhere, say so in one sentence, and stop.
- In a shared household (`household.mode: shared` in the settings note), first work out whose run this is, as `<plugin root>/references/shared-households.md` describes; the task's instructions normally say "This run is for <name>." In the weekly routine, the tidy and learn steps run only for the owner.
- If one step fails, say which one in a sentence, and carry on with the next step.
- The reply is what the user reads afterwards. Keep it short, and leave out any account of how the run went unless something failed.

## Morning routine

1. Use the brief skill, following its instructions for a scheduled run: first put away anything waiting in the inbox folder and the email drop box, then gather.
2. Refresh Carson's Desk with the desk skill, if the profile has a `desk.url`.
3. Reply with the morning brief.

## Evening routine

1. Use the review skill. Change nothing.
2. Reply with the evening review.

## Weekly routine

1. Use the tidy skill, following its instructions for a scheduled run.
2. Use the learn skill, following its instructions for a scheduled run.
3. Only if the profile has `money.on: true`: use the money skill, following its instructions for a scheduled run, which updates Carson's Budget.
4. Refresh Carson's Desk with the desk skill, if the profile has a `desk.url`.
5. Reply with a short summary of each step that ran.

## Mail check

1. Use the file skill, following its instructions for a run nobody is watching, on the inbox folder and the email drop box.
2. If nothing was waiting, reply "Nothing new" and stop.
3. Otherwise refresh Carson's Desk, if the profile has a `desk.url`, and reply with one line per document filed.
