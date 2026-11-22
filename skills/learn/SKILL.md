---
name: learn
description: >
  This skill should be used when the user says "learn from this", "remember
  how I like this", "update how you file", "what have you learned about me",
  "review your notes", or "what are your suggestions", and when Carson's
  scheduled weekly routine runs. It turns the corrections in Carson's notebook
  into proposed changes to the filing protocol and the preferences file, and
  applies them after the user agrees.
metadata:
  version: "0.2.0"
---

# Learn

Carson gets better by keeping its own short, readable record of what this household wants. This skill turns day-to-day corrections into standing rules, and keeps those rules few.

Carson learns only from two sources: what the user says in the conversation at hand, and Carson's own files in the user's Carson folder. It does not read Claude's memory or past conversations.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory).
2. Read the `files` skill (`../files/SKILL.md`).
3. In the Carson folder, read `_system/notebook.md`, `_system/preferences.md`, `_system/filing-protocol.md`, and this month's and last month's logs.

## What counts as worth learning

- A correction the user made ("vet bills go under Pets, not Home").
- A lasting preference they stated ("don't suggest a todo for bills on autopay").
- The same question Carson has had to ask more than once ("who is J. Sample?"), which a rule would settle.
- A kind of document that keeps landing in `needs-a-look`.

Not worth learning: one-time instructions, remarks about a single document, anything the user said only in passing, and anything already covered by an existing rule.

## Where each lesson goes

| Kind of lesson | Goes in |
|---|---|
| Where a kind of document belongs; how to name it; whether it gets a summary | `_system/filing-protocol.md`, as a "where things go" line or under "Rules for this household" |
| How Carson should speak or behave; what to suggest or not | `_system/preferences.md`, under "Added since" |
| Who someone is; a new pet, vehicle, or home | `_system/people.md` |
| In a shared household: which member should hear about which kind of event or todo | `_system/household.md`, under "Who hears about what" (see `<plugin root>/references/shared-households.md`, "Learning who hears about what") |

Write each rule as one plain sentence, in words the user would recognize as their own.

## Keeping the rules few

Before proposing a new rule, look for an existing one it should replace or merge with. When proposing, also propose removing:

- a rule the notebook shows the user has since contradicted;
- a rule so narrow it has applied to one document;
- two rules that say the same thing.

`_system/preferences.md` stays within about one page. If it would grow past that, propose what to merge or drop.

## In a live conversation

1. If the user asked about one thing ("learn from this"), deal with that one thing: state the rule in one sentence and ask "Shall I make that a standing rule?"
2. For a fuller review, list the proposed changes as short numbered lines, each saying what would change in everyday words ("Vet bills will go in Pets from now on"). Ask "Shall I make these changes?" with choices: all, let me pick, none.
3. Make only the approved changes, changing lines in place (files skill).
4. In `_system/notebook.md`, move each notebook line that is now covered by a rule under a heading "Now standing rules," so it is not proposed again. Move lines that were declined under "Decided against."
5. Say what changed, in one line.

If `_system/proposals.md` has proposals waiting from a scheduled review, present those first.

## In a scheduled run

Never ask and never change the protocol, the preferences, or the people list. Write the proposals to `_system/proposals.md`, replacing its contents, under the heading "Carson's suggestions" with the date, one numbered line each in everyday words. If there is nothing to propose, leave the file saying "No suggestions" and the date. The morning brief tells the user suggestions are waiting.

## When the user asks what Carson has learned

Answer from `_system/preferences.md` and the "Rules for this household" section of the filing protocol, in a few plain lines. Mention that both are ordinary files in their Carson folder that they can read or change.
