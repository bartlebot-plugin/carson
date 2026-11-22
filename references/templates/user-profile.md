# {GOES_BY}'s Carson profile

These are {GOES_BY}'s own choices. To change one, say "set up Carson."

```yaml
user:
  name: ""                # full name
  goes_by: ""             # what Carson calls them
  email_addresses: []     # every address this person sends email from
  acknowledged_on: ""     # date this person tapped "I understand"

email:
  app: none               # gmail | outlook | none
  dropbox_address: ""     # e.g. pat+carson@gmail.com; empty = no email drop box

calendar:
  app: datebook           # google | outlook | datebook (Carson's own list of dates)
  calendar_name: ""       # which calendar Carson adds events to

todos:
  app: list               # todoist | list (Carson's own list) | none
  todoist_project: ""     # the Todoist project Carson adds tasks to
  todoist_project_id: ""  # that project's ID, recorded the first time it is used
  todoist_show: project   # project (only Carson's project) | chosen (the projects listed below) | all (everything in the user's Todoist)
  todoist_show_projects: []   # when chosen: one entry per project, e.g. {name: "Personal", id: "123", with_subprojects: true}

desk:
  url: ""                 # the address of Carson's Desk; empty = not built yet
  template: ""            # the desk skill version whose page template is published

money:
  on: false               # true once a budget has been set up
  source: ""              # statements | tiller
  year: ""                # the budget year in use
  show_detail: true       # true = the budget page lists individual purchases
  page_url: ""            # the address of Carson's Budget
  tiller_spreadsheet: ""  # for Tiller: the spreadsheet's ID
  tiller_full_read_on: "" # for Tiller: the date the whole year was last read (YYYY-MM-DD)
  page_template: ""       # the money skill version whose page template is published
  sheet_id: ""            # Drive mode: the ID of the budget's Google Sheet

behavior:
  ask_first: true         # true = ask before adding a todo or an event
  detail: short           # short | fuller: how much Carson says after filing

routines:
  morning: "off"          # "off", or the time the morning briefing runs, e.g. "08:00"
  brief_email: false      # true = the briefing also mentions emails that need a reply
  evening: "off"          # "off", or the time the evening look back runs
  weekly: "off"           # "off", or the day the weekly check runs, e.g. "Sunday"
  hourly_mail: false      # true = check the inbox and the email drop box every hour
```
