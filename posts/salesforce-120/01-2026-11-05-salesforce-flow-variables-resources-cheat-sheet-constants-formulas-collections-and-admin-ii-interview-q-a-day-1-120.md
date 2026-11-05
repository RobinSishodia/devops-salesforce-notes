---
title: "Salesforce Flow Variables & Resources Cheat Sheet: Constants, Formulas, Collections and Admin II Interview Q&A (Day 1/120)"
date: 2026-11-05T07:37:28+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-variables-resources-cheat-sheet-constants-formulas-collections-and-admin-ii-interview-q-a-day-1-120
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/6788cbb5-1103-471a-9597-f56d51c75604.png
tags: ["Salesforce", "Salesforce Admin", "flow"]
brief: "Variables, constants, formulas and collections are the building blocks of every Flow. Admin II interviews ask about them to see if you can build, not just…"
series: "120 Days of Salesforce"
serial: 1
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-variables-resources-cheat-sheet-constants-formulas-collections-and-admin-ii-interview-q-a-day-1-120). This is an automated backup; read and comment on the blog.

*Variables, constants, formulas and collections are the building blocks of every Flow. Admin II interviews ask about them to see if you can build, not just click.*

---

## The 4 Building Blocks

| Resource | What it holds | Key point |
| --- | --- | --- |
| **Variable** | A value | Changes via Assignment |
| **Constant** | A fixed value | Never changes |
| **Formula** | A calculated value | Read-only, calculated live |
| **Collection** | A list of values or records | Allow multiple values |

---

## Interview Q&A

### 1. Variable, Constant or Formula?

**Variables change through Assignment.** Constants never change. Formulas calculate when they are used.

> **Tip:** Need to change it? Use a variable.

### 2. What is a record variable?

One variable that **holds a whole record**. Read its fields as `{!recVar.Field}`.

> **Tip:** Fill it with Get Records.

### 3. What is a collection variable?

A variable with **Allow multiple values** turned on. It holds a list you can loop over.

> **Tip:** Name it plural, like `contactList`.

### 4. What do the input and output settings do?

**Input lets a caller pass values in** (a subflow, Apex or a URL). **Output returns values** to the caller.

> **Tip:** Open only what you need.

### 5. What is $Record?

The **record that triggered** a record-triggered flow. `$Record__Prior` holds the old values on updates.

> **Tip:** Compare old to new.

### 6. Text Template or Formula?

**Text Template builds readable text** with merge fields. A Formula returns a calculated value.

> **Tip:** Emails and screen messages: use a template.

---

## Scenario Question

**"A screen flow must show a 10% discount on an Opportunity."**

1. **Get Records** into an Opportunity variable
2. **Formula:** Amount x 0.1
3. **Text Template:** build the message
4. **Show** it on a screen, then **Debug**

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** and add a **Get Records** element for one Opportunity into a record variable.
2. Add a **Formula** resource of type Currency: `{!oppRecord.Amount} * 0.1`.
3. Add a **Text Template** that says "Discount: {!discountFormula}".
4. Show the template in a **Display Text** component on a screen.
5. Run **Debug** and check the value against the Opportunity amount.

---

## Quick Cheat Sheet

- **Change** = variable
- **Fixed** = constant
- **Calculate** = formula
- **Message** = text template
- **List** = collection
- **Trigger record** = $Record

## Key Takeaways

- Pick the right resource type.
- Use a Formula for any calculation.
- Open input and output with care.
- Name every resource clearly.

**Next up, Day 2:** Decision and Assignment elements.

*Part of #120DaysOfSalesforce. Which resource do you use most? Tell me below.*
