---
title: "Salesforce Order of Execution: Where Flows Run When a Record Is Saved, with Admin II Interview Q&A"
date: 2026-11-27T03:24:10+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-order-of-execution-where-flows-run-when-a-record-is-saved-with-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/e0fd7067-c627-4620-85f9-fce8701fa5ed.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "\"What runs first when a record is saved?\" is a classic Admin II question. Knowing where flows, validation rules and triggers sit in the order of execution…"
series: "Salesforce"
serial: 45
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-order-of-execution-where-flows-run-when-a-record-is-saved-with-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*"What runs first when a record is saved?" is a classic Admin II question. Knowing where flows, validation rules and triggers sit in the order of execution helps you debug automation that behaves in surprising ways.*

---

## Order of Execution at a Glance

| Step | What runs | Key point |
| --- | --- | --- |
| **1** | **Before-save** record-triggered flows | Fast field updates on the same record |
| **2** | Before triggers (Apex) | Run after before-save flows |
| **3** | System and **custom validation rules** | Run after the before-save changes |
| **4** | Record is saved, **not yet committed** | Rollback is still possible |
| **5** | After triggers (Apex) | The record has an Id now |
| **6** | Workflow rules, then **after-save flows** | Flows can change the record again |
| **7** | **Commit** to the database | Post-commit work such as emails |

*This is a simplified view. Check the Salesforce Developer Guide for the full, current order.*

---

## Interview Q&A

### 1. What is the order of execution?

The fixed sequence Salesforce follows when a record is saved: before-save automation, validation, the save itself, after-save automation, then the commit.

> **Tip:** Remember the shape: before-save, validate, save, after-save, commit.

### 2. Where do before-save flows run?

At the **start**, before before triggers and before validation rules. They update fields on the triggering record without an extra save.

> **Tip:** Use them for fast field updates on the same record.

### 3. Do validation rules see before-save flow changes?

Yes. Validation rules run **after** before-save flows, so a flow can set a value that a validation rule then checks.

> **Tip:** If a rule fails unexpectedly, check what a before-save flow changed.

### 4. When do after-save flows run?

After the record is saved but before the commit. They are used to create or update **related** records, send emails and call actions.

> **Tip:** After-save flows can update the same record, but that causes an extra save.

### 5. What if an after-save flow updates the record again?

The update can fire automation again, and validation runs again. Salesforce caps the repeat so it cannot loop forever.

> **Tip:** Add entry conditions so the flow only runs when needed.

### 6. How do you control the order of several flows?

In **Flow Trigger Explorer** you can see the flows on an object and set the **trigger order** of record-triggered flows.

> **Tip:** Do not depend on the order, combine related logic where you can.

---

## Scenario Question

**"A validation rule blocks a save even though the user entered a valid value. How do you find out why?"**

1. Check for a **before-save flow** that changes the field first
2. Open **Flow Trigger Explorer** to list the flows on the object
3. Run the flow in **Debug** with the same record
4. Check **debug logs** for the order of what ran
5. Fix the flow's entry conditions, or the validation rule, and test in a sandbox

---

## Hands-On: Try It in Your Own Org

1. Create a text field `Order Test` on Account.
2. Create a **before-save** record-triggered flow on Account (create or update) that sets `Order Test` to `Before-save`.
3. Create a **validation rule** on Account that blocks the save when `Order Test` equals `Before-save`, with a clear message.
4. Create or update an Account and see that the validation rule fires, which shows the flow ran first.
5. Open **Setup > Flow Trigger Explorer**, pick Account, and look at the flows listed.
6. Turn on a **debug log** for your user and save again to see the order.
7. Clean up: delete the validation rule, deactivate the flow and delete the field.

---

## Common Mistakes

- Assuming validation rules run before flows.
- Updating the same record in an after-save flow when a before-save flow would do.
- Building several flows on one object that depend on an order.
- Skipping entry conditions, so a flow runs on every save.
- Debugging in production instead of a sandbox.

---

## Quick Cheat Sheet

- **First** = before-save flows
- **Then** = before triggers, validation rules
- **Save** = record saved, not committed
- **After** = after triggers, after-save flows
- **Last** = commit
- **Tool** = Flow Trigger Explorer and debug logs

---

## Key Takeaways

- Before-save flows run before validation rules.
- After-save flows run after the save but before the commit.
- Use entry conditions and a clear design instead of relying on order.
- Use Flow Trigger Explorer and debug logs when automation surprises you.

**Next up:** a new topic in the Admin II series.

*Part of #120DaysOfSalesforce. What was your trickiest order of execution bug? Tell me below.*
