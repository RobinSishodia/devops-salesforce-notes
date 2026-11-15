---
title: "Salesforce Flow Fault Paths Cheat Sheet: Handling Errors in Screen Flows and Admin II Interview Q&A"
date: 2026-11-15T16:30:55+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-fault-paths-cheat-sheet-handling-errors-in-screen-flows-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/36c68ff7-2a3f-4f9e-8ec0-d8c6fe0d1f6f.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Things go wrong, even in a good Screen Flow: a required field is empty, a record is locked, a validation rule fires. Admin II interviews ask how you handle…"
series: "Salesforce"
serial: 35
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-fault-paths-cheat-sheet-handling-errors-in-screen-flows-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Things go wrong, even in a good Screen Flow: a required field is empty, a record is locked, a validation rule fires. Admin II interviews ask how you handle it so the user sees a clear message instead of a scary error.*

---

## What Happens Without a Fault Path

If an element fails and you did nothing about it, the user sees a generic **unhandled fault** error and Salesforce emails the details to the admin. A **fault path** lets you decide what happens instead.

| Idea | What it means | Key point |
| --- | --- | --- |
| **Fault connector** | A second path out of an element that can fail | Drawn as a red dashed line |
| **Fault message** | The text of the error | `{!$Flow.FaultMessage}` |
| **Fault screen** | A screen that explains the problem | Shown instead of the crash |
| **Debug** | Run the flow with test data | Use it to trigger a failure on purpose |

---

## Interview Q&A

### 1. What is a fault path?

It is the path a flow takes when an element fails. You add it from the element with the **Fault** connector.

> **Tip:** Think of it as the "if this fails" branch.

### 2. Which elements can have one?

Elements that can fail, such as **Create, Update, Get and Delete Records**, **actions** and **subflows**. Screen elements do not get one.

> **Tip:** Put it on every element that changes data.

### 3. How do you show the error to the user?

Send the fault connector to a **Screen** and add a Display Text component with `{!$Flow.FaultMessage}`.

> **Tip:** Add a friendly sentence above it, such as "We could not save your call."

### 4. Should users see the raw message?

Usually not. Raw messages can be technical. Show a plain message to the user and keep the detail for the admin.

> **Tip:** Say what to do next, for example "Contact your admin."

### 5. How does the admin find out?

Salesforce sends a **flow error email** for unhandled faults. In your own fault path you can also send an email or create a record that logs the error.

> **Tip:** A log record is easier to search than a pile of emails.

### 6. How do you test it?

Use **Debug** and cause a failure on purpose, such as leaving a required field empty, then check that the fault screen appears.

> **Tip:** A fault path you never tested is a guess.

---

## Scenario Question

**"The call log flow sometimes fails and reps just see an error."**

1. Open the Screen Flow and find the **Create Records** element for the Task
2. Add a **Fault** connector from it to a new screen
3. Show a friendly message plus `{!$Flow.FaultMessage}`
4. Debug with a failing case, then **activate** the new version

---

## Hands-On: Try It in Your Own Org

1. Open yesterday's Screen Flow in Flow Builder.
2. On the **Create Records** element that creates the Task, choose **Add Fault Path**.
3. Add a **Screen** after it named `Something went wrong`.
4. In that screen add Display Text: `We could not save your call. Details: {!$Flow.FaultMessage}`
5. Run **Debug** and leave the Task **Subject** empty so the create fails.
6. Check that the fault screen appears, then **Save** and **Activate** the new version.

---

## Quick Cheat Sheet

- **Second path out** = Fault connector
- **Error text** = `{!$Flow.FaultMessage}`
- **Show it** = Fault screen
- **Screens** = no fault path
- **Test it** = Debug a failure
- **Unhandled** = Error email to admin

## Key Takeaways

- Add a fault path to every element that changes data.
- Show a friendly message, not a crash.
- Keep the technical detail for the admin.
- Test the failure on purpose.

**Next up:** Flow decisions and loops, the two elements behind most real flows.

*Part of #120DaysOfSalesforce. How do your flows handle errors? Tell me below.*
