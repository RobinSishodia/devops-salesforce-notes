---
title: "Salesforce Email-to-Case Cheat Sheet: On-Demand, Routing Addresses, and Admin Interview Q&A (Day 25/30)"
date: 2026-10-31T15:07:06+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-email-to-case-cheat-sheet-on-demand-routing-addresses-and-admin-interview-q-a-day-25-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/b369f436-93b4-418c-853c-984030ed288a.png
tags: ["Salesforce", "crm", "interview questions"]
brief: "Every support email, tracked as a case from the first message. Email-to-Case comes up in almost every Service Cloud and admin interview. Customer emails…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-email-to-case-cheat-sheet-on-demand-routing-addresses-and-admin-interview-q-a-day-25-30). This is an automated backup; read and comment on the blog.

*Every support email, tracked as a case from the first message. Email-to-Case comes up in almost every Service Cloud and admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Routing Address** | Address makes cases | Verify it first |
| **On-Demand** | Salesforce hosts it | No agent needed |
| **Standard** | Agent on your server | Behind firewall |
| **Threading** | Ref ID links replies | One case thread |

---

## Interview Q&A

### 1. What is Email-to-Case?

Customer emails **automatically become cases** in Salesforce.

> **Tip:** No manual typing.

### 2. On-Demand or Standard?

**On-Demand needs no agent.** Standard runs an agent behind your firewall.

> **Tip:** Default to On-Demand.

### 3. What is a routing address?

It links an email address to **case settings** like origin and priority.

> **Tip:** Verify it before use.

### 4. How do replies stay on one case?

A **Ref ID** in the email ties each reply to the same case.

> **Tip:** Keep it in the subject.

### 5. How do cases get an owner?

**Assignment rules** route them, or the routing address owner takes them.

> **Tip:** Queues work well.

### 6. Can customers get a reply?

**Yes**, auto-response rules confirm the case by email.

> **Tip:** Include the case number.

---

## Scenario Question

**"Support inbox emails must become cases. How?"**

1. **Enable** Email-to-Case in Setup
2. **Create** and verify a routing address
3. **Set** assignment and auto-response
4. **Test** by emailing the inbox

---

## Quick Cheat Sheet

- **Email** = becomes a case
- **Default** = On-Demand
- **Agent** = Standard only
- **Address** = verify first
- **Thread** = Ref ID
- **Reply** = auto-response

## Key Takeaways

- Pick On-Demand unless a firewall blocks it
- Verify every routing address
- Keep the Ref ID for threading
- Test with a real email

---

**Which inbox do you run? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 25 done, 5 to go.*
