---
title: "Salesforce Scheduled Paths: Run Part of a Flow Later, with Admin II Interview Q&A"
date: 2026-11-25T09:16:42+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-scheduled-paths-run-part-of-a-flow-later-with-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/f17b28c2-e55c-4d99-a952-8293c14936ce.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Sometimes a flow should not finish everything on the spot. It may need to act later, after a delay or when a condition is met. Scheduled Paths and the Wait…"
series: "Salesforce"
serial: 44
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-scheduled-paths-run-part-of-a-flow-later-with-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Sometimes a flow should not finish everything on the spot. It may need to act later, after a delay or when a condition is met. Scheduled Paths and the Wait element do that, and Admin II interviews ask about both.*

---

## Scheduled Paths and Wait at a Glance

| Piece | What it does | Key point |
| --- | --- | --- |
| **Scheduled Path** | Runs part of a record-triggered flow at a set time after the trigger | Offset from the record or a date field |
| **Run Immediately path** | The normal path that runs right away | Always there, the scheduled paths are extra |
| **Wait element** | Pauses a flow until a time or event | Resumes later as a new transaction |
| **Paused interview** | The saved state of a waiting flow | Find it in Paused and Failed Flow Interviews |

---

## Interview Q&A

### 1. What is a Scheduled Path?

An extra path on a **record-triggered flow** that runs later, for example **3 days after** the record is created, or **1 day before** a date field.

> **Tip:** The record-triggered flow still starts on a save. Only the path runs later.

### 2. When do you use it?

For follow-ups that depend on time after a change, such as a reminder Task 3 days after a Case is opened, without building a separate Scheduled Flow.

> **Tip:** Use Scheduled Flow for a batch on a clock. Use a Scheduled Path for time after a record event.

### 3. What happens if the record changes before the path runs?

The path runs with the **latest** record values. If the record no longer meets the entry conditions, the scheduled path is **cancelled**.

> **Tip:** Check the entry conditions, they decide if the path still runs.

### 4. What does the Wait element do?

It **pauses** the flow until a set time passes or an event happens. The paused interview is saved and **resumes** later.

> **Tip:** Treat the resume as a new transaction.

### 5. Who does a scheduled path run as?

Like other automation that runs later, it runs as the **Automated Process** user, so set owners explicitly.

> **Tip:** Never rely on the running user for ownership.

### 6. How do you check a waiting or failed flow?

Open **Paused and Failed Flow Interviews** in Setup. You can see waiting interviews and resume or delete them.

> **Tip:** Check it when a scheduled follow-up did not happen.

---

## Scenario Question

**"When a Case is opened, create a reminder Task if the Case is still open 3 days later. How do you build it?"**

1. Create a **record-triggered flow** on Case when a record is **created**
2. Add a **Scheduled Path** set to **3 days after** the trigger
3. In the path, add a **Decision** that checks **Status is not Closed**
4. Add **Create Records** for the Task, with the owner set
5. Add a **fault path** and test in a sandbox

---

## Hands-On: Try It in Your Own Org

1. Go to **Setup > Flows > New Flow** and pick **Record-Triggered Flow**.
2. Choose **Case** and trigger on **A record is created**.
3. Under the Start element, choose **Add Scheduled Paths**.
4. Name it `Check After 3 Days` and set it to **3 Days After** the Case is created. For a quick test use a few minutes if your org allows it.
5. In the scheduled path, add a **Decision** that checks Status is not **Closed**.
6. Add **Create Records** for a Task with Subject = `Follow up on open Case` and WhatId = `{!$Record.Id}`.
7. Add a fault path, then **Save** and **Activate**.
8. Create a test Case, then check **Paused and Failed Flow Interviews** to see the waiting path.

---

## Common Mistakes

- Expecting the scheduled path to run right away.
- Forgetting the entry conditions, so the path is cancelled.
- Not checking the record status again inside the path.
- Forgetting that scheduled paths run as the **Automated Process** user.
- Leaving test flows active after the demo.

---

## Quick Cheat Sheet

- **Scheduled Path** = runs later after the trigger
- **Immediate path** = runs right away
- **Wait** = pause until a time or event
- **Entry conditions** = can cancel a path
- **Runs as** = Automated Process
- **Check** = Paused and Failed Flow Interviews

---

## Key Takeaways

- Use a Scheduled Path for follow-ups that happen after a record event.
- The path uses the latest data, and entry conditions can cancel it.
- Check the record again before you act.
- Set owners yourself and test in a sandbox.

**Next up:** a new topic in the Admin II series.

*Part of #120DaysOfSalesforce. Where would you use a scheduled path? Tell me below.*
