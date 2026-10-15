---
title: "Lookup vs Master-Detail: Salesforce Relationships Cheat Sheet for Admin Interviews (Day 9/30)"
date: 2026-10-15T19:08:22+00:00
canonical_url: https://sishodiarobin.hashnode.dev/lookup-vs-master-detail-salesforce-relationships-cheat-sheet-for-admin-interviews-day-9-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/d162fe54-2745-411e-8e47-8c5796d1ed23.png
tags: ["Salesforce", "Salesforce Admin"]
brief: "Relationships are the backbone of every Salesforce data model, and interviewers love them. Almost every question comes down to one idea: can the child record exist without its parent? The 4 Relations"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/lookup-vs-master-detail-salesforce-relationships-cheat-sheet-for-admin-interviews-day-9-30). This is an automated backup; read and comment on the blog.

*Relationships are the backbone of every Salesforce data model, and interviewers love them. Almost every question comes down to one idea: can the child record exist without its parent?*

---

## The 4 Relationship Types

| Type | What it is | Key point |
| --- | --- | --- |
| **Lookup** | A loose link between two objects | Optional, the child keeps its own owner |
| **Master-Detail** | A tight parent-child bond | Cascade delete, roll-ups, shared access |
| **Junction object** | Links two objects many-to-many | Two master-detail fields |
| **Hierarchical** | Records link to the same object | Parent Account, user manager |

---

## Interview Q&A

### 1. Standard vs Custom objects?

Standard objects ship with Salesforce, such as Account, Contact and Opportunity. Custom objects are built by you, and their API names end in `__c`.

> **Tip:** Custom objects and fields always end in `__c`.

### 2. Lookup vs Master-Detail?

A **Lookup** is optional and loosely coupled. A **Master-Detail** is required: the child inherits the parent's owner and sharing.

> **Tip:** Ask: can the child exist without the parent?

### 3. What is a Junction object?

A custom object with **two master-detail fields** that creates a many-to-many link, like Student to Course through Enrollment.

> **Tip:** The first master-detail sets the owner and sharing.

### 4. What is a Roll-up Summary field?

It lives on the master record and calculates **COUNT, SUM, MIN or MAX** over its detail records. It is only available with master-detail.

> **Tip:** Need it on a lookup? Use a Flow instead.

### 5. Can you convert between them?

**Lookup to Master-Detail** works only if every child record already has a parent. **Master-Detail to Lookup** works only if the parent has no roll-up summary fields.

> **Tip:** Fill in blank lookups before converting.

### 6. What happens if the parent is deleted?

With **Master-Detail** the children are deleted too (cascade). With a **Lookup** the children stay, unless you restrict the delete.

> **Tip:** Restricting delete protects child data.

---

## Scenario Question

**"A school tracks Students and Courses, and each student can take many courses. How do you model it?"**

1. Create custom objects **Student** and **Course**
2. Create a junction object called **Enrollment**
3. Add **two master-detail fields**: one to Student, one to Course
4. Add a **roll-up summary** on Course to count Enrollments

---

## Quick Cheat Sheet

- **Lookup** = optional, independent
- **Master-Detail** = required, cascade delete
- **Junction** = two master-details
- **Roll-up** = master-detail only
- **Max 2** master-detail fields per object
- **Custom** API names end in `__c`

## Key Takeaways

- Start with: can the child exist alone?
- Use master-detail for tight ownership
- Use a junction object for many-to-many
- Plan relationships before you build

---

**Lookup or Master-Detail: which do you pick first? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 9 done, 21 to go.*
