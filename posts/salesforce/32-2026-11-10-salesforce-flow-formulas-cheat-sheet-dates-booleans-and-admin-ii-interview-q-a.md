---
title: "Salesforce Flow Formulas Cheat Sheet: Dates, Booleans and Admin II Interview Q&A"
date: 2026-11-10T18:51:10+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-formulas-cheat-sheet-dates-booleans-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/8591c7ed-e97f-4cb9-bfef-3ca046bd8a76.png
tags: ["Salesforce", "flow", "120daysofsalesforce", "Salesforce Admin"]
brief: "A Flow formula calculates a value from your data and variables, so you can skip extra Decision and Assignment elements. Admin II interviews ask about them…"
series: "Salesforce"
serial: 32
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-formulas-cheat-sheet-dates-booleans-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*A Flow formula calculates a value from your data and variables, so you can skip extra Decision and Assignment elements. Admin II interviews ask about them because formulas keep Flows small, readable and easy to maintain.*

---

## Formula Basics

| Piece | What it does | Key point |
| --- | --- | --- |
| **Formula resource** | Returns one calculated value | Created under New Resource |
| **Data type** | Text, Number, Currency, Date, Date/Time or Boolean | Pick the type the formula returns |
| **Functions** | IF, AND, OR, TEXT, TODAY, BLANKVALUE and more | Same style as validation rule formulas |
| **Where you use it** | Decision conditions, Assignments, Screen text, Get Records filters | Reference it like a variable |

---

## Interview Q&A

### 1. What is a formula resource in a Flow?

A **resource** that calculates **one value** from fields, variables and functions, then returns it. Reference it anywhere you would use a variable.

> **Tip:** One formula, used in many places.

### 2. Why use a formula instead of Decision and Assignment elements?

A formula can do the same logic in **one resource**, such as a calculated date or a yes/no flag. The Flow canvas stays **short and readable**.

> **Tip:** Fewer elements, fewer places to break.

### 3. How do you handle blank values?

Use **BLANKVALUE** or **ISBLANK** (or **ISNULL** checks in conditions) so a missing field does not break the result. Empty values in math can lead to unexpected results.

> **Tip:** Always plan for blank.

### 4. Can a formula return a Boolean?

Yes. A **Boolean formula** returns true or false, which is handy as a single condition in a **Decision**, for example whether an Opportunity amount is over a limit and the stage is open.

> **Tip:** Boolean formula in, simple Decision out.

### 5. How do you use dates in a formula?

Use **TODAY()** or **NOW()** and add or subtract days, for example `TODAY() + 7` for a follow-up date. Pick **Date** or **Date/Time** to match the field you set.

> **Tip:** Match the formula type to the field type.

### 6. Where are the limits?

A formula returns **one value**, it cannot change records, and it **cannot query other records** directly. Use Get Records for data, then use the formula to work with it.

> **Tip:** Get Records finds, formulas calculate.

---

## Scenario Question

**"Create a follow-up Task due in 7 days, or 2 days if the Opportunity is over 100,000."**

1. **Record-triggered flow** on Opportunity, after save, when Stage becomes Negotiation
2. **Formula (Date):** `IF({!$Record.Amount} > 100000, TODAY() + 2, TODAY() + 7)`
3. **Create Records:** a Task with `ActivityDate` set to the formula
4. **Fault path**, then **Debug**

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** with a Number input for an amount.
2. Add a **Formula resource** of type Text that returns `IF({!Amount} > 1000, "High", "Normal")`.
3. Add a **Screen** that displays the formula result.
4. Add a second **Formula** of type Date that returns `TODAY() + 7` and show that too.
5. Run **Debug** with a few amounts and check the results.

---

## Quick Cheat Sheet

- **Formula** = one calculated value
- **Boolean formula** = single true or false condition
- **Date formula** = TODAY() plus or minus days
- **Blank safe** = BLANKVALUE or ISBLANK
- **Cannot** = change records or query data
- **Pair with** = Get Records for data

## Key Takeaways

- Use a formula to replace small Decision and Assignment chains.
- Match the formula data type to what it feeds.
- Plan for blank values.
- Get Records finds data, formulas calculate on it.

**Next up:** Flow screens and user input.

*Part of #120DaysOfSalesforce. What is the most useful Flow formula you have written? Tell me below.*
