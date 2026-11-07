---
title: "Salesforce Flow Get Records Cheat Sheet: Filters, Sort Order, Null Checks and Admin II Interview Q&A"
date: 2026-11-07T17:20:59+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-get-records-cheat-sheet-filters-sort-order-null-checks-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/6b2a561e-132c-4284-8ff1-b002709dc391.png
tags: ["Salesforce", "Salesforce Admin", "flow", "120daysofsalesforce"]
brief: "Get Records is how a Flow reads data. Admin II interviews ask about its filters, sort order and null checks because a badly built one is the most common…"
series: "Salesforce"
serial: 29
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-get-records-cheat-sheet-filters-sort-order-null-checks-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Get Records is how a Flow reads data. Admin II interviews ask about its filters, sort order and null checks because a badly built one is the most common cause of slow or broken Flows.*

---

## The 4 Settings That Matter

| Setting | What it controls | Key point |
| --- | --- | --- |
| **Filter conditions** | Which records come back | AND, OR or custom logic |
| **Sort order** | Which record is "first" | Set it whenever you need one record |
| **How many records** | One or many | Only the first record, or all records |
| **Store fields** | What data is kept | Choose only the fields you need |

---

## Interview Q&A

### 1. How do you filter a Get Records?

Add **filter conditions** on the object's fields, such as `Status Equals Open`. Combine them with **All Conditions Are Met (AND)**, **Any Condition Is Met (OR)** or **Custom Condition Logic**.

> **Tip:** Filter in Get Records, not after it.

### 2. Why does sort order matter?

With **Only the first record**, Salesforce returns the first match **in your sort order**. Without a sort, which record you get is not guaranteed.

> **Tip:** Sort by CreatedDate descending for "latest".

### 3. One record or all records?

**Only the first record** stores a single record variable. **All records** stores a **collection** you can loop over.

> **Tip:** Match the choice to the variable you need.

### 4. Which fields should you store?

Choose **only the fields you need** instead of all fields. Fewer fields means less data to carry through the Flow.

> **Tip:** Name the fields you will actually read.

### 5. What if no record is found?

The variable is **empty (null)**. Add a **Decision** after the Get Records that checks whether the variable **Is Null**, and handle that path.

> **Tip:** Always plan the "found nothing" path.

### 6. Why keep Get Records out of loops?

Each Get Records is a **SOQL query**, and a transaction has a limit on queries. A query inside a loop can hit that limit on bulk data.

> **Tip:** Query once before the loop, then loop the collection.

---

## Scenario Question

**"A flow must find the most recent open Case for a Contact and show its subject."**

1. **Get Records** on Case: `ContactId Equals the Contact` AND `Status Does Not Equal Closed`
2. **Sort** by CreatedDate descending, **Only the first record**
3. **Decision:** is the Case variable **Is Null**?
4. **Display** the Subject, or a "No open cases" message

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** and add a **Get Records** element on Case, returning **Only the first record**.
2. Add a filter `Status Does Not Equal Closed` and sort by `CreatedDate` descending.
3. Choose **Choose fields and let Salesforce do the rest** and pick Subject and Status.
4. Add a **Decision** that checks the Case variable **Is Null** and a screen for each path.
5. Run **Debug** with a Contact who has open cases and one who has none.

---

## Quick Cheat Sheet

- **Read data** = Get Records
- **Narrow it down** = filter conditions
- **Pick the first** = sort order
- **A list** = All records (collection)
- **Nothing found** = Is Null Decision
- **Efficiency** = store only needed fields, no queries in loops

## Key Takeaways

- Filter and sort inside Get Records.
- Always handle the nothing-found path.
- Store only the fields you need.
- Query once, then loop.

**Next up:** Update Records and Create Records, and how they save changes.

*Part of #120DaysOfSalesforce. Which Get Records setting trips you up? Tell me below.*
