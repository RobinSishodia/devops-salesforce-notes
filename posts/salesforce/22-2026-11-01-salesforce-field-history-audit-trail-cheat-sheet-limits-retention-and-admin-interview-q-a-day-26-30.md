---
title: "Salesforce Field History & Audit Trail Cheat Sheet: Limits, Retention, and Admin Interview Q&A (Day 26/30)"
date: 2026-11-01T17:53:48+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-field-history-audit-trail-cheat-sheet-limits-retention-and-admin-interview-q-a-day-26-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/8f423134-d86f-42c7-99ce-743e5ef94263.png
tags: ["Salesforce", "crm", "interview questions"]
brief: "Prove who changed what, and when. Field History and the audit trails come up in almost every admin interview. It records the old and new values of selected…"
series: "Salesforce Admin 30-Day Series"
serial: 22
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-field-history-audit-trail-cheat-sheet-limits-retention-and-admin-interview-q-a-day-26-30). This is an automated backup; read and comment on the blog.

*Prove who changed what, and when. Field History and the audit trails come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Field History** | Old and new values | 20 fields each |
| **Setup Trail** | Logs admin changes | Last 180 days |
| **Field Audit** | Paid long retention | Up to 10 years |
| **Login History** | Who logged in | Last 6 months |

---

## Interview Q&A

### 1. What is Field History?

It records the **old and new values** of selected fields.

> **Tip:** Turn it on per object.

### 2. How many fields can you track?

**Up to 20 fields** on each object.

> **Tip:** Pick fields that matter.

### 3. How long is history kept?

**18 months in the UI** and 24 months through the API.

> **Tip:** Export what you must keep.

### 4. What is Setup Audit Trail?

It logs **setup changes** and who made them for 180 days.

> **Tip:** Download the CSV to keep it.

### 5. Need longer retention?

**Field Audit Trail** is an add-on: up to 60 fields and 10 years.

> **Tip:** Ask about licensing.

### 6. Which fields cannot be tracked?

**Formula and roll-up summary fields.**

> **Tip:** Track the source fields.

---

## Scenario Question

**"Auditors ask who changed Amount, and when. How?"**

1. **Enable** history on Opportunity
2. **Select** the Amount field
3. **Show** the History related list
4. **Check** Setup Audit Trail

---

## Quick Cheat Sheet

- **Fields** = 20 per object
- **UI** = 18 months
- **API** = 24 months
- **Setup trail** = 180 days
- **Add-on** = 60 fields
- **Formulas** = not tracked

## Key Takeaways

- Track only fields that matter
- Export before data ages out
- Setup Audit Trail covers admin changes
- Use Field Audit Trail for compliance

---

**Which field do you audit most? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 26 done, 4 to go.*
