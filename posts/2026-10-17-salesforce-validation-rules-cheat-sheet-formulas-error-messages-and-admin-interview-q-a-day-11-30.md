---
title: "Salesforce Validation Rules Cheat Sheet: Formulas, Error Messages and Admin Interview Q&A (Day 11/30)"
date: 2026-10-17T12:36:37+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-validation-rules-cheat-sheet-formulas-error-messages-and-admin-interview-q-a-day-11-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/10a66ceb-f74e-4c80-a624-63fc435d2002.png
tags: ["Salesforce", "Salesforce Admin", "validation-rules"]
brief: "Clean data starts at the door. Validation rules decide what Salesforce lets in, and what it turns away. They are one of the most asked-about admin topics because every real org depends on them. The 4"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-validation-rules-cheat-sheet-formulas-error-messages-and-admin-interview-q-a-day-11-30). This is an automated backup; read and comment on the blog.

*Clean data starts at the door. Validation rules decide what Salesforce lets in, and what it turns away. They are one of the most asked-about admin topics because every real org depends on them.*

---

## The 4 Data Quality Tools

| Tool | What it is | Key point |
| --- | --- | --- |
| **Validation Rule** | Blocks a save if the formula is TRUE | Shows your error message |
| **Formula Field** | A read-only calculated value | Recalculates automatically |
| **Required Field** | Must have a value to save | Set on the field or the layout |
| **Duplicate Rule** | Warns or blocks likely duplicates | Works with Matching Rules |

---

## Interview Q&A

### 1. What is a Validation Rule?

A formula that returns **TRUE when data is bad**. If it is TRUE, Salesforce blocks the save and shows your error message.

> **Tip:** TRUE means error, FALSE means save.

### 2. Where does the error show?

You choose: **at the top of the page**, or **next to a specific field** on the record page.

> **Tip:** Show it by the field the user must fix.

### 3. Required field vs Validation Rule?

A field-level required setting always applies, even through the API. A **validation rule** can add conditions, like required only at a certain stage.

> **Tip:** Needed only sometimes? Use a rule.

### 4. Formula field vs Validation Rule?

A **formula field** returns a value users cannot edit. A **validation rule** formula returns TRUE or FALSE to allow or block a save.

> **Tip:** Formula fields are read-only.

### 5. Which functions come up most?

`ISBLANK` for empty checks, `ISPICKVAL` for picklists, `AND` and `OR` to combine tests, `ISCHANGED` on updates, and `REGEX` for patterns.

> **Tip:** Never compare a picklist with `=`.

### 6. Do rules run on imports and Flows?

Yes. They also run for the API, Apex and Flow. To skip them for admins or data loads, check a **custom permission** in the formula.

> **Tip:** Avoid hardcoding profile names.

---

## Scenario Question

**"Reps must not mark an Opportunity Closed Won without an Amount. How do you enforce it?"**

1. Go to **Object Manager, Opportunity, Validation Rules**
2. Write the formula with **ISPICKVAL** and **ISBLANK**
3. Add a clear **error message** on the Amount field
4. **Test in a sandbox**, then activate

The formula looks like this:

```
AND(
  ISPICKVAL(StageName, "Closed Won"),
  ISBLANK(Amount)
)
```

---

## Quick Cheat Sheet

- **TRUE** = block the save
- **ISBLANK** = empty check
- **ISPICKVAL** = picklist check
- **ISCHANGED** = on updates
- **Formula field** = read-only
- **Bypass** = custom permission

## Key Takeaways

- Write the rule so TRUE means bad data
- Keep error messages specific
- Required field for always, rule for sometimes
- Add a bypass for data loads

---

**What is the best validation rule you have written? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 11 done, 19 to go.*
