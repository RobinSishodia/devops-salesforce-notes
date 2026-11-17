---
title: "Salesforce Flow Resources Cheat Sheet: Variables, Constants, Formulas and Admin II Interview Q&A"
date: 2026-11-17T16:04:52+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-resources-cheat-sheet-variables-constants-formulas-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/86b4b87d-b84d-4da4-a1df-2c410720757e.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Every flow needs places to keep and calculate values. Admin II interviews ask which resource to use and why: a variable, a constant, a formula or a text…"
series: "Salesforce"
serial: 37
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-resources-cheat-sheet-variables-constants-formulas-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Every flow needs places to keep and calculate values. Admin II interviews ask which resource to use and why: a variable, a constant, a formula or a text template.*

---

## The Four Resources at a Glance

| Resource | What it holds | Key point |
| --- | --- | --- |
| **Variable** | A value that can change while the flow runs | Single value, record or collection |
| **Constant** | A fixed value | Cannot be changed by the flow |
| **Formula** | A calculated value | Read-only, recalculated each time you use it |
| **Text template** | Formatted text with merge fields | Good for messages and email bodies |

---

## Interview Q&A

### 1. What is a variable?

A named container for a value. Choose its **data type** (Text, Number, Currency, Boolean, Date, Date/Time or Record) and whether it holds **one value or a collection**.

> **Tip:** Name it for what it holds, such as `TasksToUpdate`.

### 2. What do "Available for input" and "Available for output" mean?

**Input** lets a value be passed into the flow, for example `recordId` from a record page. **Output** lets a value be passed out to a parent flow or another caller.

> **Tip:** Tick only what you need.

### 3. When do you use a constant?

When a value never changes during the flow, such as a default Task subject. Change it in one place instead of searching every element.

> **Tip:** A constant cannot be updated by an Assignment.

### 4. What is a formula resource?

A value calculated from other values, such as a due date of today plus 7 days. It is **read-only** and works out the answer each time the flow uses it.

> **Tip:** Pick the formula's data type to match where you will use it.

### 5. When do you use a text template?

When you need a longer message that mixes text and merge fields, such as a confirmation screen or an email body.

> **Tip:** Use rich text for formatting, plain text for simple messages.

### 6. How do you refer to a resource?

Wrap its name in curly brackets with an exclamation mark, such as `{!recordId}`. Global values work the same way, for example `{!$Flow.CurrentDate}` and `{!$User.Id}`.

> **Tip:** The resource picker avoids typing mistakes.

---

## Scenario Question

**"Create a follow-up Task due 7 days from today, with the same subject every time."**

1. Create a **constant** `Default_Subject` with the value Follow up call
2. Create a **formula** `DueDate` of type Date: `{!$Flow.CurrentDate} + 7`
3. Use both in the **Create Records** element for the Task
4. Show a **text template** on the confirmation screen

---

## Hands-On: Try It in Your Own Org

1. Open your Screen Flow from this series in Flow Builder.
2. Choose **New Resource**, then **Constant**. Name it `Default_Subject`, type **Text**, value `Follow up call`.
3. Add a **Formula** named `DueDate`, data type **Date**, with `{!$Flow.CurrentDate} + 7`.
4. In the **Create Records** element for the Task, set **Subject** to `{!Default_Subject}` and **ActivityDate** to `{!DueDate}`.
5. Add a **Text Template** named `ConfirmMessage`: `Follow-up created for {!DueDate}.`
6. Show `{!ConfirmMessage}` on the last screen, then **Debug** and check the Task.

---

## Quick Cheat Sheet

- **Changes at runtime** = Variable
- **Never changes** = Constant
- **Calculated, read-only** = Formula
- **Message with merge fields** = Text template
- **Today's date** = `{!$Flow.CurrentDate}`
- **Refer to anything** = `{!Name}`

## Key Takeaways

- Use a variable when the value changes, a constant when it does not.
- A formula calculates and cannot be assigned to.
- A text template builds readable messages.
- Clear names make flows easy to maintain.

**Next up:** the Get Records element: filters, sort order and how many records to store.

*Part of #120DaysOfSalesforce. Which resource do you forget to use? Tell me below.*
