---
title: "Salesforce Duplicate & Matching Rules Cheat Sheet: Block, Alert, Merge and Admin Interview Q&A (Day 18/30)"
date: 2026-10-23T18:15:36+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-duplicate-matching-rules-cheat-sheet-block-alert-merge-and-admin-interview-q-a-day-18-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/65a26b2e-a26e-46d8-9e76-1867c19e08b4.png
tags: ["Salesforce", "Salesforce Admin", "data-quality"]
brief: "Stop messy duplicates before they land, and clean up the ones already in your data. Duplicate and matching rules are core data quality topics in any admin…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-duplicate-matching-rules-cheat-sheet-block-alert-merge-and-admin-interview-q-a-day-18-30). This is an automated backup; read and comment on the blog.

*Stop messy duplicates before they land, and clean up the ones already in your data. Duplicate and matching rules are core data quality topics in any admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Matching Rule** | Defines what is a match | Compares chosen fields |
| **Duplicate Rule** | Acts on a match | Block or alert |
| **Merge** | Combine up to 3 records | Keeps one master |
| **Report** | Lists found duplicates | Review and clean |

---

## Interview Q&A

### 1. What is a matching rule?

It **defines which fields to compare** and how closely records must match.

> **Tip:** Fuzzy or exact, field by field.

### 2. What is a duplicate rule?

It **decides what happens on a match**: block the save or allow it with an alert.

> **Tip:** Matching finds, the rule acts.

### 3. Are there standard rules?

Salesforce ships **standard rules for accounts, contacts and leads**.

> **Tip:** Activate them before customising.

### 4. Block or alert?

**Block** stops the save. **Alert** warns, then lets the user continue.

> **Tip:** Start with alert, then tighten.

### 5. How do you merge?

Combine **up to three records into one master**, choosing which values to keep.

> **Tip:** Check related records first.

### 6. What are the limits?

Rules **check new saves**, so existing duplicates need a separate clean up.

> **Tip:** Clean first, then prevent.

---

## Scenario Question

**"Stop duplicate leads being created. How?"**

1. **Activate** the standard lead matching rule
2. **Create** a duplicate rule on Lead
3. **Set** the action to alert first
4. **Test**, then merge old duplicates

---

## Quick Cheat Sheet

- **Matching** = finds matches
- **Duplicate rule** = acts
- **Block** = stops the save
- **Alert** = warns the user
- **Merge** = up to 3 records
- **Report** = lists duplicates

## Key Takeaways

- Prevent and clean, do both
- Start with alert, not block
- Test with real data
- Merge carefully, there is no undo

---

**What is the messiest duplicate you have seen? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 18 done, 12 to go.*
