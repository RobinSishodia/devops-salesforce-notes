---
title: "Salesforce Reports & Dashboards Cheat Sheet: Formats, Running User and Admin Interview Q&A (Day 10/30)"
date: 2026-10-15T19:34:56+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-reports-dashboards-cheat-sheet-formats-running-user-and-admin-interview-q-a-day-10-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/1fb51ec5-3bd6-4a7e-8d49-266df22d7b91.png
tags: ["Salesforce", "Salesforce Admin", "Reports  Dashboards"]
brief: "Reports answer the question, dashboards show the answer. Interviewers love this topic because it tests whether you can turn raw data into something a…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-reports-dashboards-cheat-sheet-formats-running-user-and-admin-interview-q-a-day-10-30). This is an automated backup; read and comment on the blog.

*Reports answer the question, dashboards show the answer. Interviewers love this topic because it tests whether you can turn raw data into something a manager can act on.*

---

## The 4 Report Formats

| Format | What it is | Key point |
| --- | --- | --- |
| **Tabular** | A simple list of records | No grouping, no dashboard charts |
| **Summary** | Rows grouped by a field | Up to 3 groupings, subtotals |
| **Matrix** | Grouped by rows and columns | Up to 2 row and 2 column groups |
| **Joined** | Blocks from different report types | Up to 5 blocks in one report |

---

## Interview Q&A

### 1. What is a Report Type?

It decides which objects and fields a report can use. Standard report types exist, and you can build **custom report types** with related objects.

> **Tip:** "With" shows parents that have children, "with or without" shows all parents.

### 2. Summary vs Matrix report?

A **Summary** report groups rows by up to 3 fields. A **Matrix** report groups by both rows and columns, so you can compare two dimensions at once.

> **Tip:** Need a cross-tab like region by quarter? Use a matrix.

### 3. Report vs Dashboard?

A **report** lists filtered records. A **dashboard** shows up to 20 components, each built from a source report.

> **Tip:** Every component needs a source report.

### 4. Running user vs dynamic dashboard?

A normal dashboard shows data as seen by its **running user**. A **dynamic dashboard** runs as whoever is viewing it.

> **Tip:** Use dynamic when each viewer should see only their own data.

### 5. What is a Bucket field?

It groups report values into categories you define, with **no formula or custom field** needed.

> **Tip:** For example, group deal amounts into Small, Medium and Large.

### 6. What is a Cross filter?

It filters records by related records, like **Accounts with or without Opportunities**.

> **Tip:** Great for finding accounts with no activity.

---

## Scenario Question

**"A sales manager wants open pipeline by stage as a dashboard, emailed weekly. How do you do it?"**

1. Build a **Summary report** on Opportunities, open only
2. **Group** the report by Stage and add a chart
3. Add it to a **dashboard** as a component
4. **Subscribe** the manager for a weekly email

---

## Quick Cheat Sheet

- **Tabular** = simple list
- **Summary** = up to 3 groupings
- **Matrix** = rows and columns
- **Joined** = up to 5 blocks
- **Dashboard** = up to 20 components
- **Bucket** = group without a formula

## Key Takeaways

- Choose the report type first
- Summary to group, matrix to compare
- Dashboards display reports
- Check the running user

---

**Summary or Matrix: which do you build most? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 10 done, 20 to go.*
