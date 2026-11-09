---
title: "Salesforce Flow Loop Element Cheat Sheet: Bulk-Safe Collections and Admin II Interview Q&A"
date: 2026-11-09T16:13:57+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-loop-element-cheat-sheet-bulk-safe-collections-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/3e82fdc6-ae52-48f3-bf49-8404cc951deb.png
tags: ["Salesforce", "flow", "120daysofsalesforce", "Salesforce Admin"]
brief: "The Loop element lets a Flow work through a collection one record at a time. Admin II interviews ask about it because loops are where Flows either stay…"
series: "Salesforce"
serial: 31
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-loop-element-cheat-sheet-bulk-safe-collections-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*The Loop element lets a Flow work through a collection one record at a time. Admin II interviews ask about it because loops are where Flows either stay bulk-safe or hit governor limits.*

---

## The 4 Loop Pieces

| Piece | What it does | Key point |
| --- | --- | --- |
| **Collection variable** | Holds the records to process | Often from Get Records |
| **Loop element** | Hands you one item at a time | Exposes the current item variable |
| **Assignment inside** | Changes the current item or builds an output collection | No DML here |
| **Data element after** | Saves the output collection once | One Update Records outside the loop |

---

## Interview Q&A

### 1. What does the Loop element do?

It goes through a **collection** and gives you **one item at a time** as a loop variable. It has two paths: **For Each Item** runs for every item, and **After Last Item** runs once at the end.

> **Tip:** Put the save step on After Last Item.

### 2. Why not put Update Records inside the loop?

Each pass would run **one DML** call. With many records you hit **governor limits** and the Flow fails. Instead, add each changed item to a **second collection**, then update that collection **once** after the loop.

> **Tip:** Never put DML or Get Records inside a loop.

### 3. How do you change a field on the current item?

Use an **Assignment** inside the loop to set the field on the **loop variable**, then **add the loop variable to an output collection**.

> **Tip:** Loop variable in, output collection out.

### 4. Can you loop in reverse?

Yes. The Loop element has a direction setting: **first to last** or **last to first**.

> **Tip:** Use reverse when order matters.

### 5. When can you skip the loop?

Often a Flow does not need one. **Update Records with conditions** can change every matching record in a single element, and a **before-save** flow can set fields on the triggering record directly.

> **Tip:** No loop is the safest loop.

### 6. How do you debug a loop?

Run **Debug** and watch the loop variable change on each pass. Use the Flow's **fault path** and, for large data, test with a small set first.

> **Tip:** Test with 2 records, then 200.

---

## Scenario Question

**"Set every open Opportunity on an Account to Needs Review when the Account is marked At Risk."**

1. **Record-triggered flow** on Account, after save, when `At_Risk__c` becomes true
2. **Get Records:** open Opportunities where `AccountId` equals the Account Id
3. **Loop** through them, with an **Assignment** setting `StageName` and adding each to an output collection
4. **Update Records** on the output collection, once, after the loop

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** and add **Get Records** for a few Contacts into a collection.
2. Add a **Loop** over that collection.
3. Inside the loop, add an **Assignment** that sets the current Contact's Description, then adds it to a new collection.
4. After the last item, add **Update Records** using the new collection.
5. Run **Debug** and check the Contacts in your org.

---

## Quick Cheat Sheet

- **Loop** = one item at a time
- **For Each Item** = runs per record
- **After Last Item** = runs once at the end
- **Output collection** = what you save
- **DML** = outside the loop
- **Often no loop** = Update Records with conditions

## Key Takeaways

- Loop through a collection, build an output collection, save once.
- Never put DML or Get Records inside a loop.
- Skip the loop when one element can do the job.
- Test with small data first.

**Next up:** Flow formulas and how they replace small pieces of logic.

*Part of #120DaysOfSalesforce. Do you try to avoid loops, or use them often? Tell me below.*
