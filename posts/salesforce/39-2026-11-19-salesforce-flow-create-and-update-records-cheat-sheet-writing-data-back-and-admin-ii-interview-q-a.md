---
title: "Salesforce Flow Create and Update Records Cheat Sheet: Writing Data Back and Admin II Interview Q&A"
date: 2026-11-19T17:05:29+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-create-and-update-records-cheat-sheet-writing-data-back-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/f8e4dff5-32dc-4a61-873d-20b6dda13bc9.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Reading data is half of a flow. The other half is writing it back. Admin II interviews ask how Create Records and Update Records differ, and how to write…"
series: "Salesforce"
serial: 39
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-create-and-update-records-cheat-sheet-writing-data-back-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Reading data is half of a flow. The other half is writing it back. Admin II interviews ask how Create Records and Update Records differ, and how to write many records without hitting limits.*

---

## Create and Update at a Glance

| Element | What it does | Key point |
| --- | --- | --- |
| **Create Records** | Inserts new records | Can store the new record Id in a variable |
| **Update Records** | Changes existing records | Find them by conditions, or use a record or collection |
| **Record variable** | Holds one record's field values | Write it with one element |
| **Record collection** | Holds many records | Write them all with one element |

---

## Interview Q&A

### 1. How do you set the fields in Create Records?

You can set fields **one by one** with values or resources, or use **all values from a record variable** that you built earlier.

> **Tip:** Required fields and validation rules still apply when the record is created.

### 2. How do you get the Id of the new record?

Choose to **store the Id** of the new record in a variable. Then use that Id in later elements, such as linking a child record.

> **Tip:** Create the parent first, then the children.

### 3. How can Update Records find the records to change?

Two ways: **specify conditions** and set fields directly, or **use the Ids and values from a record variable or collection**.

> **Tip:** With conditions you do not need a Get Records first, but check your filter carefully.

### 4. When do you use a record variable?

When you need to change a record you already hold, such as the one from Get Records. Assign the new field values to the variable, then update with it.

> **Tip:** The values in the variable are what get written, so check what it holds first.

### 5. How do you create or update many records?

Add each record to a **collection variable** with an **Assignment** inside the loop. After the loop, use **one** Create Records or Update Records on the whole collection.

> **Tip:** Never put Create, Update or Delete inside the loop.

### 6. What if the save fails?

Add a **fault path** to the element. Show a clear message or log the error, so the user is not left with a vague failure.

> **Tip:** Validation rules and required fields are the usual cause.

---

## Scenario Question

**"After the rep reviews the open Opportunity, create a follow-up Task and note it on the Opportunity."**

1. **Create Records** for the Task, storing the new Task Id
2. **Assignment**: set the Opportunity variable's **NextStep** to a short note
3. **Update Records** using the Opportunity record variable
4. Add **fault paths** to both, then show a confirmation screen

---

## Hands-On: Try It in Your Own Org

1. Open your Screen Flow from this series and keep the Get Records element for the open Opportunity.
2. Add **Create Records** for **Task**. Set **Subject** to `{!Default_Subject}` and **ActivityDate** to `{!DueDate}`. Link it with **WhatId** set to the Opportunity Id.
3. Choose to **store the Id** of the new Task in a variable named `NewTaskId`.
4. Add an **Assignment** that sets `{!Get_Open_Opportunity.NextStep}` to `Follow-up task created`.
5. Add **Update Records** using the **Ids and all values from the record variable** `{!Get_Open_Opportunity}`.
6. Add **fault paths** to both elements that lead to a screen with `{!$Flow.FaultMessage}`.
7. **Debug**, then open the Opportunity to check the Next Step and the new Task.

---

## Quick Cheat Sheet

- **Create Records** = new records, can store the new Id
- **Update Records** = by conditions, or by record or collection
- **Record variable** = one record, **collection** = many
- **Loop** = Assignment adds to a collection
- **After the loop** = one Create or Update
- **Fault path** on every element that saves

## Key Takeaways

- Build records in variables, then write them with one element.
- Store the Id of a new record when later steps need it.
- Never run Create, Update or Delete inside a loop.
- Add a fault path so errors are readable.

**Next up:** the Delete Records element and the Roll Back Records element: when to use each and how to stay safe.

*Part of #120DaysOfSalesforce. Do you update by conditions or by record variable? Tell me below.*
