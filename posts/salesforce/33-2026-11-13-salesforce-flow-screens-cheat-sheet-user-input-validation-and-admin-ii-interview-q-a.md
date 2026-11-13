---
title: "Salesforce Flow Screens Cheat Sheet: User Input, Validation and Admin II Interview Q&A"
date: 2026-11-13T14:35:26+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-flow-screens-cheat-sheet-user-input-validation-and-admin-ii-interview-q-a
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/a4c64a51-3c86-4942-bf10-2883f4fe65ab.png
tags: ["Salesforce", "Salesforce Flow", "Salesforce Admin", "trailblazer"]
brief: "Screens are how a Flow talks to the user. Admin II interviews ask about them because input, validation and navigation decide whether a Screen Flow is easy…"
series: "Salesforce"
serial: 33
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-flow-screens-cheat-sheet-user-input-validation-and-admin-ii-interview-q-a). This is an automated backup; read and comment on the blog.

*Screens are how a Flow talks to the user. Admin II interviews ask about them because input, validation and navigation decide whether a Screen Flow is easy to use and safe to trust.*

---

## The 4 Building Blocks

| Block | What it does | Key point |
| --- | --- | --- |
| **Input components** | Collect text, numbers, dates and more | The value is stored for later elements |
| **Choice components** | Radio buttons, picklists, checkboxes | Fed by a choice or a choice set |
| **Display components** | Show text, sections and messages | Guide the user |
| **Validation** | Required, or a formula with an error message | Stops bad data early |

---

## Interview Q&A

### 1. What is a Screen element?

The element that **shows a user interface** and collects input. Screens only work in **Screen Flows**, not in record-triggered or autolaunched flows.

> **Tip:** Use a Screen whenever a person has to type or choose something.

### 2. How do you use what the user entered?

Each screen component keeps its value. Reference it with the component's API name, for example `{!Subject.value}`, in later elements such as Create Records.

> **Tip:** Give components clear API names. You will type them a lot.

### 3. How do you validate input?

Mark a field **Required**, or open its **Validate Input** setting and add a formula with an **error message**. The user cannot continue until the formula is true.

> **Tip:** Stop bad data at the screen, not after it is saved.

### 4. Can you hide components?

Yes. Set **Component Visibility** conditions on a field or a section, so it only appears when an earlier answer calls for it.

> **Tip:** Show only what the user needs for this case.

### 5. Where do choices come from?

Create a **Choice** resource for a fixed option, or a **Record Choice Set** or **Picklist Choice Set** to load options from records or from a field's picklist values.

> **Tip:** Build a choice set once and reuse it across screens.

### 6. How does the user move through the flow?

With the **Next, Previous and Finish** buttons. You choose which of them each screen shows, and whether the user can go back.

> **Tip:** Check the Back button on every screen. Going back can change data you already saved.

---

## Scenario Question

**"Let sales reps log a call from a Screen Flow."**

1. **Screen:** Subject (text), Priority (picklist), Due Date (date)
2. **Create Records:** a Task, with fields from the screen inputs
3. **Confirmation screen** that shows the new Task Id
4. **Fault path** on Create Records, then **Debug**

---

## Hands-On: Try It in Your Own Org

1. Create a **Screen Flow** and add a **Screen** with a Text input named `Subject`.
2. Add a **Picklist** choice for Priority and a **Date** input for Due Date.
3. Make Subject **Required**, and add a Validate formula so the date cannot be in the past.
4. Add **Create Records** for Task and map the three inputs.
5. Add a confirmation screen, run **Debug**, then add the flow to a Lightning page.

---

## Quick Cheat Sheet

- **Show UI** = Screen
- **Read input** = `{!Name.value}`
- **Block bad data** = Validate Input
- **Hide fields** = Component Visibility
- **Pick from a list** = Choice or choice set
- **Save the data** = Create Records after the screen

## Key Takeaways

- Screens belong to Screen Flows.
- Validate on the screen.
- Reuse choice sets.
- Save once, after the user is done.

**Next up:** running a Screen Flow from buttons, Lightning pages and quick actions.

*Part of #120DaysOfSalesforce. Which Screen component do you use most? Tell me below.*
