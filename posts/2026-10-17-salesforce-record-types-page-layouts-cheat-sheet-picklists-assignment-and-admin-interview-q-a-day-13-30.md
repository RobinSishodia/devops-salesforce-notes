---
title: "Salesforce Record Types & Page Layouts Cheat Sheet: Picklists, Assignment and Admin Interview Q&A (Day 13/30)"
date: 2026-10-17T23:00:34+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-record-types-page-layouts-cheat-sheet-picklists-assignment-and-admin-interview-q-a-day-13-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/60506fb3-c59b-48de-8457-eb20f9402e04.png
tags: ["Salesforce", "Salesforce Admin", "record types"]
brief: "One object, many teams. Record types and page layouts show each team the fields, values and process it needs, and they come up in almost every admin interview. The 4 Building Blocks Block What it"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-record-types-page-layouts-cheat-sheet-picklists-assignment-and-admin-interview-q-a-day-13-30). This is an automated backup; read and comment on the blog.

*One object, many teams. Record types and page layouts show each team the fields, values and process it needs, and they come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Record Type** | Splits one object into variants | Own picklists and process |
| **Page Layout** | Fields, buttons, related lists | Assigned by profile |
| **Picklist Values** | Limited per record type | Hide the ones not needed |
| **Assignment** | Profile plus record type | Picks the layout shown |

---

## Interview Q&A

### 1. What is a Record Type?

It lets one object serve different teams, each with its own **picklist values, page layouts and business process**.

> **Tip:** Use it when processes differ.

### 2. What is a Page Layout?

It controls which **fields, buttons, sections and related lists** a user sees on a record.

> **Tip:** Layouts shape the screen, not security.

### 3. How is a layout assigned?

By **profile and record type together**. Each pair gets one page layout.

> **Tip:** Check the assignment matrix.

### 4. How do users get a record type?

Through their **profile or a permission set**. Without access, they cannot pick it.

> **Tip:** Permission sets add types without editing the profile.

### 5. Layout vs field-level security?

A layout only **hides a field on the page**. Field-level security blocks access everywhere, including reports and the API.

> **Tip:** Use FLS to truly protect data.

### 6. Page Layout vs Lightning Page?

Page layouts set **fields and related lists**. Lightning record pages set the **overall page, components and dynamic forms**.

> **Tip:** Name both, then say which you use.

---

## Scenario Question

**"Support handles Billing and Technical cases with different fields. How do you do it?"**

1. **Create** two Case record types
2. **Limit** the Status values for each type
3. **Build** one page layout for each type
4. **Assign** by profile and record type

---

## Quick Cheat Sheet

- **Record type** = variant of an object
- **Layout** = fields and related lists
- **Picklist** = values per type
- **Access** = profile or permission set
- **FLS** = real field security
- **Lightning page** = overall page

## Key Takeaways

- Add types only when processes differ
- Keep layouts simple and few
- Never rely on layouts for security
- Test as a real user

---

**Which object would you split first? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 13 done, 17 to go.*
