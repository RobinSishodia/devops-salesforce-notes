---
title: "Salesforce Approval Processes Cheat Sheet: Entry Criteria, Approvers and Admin Interview Q&A (Day 12/30)"
date: 2026-10-17T13:55:45+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-approval-processes-cheat-sheet-entry-criteria-approvers-and-admin-interview-q-a-day-12-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/ffa00b3a-6821-43d9-91bf-e3b9a1a89d05.png
tags: ["Salesforce", "Salesforce Admin", "Approval Process"]
brief: "Some changes need a second pair of eyes. Approval processes route a record to the right person before it moves on, and they come up in almost every admin…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-approval-processes-cheat-sheet-entry-criteria-approvers-and-admin-interview-q-a-day-12-30). This is an automated backup; read and comment on the blog.

*Some changes need a second pair of eyes. Approval processes route a record to the right person before it moves on, and they come up in almost every admin interview that touches automation.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Entry Criteria** | Decides which records can be submitted | Records that miss them cannot be submitted |
| **Approval Step** | Who reviews the record | User, queue, manager or field |
| **Actions** | Run on submit, approve or reject | Field update, email, task |
| **Record Lock** | Record is read-only while pending | Admins can still edit |

---

## Interview Q&A

### 1. What is an Approval Process?

It automates how a record gets approved: **submit, route to approvers, then approve or reject**, with actions at each stage.

> **Tip:** Think of it as a manager sign-off.

### 2. What are entry criteria?

Conditions a record must meet before it can be submitted, like **Discount over 20 percent**.

> **Tip:** Records that miss them cannot be submitted.

### 3. Who can be an approver?

A **user**, a **queue**, the submitter's **manager**, or a user picked from a **field** on the record.

> **Tip:** Queues let a team share the work.

### 4. What actions can run?

**Field updates, email alerts, tasks and outbound messages**, on submit, final approval, final rejection or recall.

> **Tip:** Use a field update to set Status.

### 5. What does the record lock do?

A pending record is **locked** so users cannot edit it. Admins can still edit, and a **recall** unlocks it.

> **Tip:** The lock stops edits while review is open.

### 6. Approval Process vs Flow?

Approval Processes handle classic sign-off. **Flow Orchestrator** is the newer option for complex, multi-step approvals.

> **Tip:** Name the trade-off, then pick.

---

## Scenario Question

**"Discounts over 20 percent need manager approval before the deal moves on. How do you do it?"**

1. **Entry criteria:** Discount greater than 20 percent
2. **Approver:** the submitter's manager
3. **On submit:** a field update sets Status to Pending
4. **On approval:** Status becomes Approved

---

## Quick Cheat Sheet

- **Entry** = who may submit
- **Approver** = user, queue, manager
- **Actions** = update, email, task
- **Lock** = read-only while pending
- **Recall** = pulls it back
- **Orchestrator** = newer option

## Key Takeaways

- Define entry criteria first
- Prefer queues or managers over named users
- Track status with field updates
- Test with a real submitter

---

**What would you send for approval first? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 12 done, 18 to go.*
