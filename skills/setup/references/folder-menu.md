# Folder menu

The starter set of topic folders. Setup offers these, creates the ones the user picks, and writes one "where things go" line per document kind into the filing protocol.

## How to read this menu

- **By person:** when `household.several_people` is `true`, a topic marked "by person" gets one subfolder per person, and the listed subfolders go inside each person's folder. When the household is one person, skip the person level.
- **One per thing:** create one subfolder per vehicle, pet, trip, or project, named as the user names it.
- **At setup, create only the topic folders, the per-person folders, and the one-per-thing folders the user named** (each vehicle, each pet). Do not create the other subfolders listed below. Filing creates each of those the first time a document of that kind arrives, so the user never sees a tree of empty folders.
- The "where things go" lines in the filing protocol name the subfolders anyway, so filing knows where each kind of document belongs.
- Every topic has one index note in `Reference/`, named for the topic.

## The menu

### Home
- Subfolders: Utilities · Repairs and service · Appliances and manuals · Mortgage or Rent (pick one) · Property tax · Improvements
- Index note: Home
- Goes here: water, power, gas, internet, and phone bills; repair invoices; service contracts; warranties and manuals; mortgage or rent statements and the lease; property tax bills; receipts for improvements; homeowner association letters

### Money
- Subfolders: Bank statements · Credit cards · Loans · Investments and retirement · Receipts · Giving
- By person: no (use the account's name in the description)
- Index note: Accounts
- Goes here: bank and card statements; loan statements; brokerage and retirement statements; receipts worth keeping; donation receipts
- Index lines name each account by institution, kind, and last four digits.

### Taxes
- Subfolders: one per tax year, named with the year
- Index note: Taxes
- Goes here: wage and income forms; interest and dividend forms; property tax and donation records for the year; the filed return; letters from the tax office
- File by the year the paper is about, not the year it arrived.

### Insurance
- Subfolders: Home · Auto · Health · Life · Other
- Index note: Insurance
- Goes here: policies, renewal notices, proof-of-insurance cards, claim letters
- Every policy and renewal gets a summary note. Every renewal date goes in Key dates.

### Health
- By person: yes
- Subfolders: Records and results · Bills and claims · Prescriptions
- Index note: Health
- Goes here: visit summaries, test results, vaccination records, medical bills, insurer explanations of benefits, prescription records
- Index lines stay factual and brief: provider, date, what the document is. Do not interpret results.

### Vehicles
- One per thing: one subfolder per vehicle
- Index note: Vehicles
- Goes here: title and registration; inspection and emissions records; repair and maintenance invoices; loan or lease papers
- Registration and inspection dates go in Key dates.

### Pets
- One per thing: one subfolder per pet
- Index note: Pets
- Goes here: vaccination records, vet bills, licenses, microchip papers, adoption papers

### Important papers
- By person: yes
- Subfolders: Identity · Wills and powers of attorney · Property and titles · Contracts
- Index note: Important papers
- Goes here: birth and marriage certificates; passports and licenses (copies); wills, trusts, powers of attorney, health directives; deeds; signed contracts
- Every document here gets a summary note. Ask where the paper original is kept and record that in the index note. Passport and license expiry dates go in Key dates.

### Work
- By person: yes
- Index note: Work
- Goes here: offer letters, pay statements, benefits papers, reviews, retirement plan papers from the employer

### School
- By person: yes
- Index note: School
- Goes here: report cards, enrollment papers, tuition bills, financial aid letters, transcripts

### Travel
- One per thing: one subfolder per trip
- Index note: Travel
- Goes here: tickets, bookings, itineraries, travel insurance, receipts

### Recipes
- Index note: none
- Goes here: recipes, as the user sends them

### Projects
- One per thing: one subfolder per project
- Index note: none (each project folder may hold its own notes)
- Goes here: working papers for anything with a beginning and an end: a move, a renovation, an estate to settle

## Always created

- `Reference/Key dates.md`: renewals, expirations, and recurring deadlines, one line each, soonest first.
- `_inbox/`, `_inbox/needs-a-look/`, `_processed/`, `_system/`, `_system/log/`, `_system/users/`, `_system/_queue/`.

## When a document fits no folder

Do not force it. In a live conversation, ask where the user would look for it, create that folder, and add a "where things go" line to the filing protocol. In a run nobody is watching, move it to `needs-a-look`.
