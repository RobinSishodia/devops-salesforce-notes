---
title: "Salesforce Flow Delete and Roll Back Records Cheat Sheet: Removing Data Safely and Admin II Interview Q&A"
date: 2026-11-20T16:21:32+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-delete-and-roll-back-records-cheat-sheet-removing-data-safely-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/ddca9442-e244-4d91-bc29-11eed0a890bf.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "After Get, Create and Update comes the last of the data elements: Delete Records. It pairs with Roll Back Records, which undoes saves when something goes…"
series: "Salesforce"
serial: 40
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-delete-and-roll-back-records-cheat-sheet-removing-data-safely-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*After Get, Create and Update comes the last of the data elements: Delete Records. It pairs with Roll Back Records, which undoes saves when something goes wrong. Admin II interviews love this pair.*

---

## Delete and Roll Back at a Glance

| Element | What it does | Key point |
| --- | --- | --- |
| **Delete Records** | Deletes records | By conditions, or by a record or collection |
| **Roll Back Records** | Undoes pending record changes in the transaction | Used on a fault path after a failed save |
| **Fault path** | Where the flow goes when an element fails | Add it to elements that save or delete |
| **Transaction** | A group of changes saved together | A screen or Pause ends it |

---

## Interview Q&A

### 1. How does Delete Records find the records?

Two ways: **specify conditions** and delete every record that matches, or **use the Ids stored in a record variable or collection**.

> **Tip:** With conditions, test the filter first. A loose filter deletes more than you expect.

### 2. Where do deleted records go?

Deleted records can usually be restored from the **Recycle Bin** for a limited time. Deleting a parent record can also affect its child records, depending on the relationship.

> **Tip:** Check the relationship type before you delete a parent.

### 3. Should you delete inside a loop?

No. Collect the records in a **collection variable** with an **Assignment**, then use **one** Delete Records after the loop.

> **Tip:** The same rule applies to Create and Update.

### 4. What does Roll Back Records do?

It **reverses the record changes** made earlier in the current transaction, so the data goes back to how it was before those changes.

> **Tip:** It undoes record changes only, so plan what else the flow has already done.

### 5. When do you use it?

When the flow does **several saves in a row** and a later one fails. Put Roll Back Records on the **fault path** so a half-finished set of changes does not stay in the org.

> **Tip:** Then show the user a clear message with `{!$Flow.FaultMessage}`.

### 6. What is a transaction in a flow?

The group of changes that are saved together. In a Screen Flow, changes are saved when the flow reaches a **screen** or a **Pause**, so rolling back only reaches back to that point.

> **Tip:** Put related saves together, with no screen between them.

---

## Scenario Question

**"The flow creates a follow-up Task and then updates the Opportunity. If the update fails, the Task must not stay behind."**

1. **Create Records** for the Task, then **Update Records** for the Opportunity, with no screen between them
2. Add a **fault path** to the Update Records element
3. On the fault path, add **Roll Back Records**
4. Then show a screen with `{!$Flow.FaultMessage}`

---

## Hands-On: Try It in Your Own Org

1. Open your Screen Flow from this series with the Create Records (Task) and Update Records (Opportunity) elements.
2. Make sure there is **no screen** between the Create and the Update.
3. On the **fault path** of Update Records, add a **Roll Back Records** element named `Undo Changes`.
4. After it, add a screen that shows `{!$Flow.FaultMessage}`.
5. To test, add a validation rule on Opportunity that always fails for your test record, or temporarily set a required field to blank, then **Debug** the flow.
6. Check that no new Task was left behind, then remove your test rule.
7. Optional: add **Delete Records** on **Task** with the condition **Id equals** `{!NewTaskId}` to remove a test Task you created.

---

## Quick Cheat Sheet

- **Delete Records** = by conditions, or by record or collection
- **Recycle Bin** can restore deleted records for a limited time
- **Never delete inside a loop**
- **Roll Back Records** = undo record changes in this transaction
- **Use it on a fault path**
- **A screen or Pause ends the transaction**

## Key Takeaways

- Test the conditions before you delete records.
- Collect records in a collection, then delete once after the loop.
- Roll Back Records keeps a failed multi-step save from leaving partial data.
- Keep related saves together, with no screen between them.

**Next up:** subflows, and how to call one flow from another.

*Part of #120DaysOfSalesforce. Do you use Roll Back Records? Tell me below.*
