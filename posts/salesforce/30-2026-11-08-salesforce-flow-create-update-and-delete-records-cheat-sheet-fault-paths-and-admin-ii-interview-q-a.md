---
title: "Salesforce Flow Create, Update and Delete Records Cheat Sheet: Fault Paths and Admin II Interview Q&A"
date: 2026-11-08T17:54:09+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-create-update-and-delete-records-cheat-sheet-fault-paths-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/7e7c2a4b-9c75-45d2-9a0a-70a0dd57f738.png
tags: ["Salesforce", "flow", "120daysofsalesforce", "Salesforce Admin"]
brief: "Create Records, Update Records and Delete Records are how a Flow changes data. Admin II interviews ask about them because small choices here decide whether…"
series: "Salesforce"
serial: 30
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-create-update-and-delete-records-cheat-sheet-fault-paths-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Create Records, Update Records and Delete Records are how a Flow changes data. Admin II interviews ask about them because small choices here decide whether a Flow is safe, fast and bulk-ready.*

---

## The 3 Data Elements

| Element | What it does | Key point |
| --- | --- | --- |
| **Create Records** | Adds new records | Can store the new record Id |
| **Update Records** | Changes existing records | Filter, or pass a record or collection |
| **Delete Records** | Removes records | Use filters or a collection, and be careful |

---

## Interview Q&A

### 1. How does Create Records set field values?

Either **set the fields one by one**, or **use all values from a record variable or collection** you built earlier. Choose **Create multiple records** when you pass a collection.

> **Tip:** Build a collection, then create once.

### 2. How can Update Records pick what to change?

Two ways: **specify conditions and set fields individually**, or **use the Ids and all field values from a record or collection**. The first changes every record that matches the filter.

> **Tip:** Check the filter before you run it.

### 3. Why store the new record Id?

After Create Records you can **store the Id** in a variable. Use it to create related records, such as a Task linked to the new Case.

> **Tip:** Store the Id, then relate children to it.

### 4. How do you make a Flow bulk-safe?

Do the work on a **collection**: add records to it in the loop with an Assignment, and run **one Create, Update or Delete Records** after the loop.

> **Tip:** DML belongs outside the loop.

### 5. What is a fault path?

A **fault connector** that runs when a data element fails, for example on a validation rule error. Use it to show a message or log the error.

> **Tip:** Add a fault path to every data element.

### 6. Update Records or an Assignment on $Record?

In a **before-save** record-triggered flow, an Assignment on `$Record` changes the record with no extra DML. In an **after-save** flow, use **Update Records** to change the triggering record or related records.

> **Tip:** Before-save is faster for same-record updates.

---

## Scenario Question

**"When a Case is closed, create a follow-up Task and mark the related Contact as contacted."**

1. **Record-triggered flow** on Case, after save, when Status changes to Closed
2. **Create Records:** a Task, with `WhatId` set to the Case Id
3. **Update Records:** set the Contact's `Last_Contacted__c` field
4. **Fault path** on both elements, then **Debug**

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** with a text input for a Case subject.
2. Add **Create Records** for Case, set Subject from the input, and store the new Id in a variable.
3. Add **Update Records** that sets the same Case's Priority to High using that Id.
4. Add a **fault path** from each element to a screen that shows `{!$Flow.FaultMessage}`.
5. Run **Debug** and check the new Case in your org.

---

## Quick Cheat Sheet

- **Add** = Create Records
- **Change** = Update Records
- **Remove** = Delete Records
- **Many at once** = collection, one element after the loop
- **Failure** = fault path
- **Same record, before save** = Assignment on $Record

## Key Takeaways

- Work on collections, then save once.
- Store the Id to build related records.
- Add a fault path to every data element.
- Be careful with filters on Update and Delete.

**Next up:** the Loop element and how to process collections safely.

*Part of #120DaysOfSalesforce. Which data element do you use most? Tell me below.*
