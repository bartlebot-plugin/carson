# Carson's settings for this household

These are the household-wide choices made during setup. Each person's own choices (their email, calendar, todo list, and how Carson should behave for them) are in their profile in the `users` folder beside this file.

To change anything, say "set up Carson" and Carson will walk you through it.

```yaml
carson:
  version: "0.15.2"        # the Carson version that wrote this file
  set_up_on: ""           # date setup finished (YYYY-MM-DD)
  setup_step: 0           # last setup step finished; lets setup resume
  stopped_on: ""          # date the user paused or stopped Carson; empty while Carson is in use
  stopped_how: ""         # "paused" or "stopped"

household:
  mode: solo              # solo = one person runs Carson | shared = several people each run their own Carson on this folder
  head: ""                # the owner: the person who set Carson up, and who changes settings and the filing rules
  members: []             # shared only: everyone who runs Carson here, by the name Carson calls them, owner first
  invited: []             # shared only: people the owner has added who have not joined yet
  shared_calendar: ""     # shared only: the name of a calendar every member can see; empty = none
  several_people: false   # true when Carson files paperwork for more than one person

storage:
  mode: folder            # folder = a folder on this computer | drive = a folder in Google Drive
  layout: carson          # carson = folders Carson built | own = the user's own folders, kept as they were
  old_folder: ""          # where the user's old papers are, when Carson is to copy them in (bring-in skill)
  reference_name: "Reference"   # the folder for Carson's index notes; differs only when the user already had a "Reference" folder
  drive:                  # Drive mode only: the Drive IDs recorded at setup, so Carson need not search for them
    carson_folder: ""
    inbox: ""
    needs_a_look: ""
    processed: ""
    system: ""
    log: ""
    users: ""
    reference: ""
```

## Folders chosen in setup

(Setup lists the topic folders here, one per line.)
