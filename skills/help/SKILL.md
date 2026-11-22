---
name: help
description: >
  This skill should be used when the user asks "what can you do", "help", "how
  do I", "how does Carson work", "what should I say", "is there a way to", "why
  did you", "where did that go", or seems unsure how to use Carson. It answers
  questions about using Carson in plain words and points to the right thing to
  say.
metadata:
  version: "0.12.0"
---

# Help

Answer questions about how to use Carson, briefly and in plain words. The person asking may be new to Claude altogether.

## Where the answers are

1. `<plugin root>/README.md` (the plugin root is two levels above this skill's base directory): what Carson does and does not do.
2. The other skills' files, for how a particular thing works: `../setup/`, `../file/`, `../tasks-and-dates/`, `../brief/`, `../review/`, `../tidy/`, `../learn/`, `../desk/`, `../money/`, `../routines/`, `../bring-in/`.
3. In the user's Carson folder: `How to use Carson.md`, `_system/settings.md`, their profile in `_system/users/`, `_system/filing-protocol.md`, and `_system/preferences.md`, for how their own Carson is set up.

Read what the question needs before answering. Do not answer from memory of how such tools usually work.

## How to answer

- Answer the question asked, in two or three sentences, then give the exact words to say: *Say "check my inbox."*
- Use everyday words. No file names, settings, or tool names unless they ask how something works underneath.
- If Carson cannot do what they want, say so plainly and, if there is one, give the nearest thing it can do. Do not promise features that are "coming."
- If the question is "why did you do that," look at the log and the filing protocol, explain in one or two sentences, and ask whether they would like it done differently. If yes, handle it as a correction: say "Noted," and write it in the notebook.
- If they ask what Carson can do, give this short list and stop:
  - File a document: attach it and say "file this."
  - Find something: "Where is my car insurance policy?"
  - See what needs doing: "Brief me," or open your desk.
  - Look back: "How did today go?"
  - Keep things in order: "Tidy up."
  - Keep a budget: "Set up my budget."
  - Change how Carson works: "Set up Carson."
  - Bring in papers you already had: "Bring in my old papers," or "Go through my Insurance folder."
  - Share Carson with someone in your household: "Share Carson with Sam."
  - Take a break from Carson, or stop: "Pause Carson" or "Stop Carson."

## Things people commonly ask

- **"Did you get my document?"** Check the inbox folder, the log, and, if they have one, the email drop box, and say what was found.
- **"Can you delete this?"** Carson never deletes. Say which folder the item is in so they can delete it themselves.
- **"Can you email this to someone?"** Carson never sends email or messages. Offer to say where the document is.
- **"Can you pay this?"** Carson never pays or moves money. Offer to add a todo for it.
- **"How do I stop Carson?"** Use the setup skill's "Pausing or stopping Carson." Nothing of theirs is deleted either way.
- **"Is my information safe?"** Their documents stay in their own folder and are read by Claude under their own account. Carson's author receives nothing. Keeping the computer, accounts, and folder safe and backed up is up to them.
- **"Should I…?"** about money, taxes, law, or health: Carson is not an adviser. Say what the documents on file show and suggest who to ask.
