---
title: "Salesforce Flow Cheat Sheet: Types, Triggers and Admin Interview Q&A (Day 8/30)"
date: 2026-10-13T22:00:06+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-cheat-sheet-types-triggers-and-admin-interview-q-a-day-8-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/eb5a0a21-2efe-429d-a1da-6e43dd949dff.png
tags: ["Salesforce", "Salesforce Admin", "flow"]
brief: "Flow is now the one automation tool every Salesforce Admin is expected to know. Interviewers usually ask the same few things: which type, which trigger…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-cheat-sheet-types-triggers-and-admin-interview-q-a-day-8-30). This is an automated backup; read and comment on the blog.

*Flow is now the one automation tool every Salesforce Admin is expected to know. Interviewers usually ask the same few things: which type, which trigger timing, and how you keep it safe at scale.*

---

## The 4 Flow Types

| Type | Use it when | Examples |
| --- | --- | --- |
| **Screen Flow** | A user needs to click and type | Guided forms, wizards, Lightning pages |
| **Record-Triggered Flow** | A record is created, updated or deleted | Update a field, create a task |
| **Scheduled-Triggered Flow** | Something must run at a set time | Daily or weekly batch jobs |
| **Autolaunched Flow** | Another process calls it | Called from flows, Apex, buttons |

---

## Interview Q&A

### 1. What is a Record-Triggered Flow?

It runs automatically when a record is created, updated or deleted. Entry conditions decide when it actually fires.

> **Tip:** Add entry conditions so it only runs when needed.

### 2. Before-save vs After-save?

**Before-save** updates the same record that triggered the flow, fast, with no extra DML. **After-save** handles related records, emails and other actions.

> **Tip:** Same record = before. Anything else = after.

### 3. Flow vs Workflow Rules and Process Builder?

Workflow Rules and Process Builder are retired, with support ending on Dec 31, 2025. Flow is the single automation tool going forward.

> **Tip:** Say you would migrate old automation to Flow.

### 4. Flow or Apex?

Start with clicks, not code. Use Apex when logic is very complex, needs heavy bulk processing, or Flow cannot do it.

> **Tip:** "Declarative first" is the safe answer.

### 5. What are the data elements?

Get, Create, Update and Delete Records. Get Records reads data into variables you can reuse.

> **Tip:** One well-filtered Get Records beats many.

### 6. Why never put DML in a loop?

Governor limits cap queries and DML per transaction. Collect records in a collection variable, then do **one** DML after the loop.

> **Tip:** Add a Fault path and test with Debug.

---

## Scenario Question

**"When an Opportunity becomes Closed Won, create a follow-up Task and update the Account. How?"**

1. Build a **Record-Triggered Flow** on Opportunity, run **after save**
2. Entry condition: **Stage = Closed Won** and Stage **is changed**
3. **Create Records**: a Task for the Account owner
4. **Update Records**: the Account, add a **Fault path**, then test with **Debug**

---

## Quick Cheat Sheet

- **Screen** = user input
- **Record-Triggered** = on create, update, delete
- **Scheduled** = runs at a set time
- **Autolaunched** = called by others
- **Before-save** = fast, same record
- **No DML in loops**

## Key Takeaways

- Flow first, Apex only when needed
- Choose before-save or after-save on purpose
- Use entry conditions to limit runs
- Always add Fault paths and test with Debug

---

**Which Flow type do you use most? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 8 done, 22 to go.*
