---
title: "Salesforce Flow Decision and Assignment Elements Cheat Sheet: Outcomes, Operators and Admin II Interview Q&A"
date: 2026-11-06T16:14:39+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-decision-and-assignment-elements-cheat-sheet-outcomes-operators-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/37320372-06a2-4897-9e7f-f13110315cea.png
tags: ["Salesforce", "Salesforce Admin", "flow", "120daysofsalesforce"]
brief: "Decisions send a flow down the right path. Assignments change values along the way. Admin II interviews ask about both because almost every real Flow uses…"
series: "Salesforce"
serial: 28
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-decision-and-assignment-elements-cheat-sheet-outcomes-operators-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Decisions send a flow down the right path. Assignments change values along the way. Admin II interviews ask about both because almost every real Flow uses them.*

---

## The 2 Elements

| Element | What it does | Key point |
| --- | --- | --- |
| **Decision** | Routes the flow into one path | Outcomes are checked top to bottom, the first match wins |
| **Assignment** | Sets or changes values | Changes variables, not the database |

---

## Interview Q&A

### 1. How does a Decision pick a path?

It checks its **outcomes from top to bottom**. The first outcome whose conditions are met runs. If none match, the **Default Outcome** runs.

> **Tip:** Put the most specific outcome first.

### 2. How can outcome conditions be combined?

Choose **All Conditions Are Met (AND)**, **Any Condition Is Met (OR)**, **Custom Logic** such as `1 AND (2 OR 3)`, or **Always (No Conditions Required)**.

> **Tip:** Use custom logic for mixed AND and OR.

### 3. What does an Assignment do?

It **sets values** on variables, including fields of a record variable such as `{!caseRecord.Status}`. Operators include **Equals**, **Add** and **Subtract**.

> **Tip:** Equals overwrites, Add accumulates.

### 4. Does an Assignment save to the database?

**No.** It only changes values in the flow. Use **Update Records** to save, except for `$Record` in a before-save record-triggered flow, which saves automatically.

> **Tip:** Assignment edits, Update Records saves.

### 5. How do you build up a collection?

Use an Assignment on a **collection variable** with the **Add** operator to put each record in the list. Then use **one Update Records** after the loop.

> **Tip:** Never put DML inside a loop.

### 6. What should the Default Outcome do?

Handle everything **no outcome matched**. Rename it so the path is clear, and leave it connected to something, even a simple end.

> **Tip:** Plan the "none of the above" case.

---

## Scenario Question

**"A record-triggered flow must escalate high-priority Cases from Premium accounts."**

1. **Decision:** Priority equals High AND account type is Premium
2. **Assignment:** set Escalated to true and Status to Escalated on `{!caseRecord}`
3. **Assignment:** add the record to a collection
4. **One Update Records** after the loop, then **Debug**

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** with a **Get Records** for one Case into a record variable.
2. Add a **Decision** with an outcome `High Priority` where Priority equals High, and leave the Default Outcome as `Other`.
3. On the `High Priority` path, add an **Assignment** that sets `{!caseRecord.Status}` to Escalated.
4. Add an **Update Records** element that saves `{!caseRecord}`.
5. Run **Debug** with a High priority Case and then a Low priority Case, and compare the paths.

---

## Quick Cheat Sheet

- **Choose a path** = Decision
- **Change a value** = Assignment
- **Order of outcomes** = top to bottom
- **None matched** = Default Outcome
- **Save changes** = Update Records
- **Add to a list** = Assignment on a collection

## Key Takeaways

- Decisions route, Assignments change values.
- The first matching outcome wins.
- Assignments do not save to the database.
- Keep DML outside loops.

**Next up:** the Get Records element and how filters and sort order work.

*Part of #120DaysOfSalesforce. Which element do you use most? Tell me below.*
