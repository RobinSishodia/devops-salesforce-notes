---
title: "Salesforce Flow Decisions and Loops Cheat Sheet: Branching, Looping and Admin II Interview Q&A"
date: 2026-11-16T14:12:41+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-decisions-and-loops-cheat-sheet-branching-looping-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/68f3f894-0a91-4f36-bcbf-009cb2157e96.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Almost every real flow is built from two elements: a Decision that chooses a path and a Loop that works through a list. Admin II interviews love them…"
series: "Salesforce"
serial: 36
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-decisions-and-loops-cheat-sheet-branching-looping-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Almost every real flow is built from two elements: a Decision that chooses a path and a Loop that works through a list. Admin II interviews love them, especially the rule about what never goes inside a loop.*

---

## The Two Elements at a Glance

| Element | What it does | Key point |
| --- | --- | --- |
| **Decision** | Sends the flow down one path | Outcomes are checked in order, first match wins |
| **Default outcome** | The path when no outcome matches | Always plan for it |
| **Loop** | Goes through a collection one item at a time | Has a For Each path and an After Last Item path |
| **Assignment** | Changes variable values | Use it inside the loop to build a collection |

---

## Interview Q&A

### 1. How does a Decision pick a path?

It checks its outcomes **from top to bottom** and takes the first one whose conditions are met. If none match, the **Default outcome** runs.

> **Tip:** Put the most specific outcome first.

### 2. Can an outcome have several conditions?

Yes. Combine them with **AND**, **OR** or a **custom logic** such as `1 AND (2 OR 3)`.

> **Tip:** Name outcomes clearly, for example "Has open tasks".

### 3. What does a Loop need?

A **collection variable** to loop over. The loop gives you one record at a time as the **current item**.

> **Tip:** Name the loop after what it holds, such as `Loop_Tasks`.

### 4. What are the two paths out of a Loop?

**For Each Item** runs once per record. **After Last Item** runs once when the loop is done.

> **Tip:** Do the saving after the last item, not during the loop.

### 5. What should you never put inside a loop?

**Create, Update, Delete or Get Records** elements. They run once per item and can hit governor limits.

> **Tip:** Collect changes in a collection, then save once after the loop.

### 6. How do you change records in a loop the right way?

Use an **Assignment** to set the field on the current item, then **add the item to a second collection**. After the loop, run one **Update Records** on that collection.

> **Tip:** Check the collection is not empty before the update.

---

## Scenario Question

**"Close all open Tasks on an Account when the rep clicks a button."**

1. **Get Records** for open Tasks on the Account, storing all records
2. A **Decision** checks that at least one Task was found
3. A **Loop** goes through the Tasks, with an **Assignment** that sets Status to Completed and adds the Task to a collection
4. After the last item, one **Update Records** saves the collection

---

## Hands-On: Try It in Your Own Org

1. Create a Screen Flow with a Text variable `recordId`, available for input.
2. Add **Get Records** on Task where **WhatId** equals `{!recordId}` and **IsClosed** is False. Store **all records**.
3. Add a **Decision** with an outcome "Found tasks" where the Get Records result **Is Null** equals False.
4. Create a record collection variable `TasksToUpdate` for Task.
5. Add a **Loop** over the Get Records result. Inside it, add an **Assignment** that sets `{!Loop_Tasks.Status}` to `Completed`, then adds `{!Loop_Tasks}` to `{!TasksToUpdate}`.
6. After the last item, add **Update Records** using `{!TasksToUpdate}`, and a closing screen.
7. Run **Debug** on an Account with open Tasks and check the Tasks are completed.

---

## Quick Cheat Sheet

- **Pick a path** = Decision
- **Order** = Top to bottom, first match
- **No match** = Default outcome
- **One at a time** = Loop
- **Save once** = After Last Item
- **Never in a loop** = Records elements

## Key Takeaways

- A Decision takes the first matching outcome.
- A Loop works on one record at a time.
- Collect changes in a collection inside the loop.
- Save once after the last item.

**Next up:** Flow resources: variables, constants and formulas.

*Part of #120DaysOfSalesforce. Which do you use more, Decisions or Loops? Tell me below.*
