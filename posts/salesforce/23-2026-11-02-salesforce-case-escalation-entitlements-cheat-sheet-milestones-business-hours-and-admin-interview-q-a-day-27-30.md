---
title: "Salesforce Case Escalation & Entitlements Cheat Sheet: Milestones, Business Hours, and Admin Interview Q&A (Day 27/30)"
date: 2026-11-02T14:35:57+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-case-escalation-entitlements-cheat-sheet-milestones-business-hours-and-admin-interview-q-a-day-27-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/59358d6f-5056-45ec-8bdd-8205bbd34736.png
tags: ["Salesforce", "crm", "interview questions"]
brief: "Make sure no customer waits longer than promised. Escalation rules and entitlements come up in almost every Service Cloud admin interview. It reassigns or…"
series: "Salesforce Admin 30-Day Series"
serial: 23
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-case-escalation-entitlements-cheat-sheet-milestones-business-hours-and-admin-interview-q-a-day-27-30). This is an automated backup; read and comment on the blog.

*Make sure no customer waits longer than promised. Escalation rules and entitlements come up in almost every Service Cloud admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Escalation** | Acts on open cases | One active rule |
| **Business Hours** | Working time clock | Set them first |
| **Entitlement** | Support level owed | Link to account |
| **Milestone** | Timed required step | Warn and violate |

---

## Interview Q&A

### 1. What is an escalation rule?

It **reassigns or notifies** when a case stays open too long.

> **Tip:** Built for missed deadlines.

### 2. Assignment or escalation?

**Assignment routes new cases.** Escalation acts on open ones.

> **Tip:** They work together.

### 3. How many can be active?

Only **one escalation rule** is active at a time.

> **Tip:** Use rule entries for variety.

### 4. Why set business hours?

Timers can count **only working hours**.

> **Tip:** Add holidays too.

### 5. What is an entitlement?

It defines the **support a customer is owed**, like response time.

> **Tip:** Link it to the account.

### 6. What is a milestone?

A **required step with a time limit**, such as first response.

> **Tip:** Add warning and violation actions.

---

## Scenario Question

**"Premium cases need a reply within an hour. How?"**

1. **Create** a Premium entitlement
2. **Add** a first response milestone
3. **Set** warning and violation actions
4. **Test** with a sample case

---

## Quick Cheat Sheet

- **Assign** = routes new cases
- **Escalate** = acts on open cases
- **Active** = one rule
- **Clock** = business hours
- **Entitlement** = support level
- **Milestone** = time target

## Key Takeaways

- Assign first, escalate later
- Set business hours before timers
- Link entitlements to accounts
- Warn before the violation

---

**What is your case SLA? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 27 done, 3 to go.*
