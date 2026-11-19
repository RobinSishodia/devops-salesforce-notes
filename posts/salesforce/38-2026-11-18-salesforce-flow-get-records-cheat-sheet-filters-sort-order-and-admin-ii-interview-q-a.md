---
title: "Salesforce Flow Get Records Cheat Sheet: Filters, Sort Order and Admin II Interview Q&A"
date: 2026-11-18T14:24:05+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-get-records-cheat-sheet-filters-sort-order-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/64d2b98b-9942-47ce-b22d-1934f6f1dcf6.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Almost every flow starts by reading data. The Get Records element is where that happens, and Admin II interviews love to ask how to set it up and what…"
series: "Salesforce"
serial: 38
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-get-records-cheat-sheet-filters-sort-order-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Almost every flow starts by reading data. The Get Records element is where that happens, and Admin II interviews love to ask how to set it up and what happens when nothing comes back.*

---

## Get Records at a Glance

| Setting | What it does | Key point |
| --- | --- | --- |
| **Object** | Which object to query | One object per element |
| **Filter conditions** | Which records to find | AND, OR or custom logic |
| **Sort order** | Which record comes first | Pick a field and direction |
| **How many records** | Only the first, or all matching | First record = one record variable; all = a collection |
| **Which fields to store** | What the flow keeps | Choose only the fields you need |

---

## Interview Q&A

### 1. What does Get Records do?

It finds records in your org that match your conditions and stores them in the flow, so later elements can use them.

> **Tip:** One element queries one object.

### 2. How do you filter the results?

Add **filter conditions** on fields. Choose **All Conditions Are Met (AND)**, **Any Condition Is Met (OR)** or **Custom Condition Logic**.

> **Tip:** Filter as tightly as you can, so you do not read records you do not need.

### 3. First record or all records?

Choose **Only the first record** when you expect one result, such as the Account for a recordId. Choose **All records** when you need a list, which is stored in a **collection**.

> **Tip:** Add a sort order so "first" is the one you mean, such as the newest.

### 4. Which fields should you store?

You can store all fields, or choose only the ones you need. Choosing fields is better for performance and keeps the flow lean.

> **Tip:** Fields you do not store are empty later. Store what you will use.

### 5. What if no record is found?

The result is empty (null). Add a **Decision** with the condition "Is Null" for that record or collection, and handle the empty case instead of letting the flow fail later.

> **Tip:** Always plan for zero results.

### 6. Why not put Get Records inside a loop?

Each Get Records is a query, and a flow has limits on queries in one transaction. Query **before** the loop, and loop over the collection.

> **Tip:** Same idea for Create, Update and Delete: do them after the loop.

---

## Scenario Question

**"A rep opens an Account and the flow must show the most recent open Opportunity."**

1. Add **Get Records** on **Opportunity**
2. Filter: **AccountId equals {!recordId}** AND **IsClosed equals False**
3. Sort by **CloseDate**, then store **only the first record**
4. Add a **Decision** to check if the result is null, then show a screen with the Opportunity name and amount

---

## Hands-On: Try It in Your Own Org

1. Open your Screen Flow from this series in Flow Builder.
2. Add a **Get Records** element, label it `Get Open Opportunity`, object **Opportunity**.
3. Set conditions with **All Conditions Are Met (AND)**: `AccountId` equals `{!recordId}` and `IsClosed` equals `False`.
4. Sort by `CloseDate` ascending and choose **Only the first record**. Store only the fields **Name** and **Amount**.
5. Add a **Decision** named `Found?` with the outcome `Is Null` for `{!Get_Open_Opportunity}` set to **True**, and a default outcome for found.
6. Add one screen for each path, showing `{!Get_Open_Opportunity.Name}` on the found path and a short message on the empty path.
7. **Debug** the flow with an Account that has an open Opportunity, then with one that does not.

---

## Quick Cheat Sheet

- **One object** per Get Records element
- **Filters**: AND, OR or custom logic
- **Sort** so the first record is the one you want
- **First record** = record variable, **all records** = collection
- **Store only the fields you need**
- **No result** = null, so check with a Decision
- **Never inside a loop**

## Key Takeaways

- Get Records reads data into the flow, so set it up carefully.
- Tight filters and chosen fields keep flows fast.
- Always handle the case where nothing is found.
- Query before a loop, not inside it.

**Next up:** the Create Records and Update Records elements: record variables, collections and what each one writes.

*Part of #120DaysOfSalesforce. How do you handle the "no records found" case? Tell me below.*
