---
title: "Salesforce Permission Sets & Groups Cheat Sheet: Profiles, Muting and Admin Interview Q&A (Day 14/30)"
date: 2026-10-19T08:21:14+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-permission-sets-groups-cheat-sheet-profiles-muting-and-admin-interview-q-a-day-14-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/ca65621a-a9c9-4d5f-b797-87005f208713.png
tags: ["Salesforce", "Salesforce Admin", "Permission Sets"]
brief: "One profile, many permission sets. Start with minimum access, then add only what each person needs. It is the access-control answer interviewers expect from a modern admin. The 4 Building Blocks B"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-permission-sets-groups-cheat-sheet-profiles-muting-and-admin-interview-q-a-day-14-30). This is an automated backup; read and comment on the blog.

*One profile, many permission sets. Start with minimum access, then add only what each person needs. It is the access-control answer interviewers expect from a modern admin.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Permission Set** | Adds access on top of a profile | Grants only, never removes |
| **Set Group** | Bundles sets for a job role | Assign one group per role |
| **Muting Set** | Switches off a permission in a group | Other uses stay unchanged |
| **Assignment** | Many sets per user | One profile per user |

---

## Interview Q&A

### 1. Profile vs Permission Set?

A user has **one profile** as the baseline, and **any number of permission sets** that add extra access.

> **Tip:** One profile, many sets.

### 2. Why prefer permission sets?

They follow **least privilege**: keep profiles minimal and grant extras only to the people who need them.

> **Tip:** Fewer profiles, easier upkeep.

### 3. What is a Permission Set Group?

It **bundles several permission sets** into one unit you assign, usually matching a job role.

> **Tip:** Assign one group per role.

### 4. What is a Muting Permission Set?

It lives **inside a group** and turns off chosen permissions from that group's sets, without editing the sets.

> **Tip:** Mute, do not clone.

### 5. Can a permission set remove access?

A normal set **only grants**. To take access away, use a muting set or change the profile.

> **Tip:** Access is additive.

### 6. What stays on the profile?

**Login hours, login IP ranges, default record types and page layout assignments** still live on the profile.

> **Tip:** Name login hours and IP ranges.

---

## Scenario Question

**"Only 10 of 100 reps may export reports. How do you do it?"**

1. **Keep** one shared profile for all reps
2. **Create** a permission set with Export Reports
3. **Assign** it to the 10 users
4. **Bundle** into a group if roles grow

---

## Quick Cheat Sheet

- **Profile** = baseline, one per user
- **Set** = extra access, many per user
- **Group** = bundle for a role
- **Muting** = off inside a group
- **Additive** = sets only grant
- **Profile-only** = login hours, IPs

## Key Takeaways

- Keep profiles minimal
- Grant extra access with sets
- Group sets by job role
- Document what each set is for

---

**Which access would you move to a set first? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 14 done, 16 to go.*
