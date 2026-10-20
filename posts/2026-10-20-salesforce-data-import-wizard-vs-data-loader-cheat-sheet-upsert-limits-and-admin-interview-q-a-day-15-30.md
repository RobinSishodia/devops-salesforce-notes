---
title: "Salesforce Data Import Wizard vs Data Loader Cheat Sheet: Upsert, Limits and Admin Interview Q&A (Day 15/30)"
date: 2026-10-20T10:52:05+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-data-import-wizard-vs-data-loader-cheat-sheet-upsert-limits-and-admin-interview-q-a-day-15-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/99301182-eac6-4186-9c68-940321906d20.png
tags: ["Salesforce", "Salesforce Admin", "data loader"]
brief: "Two tools, one job. Pick by record volume, objects and whether you need to update or delete. This is one of the most common practical questions in a…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-data-import-wizard-vs-data-loader-cheat-sheet-upsert-limits-and-admin-interview-q-a-day-15-30). This is an automated backup; read and comment on the blog.

*Two tools, one job. Pick by record volume, objects and whether you need to update or delete. This is one of the most common practical questions in a Salesforce admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Import Wizard** | Browser tool for simple loads | Up to 50,000 records |
| **Data Loader** | Desktop app for big jobs | Up to 5 million records |
| **Upsert** | Update matches, insert the rest | Matched by External ID |
| **Export** | Back up data before a load | Export or Export All |

---

## Interview Q&A

### 1. Wizard vs Data Loader?

The Wizard is **simple and browser-based** for up to 50,000 records. Data Loader handles **far larger volumes and more objects**.

> **Tip:** Size and object decide.

### 2. What is an upsert?

It **updates records that match and inserts the rest**, matching on the record ID or an External ID field.

> **Tip:** External IDs avoid duplicates.

### 3. What can Data Loader do?

**Insert, update, upsert, delete, hard delete, export and export all**, from the app or the command line.

> **Tip:** Export All includes deleted rows.

### 4. How do you load related data?

**Load parents first**, then load children using IDs or External IDs to link them to their parents.

> **Tip:** Parents before children.

### 5. What do you check after a load?

Open the **success and error files**, fix the failed rows, and reload only those.

> **Tip:** Keep the error file.

### 6. How do you avoid a bad load?

**Test in a sandbox**, export a backup first, and check validation rules and automation that will fire.

> **Tip:** Back up before you load.

---

## Scenario Question

**"Load 200,000 contacts from a CSV without duplicates. How do you do it?"**

1. **Export** a backup of existing contacts
2. **Clean** the CSV and add an External ID
3. **Run** Data Loader with upsert
4. **Check** the success and error files

---

## Quick Cheat Sheet

- **Wizard** = up to 50,000 records
- **Loader** = up to 5 million
- **Upsert** = update or insert
- **External ID** = match key
- **Parents** = load first
- **Error file** = fix and reload

## Key Takeaways

- Clean the data before loading
- Test in a sandbox first
- Export a backup beforehand
- Keep success and error files

---

**What was your biggest data load? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 15 done, 15 to go.*
