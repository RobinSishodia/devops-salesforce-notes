---
title: "Salesforce Custom Metadata vs Custom Settings Cheat Sheet: Deploy, Hierarchy and Admin Interview Q&A (Day 22/30)"
date: 2026-10-28T13:36:46+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-custom-metadata-vs-custom-settings-cheat-sheet-deploy-hierarchy-and-admin-interview-q-a-day-22-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/453ebfe5-9b4d-48c7-b2e7-c8d676def4b1.png
tags: ["Salesforce", "Salesforce Admin", "configuration"]
brief: "Never hardcode a value. Pick the home that fits how it must travel. Custom metadata versus custom settings comes up in almost every admin interview. App…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-custom-metadata-vs-custom-settings-cheat-sheet-deploy-hierarchy-and-admin-interview-q-a-day-22-30). This is an automated backup; read and comment on the blog.

*Never hardcode a value. Pick the home that fits how it must travel. Custom metadata versus custom settings comes up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Custom Settings** | List or hierarchy type | Data stays in the org |
| **Custom Metadata** | Config stored as records | Deploys with metadata |
| **Hierarchy** | Values per user or profile | Settings only |
| **Use Cases** | Rates, flags, mappings | Not for big data |

---

## Interview Q&A

### 1. What are custom settings?

App config kept in a **cached table**, as a List or Hierarchy type.

> **Tip:** Fast to read in code.

### 2. What is custom metadata?

Custom types whose **records are metadata**, so they deploy between orgs.

> **Tip:** Records travel with deploys.

### 3. Biggest difference?

**Custom metadata records deploy.** Custom settings data does not.

> **Tip:** The interview favorite.

### 4. What is a hierarchy setting?

A setting with **values per user, profile or org default**.

> **Tip:** Only in custom settings.

### 5. Can admins use them without code?

**Yes**, in formulas, validation rules and flows.

> **Tip:** Skip hardcoding.

### 6. Which should you pick?

**Metadata for deployable config.** Settings for per user values.

> **Tip:** Default to metadata.

---

## Scenario Question

**"A tax rate differs by region and must reach prod. How?"**

1. **Create** a custom metadata type
2. **Add** one record per region
3. **Use** it in a formula or flow
4. **Deploy** with a change set

---

## Quick Cheat Sheet

- **Settings** = data stays
- **Metadata** = deploys
- **Hierarchy** = per user
- **Cache** = fast reads
- **Hardcode** = avoid
- **Default** = metadata

## Key Takeaways

- Never hardcode values
- Choose metadata when you deploy
- Choose hierarchy for per user rules
- Admins edit it without code

---

**What do you still hardcode? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 22 done, 8 to go.*
