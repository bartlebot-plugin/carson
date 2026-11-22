---
name: goals
description: >
  This skill should be used when the user says "add a weekly goal", "track my
  workouts", "I want to exercise three times a week", "log a workout", "I did
  my cardio", "how am I doing on my goals", "how did I do last month", "change
  my goals", or "stop tracking that", and when Carson's midweek check, a brief,
  or a review needs to know where the week's goals stand. It keeps a short
  list of things the user wants to do a certain number of times each week and
  counts them, with tap-boxes on Carson's Desk.
metadata:
  version: "0.14.1"
---

# Weekly goals

Some people want help keeping a weekly habit: two strength workouts and three cardio sessions, a call to a parent, an hour on the garden. Carson keeps the count. The user taps a box on Carson's Desk each time they do one, or tells Carson, and Carson says where the week stands in the brief, the review, and a midweek check.

This is counting, not coaching. Never give exercise, diet, or health advice, never comment on the user's body or fitness, and never scold. State the count and what is still possible this week.

## Before starting

1. Read `<plugin root>/references/house-rules.md` (the plugin root is two levels above this skill's base directory).
2. Read the `files` skill (`../files/SKILL.md`).
3. In the Carson folder, read the user's profile and `_system/goals.md` if it exists.

## The record: `_system/goals.md`

Created the first time the user asks for a goal. In a shared household each person has their own, beside their own list (see the shared-households reference).

```
# Weekly goals

The week runs Monday to Sunday.

## Goals

- Resistance | 2 a week
- Cardio | 3 a week

## Log

- 2026-11-23 | Cardio
- 2026-11-24 | Resistance

## Past weeks

- Week of 2026-11-16 | Resistance 1 of 2 | Cardio 3 of 3
```

- **Goals:** one line each: the name the user gave it, and how many times a week. Keep the list short; ask before adding a seventh. A goal tied to a Todoist task (below) carries a third part: `| todoist: Cardio Exercise (TASK_ID)`.
- **Log:** one line for each time the user did one, with the day. Only this week's and last week's lines are kept here.
- **Past weeks:** when a week is two weeks gone, replace its log lines with one summary line. Never drop a week.
- A goal the user stops is moved under a heading "Stopped," with the date. Its past weeks stay.

## Adding or changing a goal

Ask only what is missing: what to call it, and how many times a week. Say it back in one sentence and write it after a yes. Then:

- Add `goals` to `desk.sections` in the profile if the user has a Desk and it is not there, and refresh the Desk so the boxes appear. If they have no Desk, say that the boxes live on the Desk and offer to build one; the count still works without it.
- Offer the midweek check once, if `routines.midweek` is off: "Shall I check in midweek and tell you if you're behind?" Set it up as the setup skill's routines step describes, using the `midweek.md` instructions.

## Tying a goal to a Todoist task

Only when the profile's `todos.app` is `todoist`. If the user already ticks a repeating task in Todoist each time they do the thing ("Cardio Exercise"), tie the goal to that task so they never have to record it twice: every tick of that task counts as one.

- Offer it when a goal is added and a repeating Todoist task plainly matches, or when the user asks. Find the task, name it back, and tie it only after a yes. Record the task's name and id on the goal's line.
- Never create, rename, or reschedule a Todoist task for this without asking, as with any Todoist change.
- Say once how to keep the count honest: "Tick it only when you've done it. To skip a day, postpone the task in Todoist; don't tick it."
- Taps on the Desk still count as well, for a session with no task to tick.

**Counting a tied goal.** Each completion of the tied task this week is one, dated by the day it was ticked. Read them from Todoist's activity (completed events for that task since Monday); the list of completed tasks leaves out repeating tasks. When bringing the record up to date, add a Log line for each completion not yet there, ending `| via Todoist`, and take out any `via Todoist` line whose completion is no longer in Todoist (the user un-ticked it). Lines without that ending are taps or things the user told Carson; leave them alone.

## Logging one

- **On the Desk:** the user taps an empty box. The desk skill carries taps into the Log at each refresh ("Carry the user's answers and ticks back").
- **By telling Carson:** "I did my cardio," "log a resistance workout yesterday." Add the line to the Log with that day, add the matching entry to the Desk's `goal_log` if there is a Desk, and reply with the count: "That's two of three for cardio this week."
- A day in the future is not logged. A day in an earlier week is logged to that week.
- Never log one the user did not report. A completed todo or a calendar event is not a report.

## Where the week stands

Used by the brief, the review, the midweek check, and "how am I doing?"

1. **Bring the Desk's taps in first.** If the profile has a `desk.url`, read the Desk's `goal_log` and apply it to the Log as the desk skill describes, so the count is current.
2. For each goal tied to a Todoist task, bring its completions in as "Counting a tied goal" describes.
3. Count this week's Log lines for each goal (Monday through today).
4. Say it in one line, plainly: "Resistance one of two, cardio two of three; three days left." When everything is met: "Both goals met this week." Add nothing else.

**Behind** means, for any goal: nothing logged yet when half the week has gone, or the number still needed is as many as, or more than, the days left in the week including today. Say what is needed, not that the user has failed: "Cardio needs two more, and there are three days left."

## Looking back

"How did I do in October?" Read "Past weeks" and the Log, and answer with the weeks met out of the weeks counted, per goal. No commentary.
