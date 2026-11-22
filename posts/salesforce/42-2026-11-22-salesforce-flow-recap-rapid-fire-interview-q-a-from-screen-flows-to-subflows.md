---
title: "Salesforce Flow Recap: Rapid-Fire Interview Q&A from Screen Flows to Subflows"
date: 2026-11-22T15:05:24+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-recap-rapid-fire-interview-q-a-from-screen-flows-to-subflows
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/339c800e-6cf8-472c-8826-33c5077fafd4.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Eight posts into the Flow series, it is time to pull it together. Here is a rapid-fire recap you can use to revise before an Admin II interview. Add a…"
series: "Salesforce"
serial: 42
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-recap-rapid-fire-interview-q-a-from-screen-flows-to-subflows). This is an automated backup; read and comment on the blog.

*Eight posts into the Flow series, it is time to pull it together. Here is a rapid-fire recap you can use to revise before an Admin II interview.*

---

## The Flow Series at a Glance

| Topic | The one thing to remember |
| --- | --- |
| **Screen Flow launch** | A Screen Flow needs a way to start: a button, a Lightning page or a utility bar |
| **Fault paths** | Add them to elements that save or delete, and show `{!$Flow.FaultMessage}` |
| **Decisions and Loops** | Decisions pick a path. Loops go through a collection one record at a time |
| **Flow resources** | Variables, collections, formulas and constants hold your data |
| **Get Records** | Query once, store the result, and check it is not empty |
| **Create and Update Records** | Use a collection and save once, never inside a loop |
| **Delete and Roll Back** | Test conditions before deleting, and roll back failed multi-step saves |
| **Subflows** | Build once, call from many flows, and activate it first |

---

## Rapid-Fire Q&A

### 1. A flow fails halfway. What do you do?

Add a **fault path** to the element that can fail, show the message, and use **Roll Back Records** if earlier saves should not stay.

> **Tip:** Fault paths on every save and delete.

### 2. Where do you keep a list of records?

In a **collection variable**. Build it with an **Assignment** inside the loop.

> **Tip:** Collect first, save after.

### 3. How do you avoid hitting limits?

Never put **Get Records**, **Create**, **Update** or **Delete** inside a loop. Use one element after the loop.

> **Tip:** One query, one save.

### 4. How do you reuse logic?

Put it in an **Autolaunched Flow** and call it with a **Subflow** element. Use **Available for input** and **Available for output** for values.

> **Tip:** Name subflows clearly.

### 5. How do you know a Get Records found nothing?

Add a **Decision** after it and check whether the record variable or collection **is empty**.

> **Tip:** Plan the empty case.

### 6. How do you test a flow?

Use **Debug** in Flow Builder. Test the happy path, the empty case and a forced failure.

> **Tip:** Test the fault path too.

---

## Scenario Question

**"A Screen Flow updates an Opportunity and creates a Task. How do you make it safe and tidy?"**

1. Keep the Create and Update together, with no screen between them
2. Add a **fault path** to the Update
3. Add **Roll Back Records** on the fault path
4. Move repeated Task logic into a **subflow**
5. Show the fault message to the user

---

## Hands-On: Try It in Your Own Org

1. Open your Screen Flow from this series.
2. Check that every Create, Update and Delete element has a **fault path**.
3. Check that no **Get Records** or save element sits inside a loop.
4. Move any repeated elements into a **subflow** and activate it.
5. Run **Debug** with an empty result and with a forced failure.
6. Write down one thing you would explain differently in an interview.

---

## Quick Cheat Sheet

- **Start a Screen Flow** = button, page or utility bar
- **Errors** = fault paths plus Roll Back Records
- **Lists** = collections, saved once
- **Reuse** = subflows
- **Empty result** = check with a Decision
- **Test** = Debug, including failures

## Key Takeaways

- Plan for errors and empty results in every flow.
- Never query or save inside a loop.
- Reuse logic with subflows.
- Test the failure paths, not only the happy path.

**Next up:** a new topic in the Admin II series. Tell me what you would like to see.

*Part of #120DaysOfSalesforce. Which Flow topic do you find hardest? Tell me below.*
