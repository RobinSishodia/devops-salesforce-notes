---
title: "Salesforce Screen Flow Launch Cheat Sheet: Quick Actions, Lightning Pages and Admin II Interview Q&A"
date: 2026-11-14T12:09:47+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-screen-flow-launch-cheat-sheet-quick-actions-lightning-pages-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/76c209cb-b179-4ff2-b1d2-874e8b355206.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "A Screen Flow only helps if users can find it. Admin II interviews ask where you would launch one, how it knows which record it is on, and who is allowed…"
series: "Salesforce"
serial: 34
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-screen-flow-launch-cheat-sheet-quick-actions-lightning-pages-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*A Screen Flow only helps if users can find it. Admin II interviews ask where you would launch one, how it knows which record it is on, and who is allowed to run it.*

---

## The 4 Ways to Launch a Screen Flow

| Where | How | Key point |
| --- | --- | --- |
| **Quick action** | Action of type Flow on an object | Shows as a button on the record page |
| **Lightning page** | The Flow component | Runs inline on the page |
| **URL or button** | `/flow/FlowApiName` | Good for links and custom buttons |
| **Utility bar** | Flow utility item | Always available in the app |

---

## Interview Q&A

### 1. Why must the flow be active?

Users can only run an **active** flow. Activate it before you add it to a page, an action or a link.

> **Tip:** Test with Debug first, then activate.

### 2. How do you add a quick action?

In Object Manager, create an action of type **Flow**, pick the flow and give it a short label. Then add it to the **page layout** so the button appears.

> **Tip:** Keep the label short so it fits on the button.

### 3. How do you embed the flow on a page?

In the Lightning App Builder, drag the **Flow** component onto the page and choose the flow.

> **Tip:** One flow per section keeps the page clean.

### 4. How does the flow get the current record?

Create a **Text variable named `recordId`** and tick **Available for input**. Salesforce passes the record Id in when the flow runs from a record page.

> **Tip:** The variable name must match exactly.

### 5. Who can run it?

Users need access to the flow, for example the **Run Flows** permission, or access given through a profile or permission set.

> **Tip:** Test as a real user, not only as an admin.

### 6. What happens when the flow finishes?

Show a **confirmation screen**, or use the flow's finish setting to restart it or send the user elsewhere.

> **Tip:** End with a clear message so the user knows it worked.

---

## Scenario Question

**"Let reps log a call from the Account page."**

1. Build the **Screen Flow** with a `recordId` variable
2. **Activate** it
3. Create a **Flow quick action** on Account
4. Add it to the **page layout** and test as a rep

---

## Hands-On: Try It in Your Own Org

1. Open yesterday's Screen Flow and add a Text variable `recordId`, available for input.
2. Use `{!recordId}` as the `WhatId` when it creates the Task.
3. **Save** and **Activate** the flow.
4. In Object Manager, create a **Flow** quick action on Account and add it to the page layout.
5. Open an Account, run the action, and check that the Task is linked to that Account.

---

## Quick Cheat Sheet

- **Run from a record** = Quick action
- **Embed inline** = Flow component
- **Link to it** = `/flow/ApiName`
- **Know the record** = `recordId`
- **Must be** = Active
- **Access** = Run Flows

## Key Takeaways

- Activate before you place it.
- Use `recordId` for record context.
- Pick the launch spot that suits the user.
- Test as a real user.

**Next up:** Flow error handling and fault paths in Screen Flows.

*Part of #120DaysOfSalesforce. Where do your users launch Screen Flows? Tell me below.*
