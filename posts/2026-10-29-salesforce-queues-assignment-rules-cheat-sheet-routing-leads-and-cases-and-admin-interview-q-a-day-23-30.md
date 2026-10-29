---
title: "Salesforce Queues & Assignment Rules Cheat Sheet: Routing Leads and Cases and Admin Interview Q&A (Day 23/30)"
date: 2026-10-29T12:22:43+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-queues-assignment-rules-cheat-sheet-routing-leads-and-cases-and-admin-interview-q-a-day-23-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/ce3e14b7-d115-4ddb-a089-5708be00f5a6.png
tags: ["Salesforce", "Salesforce Admin", "crm"]
brief: "Every lead and case needs an owner. Queues hold them, rules route them. Queues and assignment rules come up in almost every admin interview. A shared owner…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-queues-assignment-rules-cheat-sheet-routing-leads-and-cases-and-admin-interview-q-a-day-23-30). This is an automated backup; read and comment on the blog.

*Every lead and case needs an owner. Queues hold them, rules route them. Queues and assignment rules come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Queues** | Shared record owner | Members claim records |
| **Assignment Rules** | Leads and cases only | Entries run in order |
| **Rule Entries** | Criteria then assignee | First match wins |
| **Activation** | One active per object | Tick the box to apply |

---

## Interview Q&A

### 1. What is a queue?

A **shared owner** that holds records until a member claims them.

> **Tip:** Records wait in it.

### 2. Who can be queue members?

**Users, roles, public groups** and more.

> **Tip:** Add groups, not people.

### 3. Which objects get rules?

Assignment rules work for **leads and cases only**.

> **Tip:** Not custom objects.

### 4. How do rule entries work?

Entries run in order and the **first match assigns** the record.

> **Tip:** Order matters.

### 5. How many rules can be active?

**One active** assignment rule per object at a time.

> **Tip:** Activate one at a time.

### 6. Why did a record skip the rule?

The **assign using active rules** box was not ticked.

> **Tip:** Tick it when saving.

---

## Scenario Question

**"New web leads must route to regional teams. How?"**

1. **Create** a queue per region
2. **Add** rule entries by country
3. **Activate** the lead rule
4. **Test** with a sample lead

---

## Quick Cheat Sheet

- **Queue** = shared owner
- **Rule** = leads, cases
- **Entry** = criteria + owner
- **Order** = first match
- **Active** = one rule
- **Checkbox** = apply rule

## Key Takeaways

- Queues stop records going unowned
- Order entries specific to general
- Add a catch all entry
- Test before you activate

---

**Queue or direct owner? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 23 done, 7 to go.*
