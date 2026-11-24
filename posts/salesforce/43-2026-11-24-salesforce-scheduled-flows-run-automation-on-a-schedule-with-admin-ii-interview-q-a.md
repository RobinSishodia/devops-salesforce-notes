---
title: "Salesforce Scheduled Flows: Run Automation on a Schedule, with Admin II Interview Q&A"
date: 2026-11-24T18:11:37+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-scheduled-flows-run-automation-on-a-schedule-with-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/11d26c13-c2b9-4f7a-83a5-daa66c3d5c64.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Not every automation starts from a record change. A Scheduled Flow runs at a set time, on a set frequency, over a batch of records. Admin II interviews…"
series: "Salesforce"
serial: 43
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-scheduled-flows-run-automation-on-a-schedule-with-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Not every automation starts from a record change. A Scheduled Flow runs at a set time, on a set frequency, over a batch of records. Admin II interviews love it for cleanup and reminder jobs.*

---

## Scheduled Flows at a Glance

| Piece | What it does | Key point |
| --- | --- | --- |
| **Start element** | Sets the first run date, time and frequency | Once, Daily or Weekly |
| **Object + filters** | Pick which records the flow runs on | Filter so it only touches what it needs |
| **Run as** | Scheduled flows run as the **Automated Process** user | Set owner fields explicitly |
| **Batch size** | Records are processed in batches of up to 200 | Plan for volume |

---

## Interview Q&A

### 1. What is a Scheduled Flow?

An **autolaunched flow** that starts at a time you choose and repeats **Once, Daily or Weekly**. You can also pick an object and filters, and the flow runs once for each matching record.

> **Tip:** Use it when nothing changes on a record but time passes.

### 2. When do you use it instead of a record-triggered flow?

When the trigger is **time**, such as "every night, find Opportunities with no activity for 30 days", and not a save.

> **Tip:** If a record save starts it, use record-triggered. If a clock starts it, use scheduled.

### 3. Who does the flow run as?

The **Automated Process** user, not you. So fields like **Owner** or **Created By** may not be what you expect unless you set them.

> **Tip:** Set the owner explicitly when you create records.

### 4. How do you avoid running on too many records?

Add **filters** on the Start element, such as Stage, Last Activity Date or Status. Then handle records in a **collection** and save once, as you would in any flow.

> **Tip:** Filter first. Do not Get Records inside a loop.

### 5. How do you test it?

Use **Debug** on the flow, or set the start time a few minutes ahead in a **sandbox**. You can also check **Paused and Failed Flow Interviews** in Setup.

> **Tip:** Never test a scheduled flow first in production.

### 6. What are the limits to remember?

It follows the usual **governor limits**, and each batch of records runs as its own transaction. Very large volumes may need a different tool.

> **Tip:** For huge data jobs, ask if Batch Apex fits better.

---

## Scenario Question

**"Every night, create a follow-up Task for Opportunities that have had no activity for 30 days. How do you build it?"**

1. Create a **Schedule-Triggered Flow** that runs **Daily**
2. Pick **Opportunity** and filter on **Is Closed = False** and **Last Activity Date** older than 30 days
3. Add an **Assignment** that builds a Task and adds it to a **collection**
4. Use one **Create Records** on the collection, with the owner set
5. Add a **fault path** and test in a sandbox

---

## Hands-On: Try It in Your Own Org

1. Go to **Setup > Flows > New Flow** and choose **Schedule-Triggered Flow**.
2. Set the start to a few minutes from now, with frequency **Once**.
3. Choose the **Opportunity** object and add the filter **Is Closed = False**.
4. Add an **Assignment** that sets a Task record variable (Subject = `Check in`, WhatId = `{!$Record.Id}`).
5. Add the Task to a collection variable.
6. After the Assignment, add **Create Records** using the collection.
7. Add a fault path to Create Records.
8. Save, **Activate**, wait for the time, then check the new Tasks.

---

## Common Mistakes

- Forgetting the filters, so the flow runs on every record.
- Putting a **Create Records** inside a loop.
- Forgetting that the flow runs as the **Automated Process** user.
- Testing a scheduled flow in production first.
- Leaving a **Daily** flow running after the test.

---

## Quick Cheat Sheet

- **Trigger** = a time, not a save
- **Frequency** = Once, Daily, Weekly
- **Runs as** = Automated Process
- **Filter** = on the Start element
- **Save** = one collection, one Create
- **Test** = sandbox or Debug

---

## Key Takeaways

- Use a Scheduled Flow when time, not a record save, starts the work.
- Filter on the Start element so it only touches the records you need.
- Set the owner yourself, because it runs as the Automated Process user.
- Test in a sandbox and keep saves outside the loop.

**Next up:** a new topic in the Admin II series.

*Part of #120DaysOfSalesforce. Which scheduled job would you automate first? Tell me below.*
