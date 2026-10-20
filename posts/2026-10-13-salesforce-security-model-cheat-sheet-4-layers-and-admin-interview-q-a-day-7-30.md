---
title: "Salesforce Security Model Cheat Sheet: 4 Layers and Admin Interview Q&A (Day 7/30)"
date: 2026-10-13T13:33:10+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-security-model-cheat-sheet-4-layers-and-admin-interview-q-a-day-7-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/3deb4392-f75a-4e09-ab55-b0d29d266241.png
tags: ["Salesforce", "Salesforce Admin"]
brief: "Security questions come up in almost every Salesforce Admin interview. The good news: the whole model fits in one picture. Think of it as four locks on…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-security-model-cheat-sheet-4-layers-and-admin-interview-q-a-day-7-30). This is an automated backup; read and comment on the blog.

*Security questions come up in almost every Salesforce Admin interview. The good news: the whole model fits in one picture. Think of it as four locks on four doors, and every question is really asking "which lock is this?"*

This is the quick **cheat sheet** version. For the long, step-by-step walkthrough, read my earlier post: [The Salesforce Security Model Explained: OWD, Roles, Sharing Rules and More](https://sishodiarobin.hashnode.dev/the-salesforce-security-model-explained-owd-roles-sharing-rules-and-more).

---

## The Big Picture: 4 Layers of Access

| Layer | Question it answers | Tools |
| --- | --- | --- |
| **Org level** | Can this person log in at all? | Password policies, login hours, login IP ranges, MFA |
| **Object level** | Can they see or edit this *type* of data? | Profiles, Permission Sets |
| **Field level** | Can they see this *column*? | Field-Level Security (FLS) |
| **Record level** | Can they see this *row*? | OWD, Role Hierarchy, Sharing Rules, Manual Sharing |

**Golden rule:** Object and field access decide *what kind* of data you can touch. Record access decides *which rows* you can touch. You need both.

---

## Interview Q&A

### 1. What is a Profile?

A profile controls what a user can do: which objects and fields they can access, which apps and tabs they see, and system permissions. Every user has exactly **one** profile.

> **Tip:** Say "profile = baseline permissions". It sets up your next answer about permission sets.

### 2. What is a Permission Set, and how is it different from a Profile?

A permission set **adds** access on top of a profile. A user can have many permission sets, but only one profile. Permission sets can only grant access, never take it away.

> **Tip:** Mention best practice: keep profiles minimal and grant extra access through permission sets (and Permission Set Groups to bundle them).

### 3. What is OWD (Organization-Wide Defaults)?

OWD sets the **baseline record access** for each object. It is the most restrictive level in the system, and every other tool (roles, sharing rules) can only **open access up** from there.

Common settings: **Private**, **Public Read Only**, **Public Read/Write**, **Controlled by Parent**.

> **Tip:** Always say "start restrictive, then open up".

### 4. What is the Role Hierarchy?

Roles control **record visibility upward**. A manager can see the records owned by people below them in the hierarchy. Roles do **not** give object permissions; that is the profile's job.

> **Tip:** The classic trap question: *"Profile vs Role?"* Profile = what you can **do**. Role = which records you can **see**.

### 5. What are Sharing Rules?

Sharing rules open access to records for groups of users when OWD is restrictive. They can be based on **record owner** or on **record criteria** (for example, Region = West).

> **Tip:** Remember sharing rules only **extend** access. They can never restrict it.

### 6. What is Field-Level Security?

FLS controls whether a user can see or edit a specific field, set through profiles or permission sets. Hidden fields disappear from page layouts, reports and list views.

> **Tip:** A page layout alone does not secure a field. FLS does.

### 7. What is Manual Sharing?

The record owner (or a user with full access) can share an individual record with a specific user or group. It is useful for one-off exceptions.

> **Tip:** Manual sharing is lost if the record owner changes, so don't build a process around it.

### 8. If two settings conflict, which one wins?

Access in Salesforce is **additive**: the **most permissive** result wins. Two permission sources never cancel each other out.

---

## Scenario Question (Very Common!)

**"Sales reps should only see their own accounts. Managers should see their team's accounts. How do you set that up?"**

1. Set **Account OWD = Private**
2. Build the **Role Hierarchy** with managers above reps
3. Keep **Grant Access Using Hierarchies** enabled
4. If one team needs to see another team's accounts, add a **Sharing Rule**

Result: reps see their own records, managers see their whole team's, no extra code needed.

---

## Quick Cheat Sheet

- **Profile** = baseline permissions (one per user)
- **Permission Set** = extra permissions (many per user)
- **OWD** = the most restrictive baseline for records
- **Role Hierarchy** = upward record visibility
- **Sharing Rules** = open access to groups
- **FLS** = field-level visibility
- **Most permissive wins**

## Key Takeaways

- Answer in layers: org, object, field, record
- Use a real example for every answer
- Always separate "what you can do" (profile) from "what you can see" (role)
- Keep it simple, and explain *why* each tool exists

---

**Which part of the Salesforce security model confused you the most when you were learning it? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 7 done, 23 to go.*
