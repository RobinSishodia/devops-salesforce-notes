---
title: "Salesforce Flow Subflows Cheat Sheet: Reusing Logic Across Flows and Admin II Interview Q&A"
date: 2026-11-21T18:23:41+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-subflows-cheat-sheet-reusing-logic-across-flows-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/af192ad7-38b3-46fd-8cca-655fe87d1cf9.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Flows can get big fast. A subflow lets you build a piece of logic once and call it from other flows. Admin II interviews ask about it often. A flow that…"
series: "Salesforce"
serial: 41
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-subflows-cheat-sheet-reusing-logic-across-flows-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Flows can get big fast. A subflow lets you build a piece of logic once and call it from other flows. Admin II interviews ask about it often.*

---

## Subflows at a Glance

| Piece | What it does | Key point |
| --- | --- | --- |
| **Subflow element** | Calls another flow from a flow | The called flow must be **active** |
| **Input variable** | Sends a value into the subflow | Tick **Available for input** |
| **Output variable** | Sends a value back | Tick **Available for output** |
| **Flow type** | Which flows can be called | Autolaunched flows and Screen Flows can be subflows |

---

## Interview Q&A

### 1. What is a subflow?

A flow that another flow calls with the **Subflow** element. The parent flow pauses at that element, the subflow runs, and then the parent carries on.

> **Tip:** Think of it like a function you can reuse.

### 2. Why use one?

To **reuse** the same logic in many flows, to keep a big flow **readable**, and to change the logic in **one** place.

> **Tip:** Name subflows clearly, for example `Sub - Create Follow-Up Task`.

### 3. How do you pass values in and out?

Create variables in the subflow and tick **Available for input** or **Available for output**. In the Subflow element you then set each input and can store each output.

> **Tip:** Pass only what the subflow needs.

### 4. Which flows can you call?

**Autolaunched flows** and **Screen Flows**. The flow you call must be **active**.

> **Tip:** Keep a version active before you call it from a parent.

### 5. How do errors behave?

If the subflow fails, the error comes back to the parent. Add a **fault path** on the Subflow element, so the parent can show a message or roll back.

> **Tip:** Fault paths work on the Subflow element too.

### 6. Do subflows share limits with the parent?

Yes. A subflow that runs in the same transaction uses the **same governor limits** as the parent flow.

> **Tip:** Do not hide a Get Records inside a loop by putting it in a subflow.

---

## Scenario Question

**"Three flows all create a follow-up Task in the same way. How do you stop copying the same elements?"**

1. Build one **Autolaunched Flow** that creates the Task
2. Add input variables for **Subject** and **Related Id**
3. Activate it
4. In each parent flow, add a **Subflow** element and set the inputs
5. Add a **fault path** on the Subflow element

---

## Hands-On: Try It in Your Own Org

1. Create an **Autolaunched Flow** named `Sub - Create Follow-Up Task`.
2. Add a text variable `TaskSubject` and tick **Available for input**.
3. Add a text variable `RelatedId` and tick **Available for input**.
4. Add **Create Records** for **Task** with Subject = `{!TaskSubject}` and WhatId = `{!RelatedId}`.
5. Save and **Activate** it.
6. Open your Screen Flow from this series and add a **Subflow** element.
7. Pick `Sub - Create Follow-Up Task` and set the two inputs.
8. Add a fault path to the Subflow element, then **Debug** and check the new Task.

---

## Quick Cheat Sheet

- **Subflow element** = call another flow
- **Called flow** = must be active
- **Input / Output** = Available for input / output
- **Fault path** = add it on the Subflow element
- **Limits** = shared with the parent in the same transaction

## Key Takeaways

- Build repeated logic once and call it as a subflow.
- Give subflows clear names and pass only what they need.
- Activate the subflow before you call it.
- Add a fault path on the Subflow element.

**Next up:** a quick recap of the Flow series so far, and what to practice for the exam.

*Part of #120DaysOfSalesforce. Do you reuse flows with subflows? Tell me below.*
