---
title: "Salesforce Roles & Role Hierarchy Cheat Sheet: Record Access, Profiles and Admin Interview Q&A (Day 20/30)"
date: 2026-10-26T14:38:08+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-roles-role-hierarchy-cheat-sheet-record-access-profiles-and-admin-interview-q-a-day-20-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/40f9df12-ed9f-4d3d-903f-aab2b1153d8b.png
tags: ["Salesforce", "Salesforce Admin", "Security"]
brief: "Access flows up the org chart. Roles open doors for managers, they never close them. Roles and the role hierarchy come up in almost every admin interview…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-roles-role-hierarchy-cheat-sheet-record-access-profiles-and-admin-interview-q-a-day-20-30). This is an automated backup; read and comment on the blog.

*Access flows up the org chart. Roles open doors for managers, they never close them. Roles and the role hierarchy come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Hierarchy** | Top down visibility | Managers see below |
| **Roles** | Jobs in the org chart | One per user |
| **Grant Access** | Using Hierarchies setting | On for standard objects |
| **Vs Profiles** | Roles = records | Profiles = permissions |

---

## Interview Q&A

### 1. What is a role hierarchy?

A **structure that gives managers access to records owned by people below them**.

> **Tip:** Access flows up, never down.

### 2. Role vs profile?

**Roles control record access.** Profiles control object and field permissions.

> **Tip:** Data versus permissions.

### 3. Does a role restrict access?

**No.** It only opens access above a Private default, it never reduces it.

> **Tip:** OWD sets the floor.

### 4. What is Grant Access Using Hierarchies?

A **per object setting** that lets higher roles see lower roles' records.

> **Tip:** Always on for standard objects.

### 5. Can a user have many roles?

**No.** One role per user, but one role can hold many users.

> **Tip:** One role each.

### 6. What if you delete a role?

You must **reassign its users and child roles** to another role first.

> **Tip:** Plan before deleting.

---

## Scenario Question

**"A manager cannot see her team's accounts. Why?"**

1. **Check** the default access is Private
2. **Place** her role above the team
3. **Confirm** hierarchy access is on
4. **Verify** who owns the records

---

## Quick Cheat Sheet

- **Role** = record access
- **Hierarchy** = flows up
- **Profile** = permissions
- **OWD** = the floor
- **Branch** = a region
- **One role** = per user

## Key Takeaways

- Roles open access, never close it
- Mirror the org chart, keep it simple
- Cross branch? Use sharing rules
- Few levels run faster

---

**How deep is your role hierarchy? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 20 done, 10 to go.*
