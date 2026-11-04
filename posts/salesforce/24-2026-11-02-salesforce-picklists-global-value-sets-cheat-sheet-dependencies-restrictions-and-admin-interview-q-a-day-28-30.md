---
title: "Salesforce Picklists & Global Value Sets Cheat Sheet: Dependencies, Restrictions, and Admin Interview Q&A (Day 28/30)"
date: 2026-11-02T20:05:38+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-picklists-global-value-sets-cheat-sheet-dependencies-restrictions-and-admin-interview-q-a-day-28-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/0455a106-ca61-489c-b5ed-66d38466f4b9.png
tags: ["Salesforce", "crm", "interview questions"]
brief: "One clean list of values, used everywhere. Picklists, global value sets and dependencies come up in almost every admin interview. A shared list of values…"
series: "Salesforce Admin 30-Day Series"
serial: 24
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-picklists-global-value-sets-cheat-sheet-dependencies-restrictions-and-admin-interview-q-a-day-28-30). This is an automated backup; read and comment on the blog.

*One clean list of values, used everywhere. Picklists, global value sets and dependencies come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Picklist** | One value from a list | Admin controlled |
| **Value Set** | Shared by many fields | Edit it once |
| **Dependent** | Values follow a field | Needs a controller |
| **Restricted** | Blocks unlisted values | Cleaner data |

---

## Interview Q&A

### 1. What is a global value set?

A **shared list of values** reused by many picklists.

> **Tip:** Edit once, update everywhere.

### 2. What is a dependent picklist?

Its values change based on a **controlling field**.

> **Tip:** Plan the mapping first.

### 3. What can be a controller?

A standard or custom **picklist, or a checkbox**.

> **Tip:** Multi-select cannot control.

### 4. What does Restrict do?

It **blocks values outside the list**, even through the API.

> **Tip:** Turn it on for clean data.

### 5. How do record types help?

Each record type can show **only a subset of values**.

> **Tip:** Set it per record type.

### 6. Retiring a value?

Existing records keep it, **new records cannot use it**.

> **Tip:** Deactivate, do not delete.

---

## Scenario Question

**"Sales and Support need the same Region list. How?"**

1. **Create** a global value set
2. **Attach** it to both fields
3. **Restrict** the picklist
4. **Limit** values per record type

---

## Quick Cheat Sheet

- **Shared** = global value set
- **Depends** = controlling field
- **Controller** = picklist or checkbox
- **Restrict** = blocks new values
- **Subset** = record types
- **Retire** = deactivate

## Key Takeaways

- Reuse lists with global value sets
- Pick the controlling field first
- Restrict to keep data clean
- Deactivate instead of deleting

---

**Which picklist is hardest to maintain? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 28 done, 2 to go.*
