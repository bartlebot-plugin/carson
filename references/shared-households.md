# Shared households

Read this whenever `_system/settings.md` says `household.mode: shared`. It applies on top of every Carson skill. In a household where one person runs Carson (`solo`), ignore this file.

In a shared household, several people each run their own Carson, on their own Claude account, all working in one Carson folder. Each person has their own apps, inbox, todos, suggestions, Desk, and routines. The papers, the notes about them, and the filing rules are shared.

## Who am I working for?

Settle this before anything else, every time. The members are listed in the settings note as `household.members`; each has a profile in `_system/users/`.

1. If the instructions for this run name the person ("This run is for Sam"), it is that person.
2. Otherwise, if an email or calendar tool is connected and reports which account it belongs to, match that address against `user.email_addresses` in the profiles.
3. Otherwise ask, once, at the start of the conversation: "Who am I speaking with?" and offer the members' names, plus "Someone new."
   - "Someone new": run the setup skill's joining steps.
4. In a scheduled run that names nobody and matches nobody: change nothing, say "I couldn't tell whose routine this is," and stop.

From then on, "the user" and "the profile" in every skill mean that person and their profile. Call them by their own name.

## What is each person's own, and what is shared

| A skill says | In a shared household it means |
|---|---|
| the profile | this person's profile, `_system/users/<name>.md` |
| `_inbox/` | the owner: `_inbox/` itself. Every other member: `_inbox/<name>/` |
| `_system/pending.md` | the owner: that file. Every other member: `_system/users/<name>/pending.md` |
| `_system/todos.md` | the same pattern: the owner's stays where it is; a member's is `_system/users/<name>/todos.md` |
| `_system/dates.md` | the same pattern |
| the email drop box | this person's own, from their profile |
| the Desk, the routines | this person's own |

The owner is the person named in `household.head`. Their files stay where a one-person household keeps them, so nothing has to move when a household starts sharing.

Everything else is shared, and every member's Carson reads and writes it directly: the topic folders and every filed paper, `Reference/` and its index notes and key dates, `_system/filing-protocol.md`, `_system/people.md`, `_system/preferences.md`, `_system/notebook.md`, `_system/household.md`, `_inbox/needs-a-look/`, `_processed/`, and the log.

Never read or write another member's inbox, todos, date book, or profile. The one exception is leaving an offer in their `pending` file (below).

## Who may change what

- **Settings and the filing rules** (`_system/settings.md`, `_system/filing-protocol.md`, the folder list) are changed only when working for the owner. For anyone else, say "That's one for <owner> to change," and, if they wish, note their request in `_system/notebook.md` for the owner's Carson to raise.
- **A correction to how something was filed** can come from anyone: write it in the notebook as usual, with their name.
- **Each person's own choices** (their apps, routines, how Carson speaks to them) are theirs alone.
- **`_system/household.md`** (who hears about what): any member may change the lines about themselves. Lines about someone else are changed by that person or the owner.

## Writing shared notes when others may be writing too

Two people's Carsons may work in the folder on the same day. Collisions are rare; keep them harmless.

- Read a shared note immediately before changing it, and change only the lines concerned. Never write a shared note back from a copy read earlier in the conversation.
- Put the person's name on every log line and notebook line.
- A paper is filed once. Before filing, check the log for the same document filed by someone else today; if it is there, do not file it again.
- If the folder holds a second copy of a note that a syncing service made (its name carries words such as "conflicted copy," or a number in brackets), never merge or remove it. Leave both, and report it; tidy lists these for the owner.

## Offering things to other members

One person's Carson cannot reach another person's calendar or todo list. It can leave them an offer, which their own Carson shows them. An offer is a line in the shared folder, not a message; it does not break the rule against contacting anyone.

### The shared calendar, when there is one

If `household.shared_calendar` names a calendar, and this person's calendar app can see a calendar of that name, an event for the household goes on it, once (after the usual asking-first). Check first that another member's Carson has not already added it. Nobody else needs an offer; they will see it there. If this person's Carson cannot see that calendar, treat them as having no shared calendar.

### Otherwise: who is offered what

Read `_system/household.md`. Its "Who hears about what" lines are the household's own rules and come first. Where no line covers the case:

| The event or todo is for | Offer it to |
|---|---|
| A child, a pet, the home, a vehicle, or everyone | **Events:** every member who runs Carson. **Todos:** only the person filing, unless they say who else |
| One member who runs Carson | That member. If that is not the person filing, the person filing is not offered it unless they ask |
| Someone who does not run Carson and is not a child (a parent whose papers the household keeps) | The person filing |

### How an offer is made

- **In a live conversation,** the suggestion line says who else will be offered it, so the user can change that before saying yes: "Calendar: Soccer game, Saturday at 10:00 (I'll offer it to Sam too)." If they say "not Sam," leave Sam out. If they say something lasting ("Sam doesn't need the practices, only the games"), that is a rule: see "Learning who hears about what."
- **In a run nobody is watching,** apply the rules without asking.
- Write one line in each other member's `pending` file, in the usual form, ending ` | offered by: <name>`. Do not add anything to their calendar or todo app.
- An offer is made once. If the same event is already in that member's `pending` file, or the log shows it was offered, do not offer it again.

### When this person has offers waiting

They are in this person's `pending` file like any other suggestion, and are shown with who offered them: "From Pat: Soccer game, Saturday at 10:00. Add it to your calendar?" On the Desk, put "Offered by Pat" in the suggestion's detail. A yes adds it to this person's own calendar or todos. A no drops it, and is noted (below).

## Learning who hears about what

`_system/household.md` holds the household's rules, one plain sentence each, under "Who hears about what." Carson adds or changes a line in three ways:

1. **Someone says so.** "Don't offer me the soccer practices." "Always tell me about anything from the school." "Pat deals with the vet." Say the rule back in one sentence, ask "Shall I make that a standing rule?", and on a yes write the line, with the date and who asked.
2. **A pattern in the answers.** Each time a member says no to an offer, add a notebook line: `<date> | <name> passed on: <kind of thing> (offered by <name>)`. When working for a member in a live conversation, if the notebook shows they have passed on the same kind of thing three times and no rule covers it, ask once: "You've passed on soccer practices three times. Shall I stop offering them to you?" On a yes, write the rule. Either way, mark those notebook lines as dealt with so the question is not asked again.
3. **The learn skill,** in its regular review, treats "who hears about what" like any other lesson, and writes approved rules here.

Write rules by kind of thing and person, never by one event: "Soccer practices → Pat only. Soccer games → Pat and Sam." Keep them few; replace a line instead of stacking a second one on it.

## Routines in a shared household

Each member sets up their own routines, on their own account. The pasted instructions end with one extra line: "This run is for <name>."

- **Morning, evening, mail check:** for this person. The mail check and the morning routine put away this person's inbox and drop box only.
- **Weekly:** the tidy and learn steps run only when the run is for the owner. For anyone else, skip them, and do the rest (their budget, if they keep one, and their Desk).
- A brief or review may mention what another member filed since the last one, when it concerns this person or the whole household: "Pat filed the auto policy renewal."

## Privacy, said plainly

Everyone the folder is shared with can open every paper and note in it. Carson cannot hide one member's papers from another. If asked to keep something private from another member, say so in one sentence and suggest keeping that paper outside the Carson folder. Never promise privacy the folder cannot give.
