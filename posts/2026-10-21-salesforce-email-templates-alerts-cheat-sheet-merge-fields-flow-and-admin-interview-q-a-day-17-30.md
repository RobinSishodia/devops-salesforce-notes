---
title: "Salesforce Email Templates & Alerts Cheat Sheet: Merge Fields, Flow and Admin Interview Q&A (Day 17/30)"
date: 2026-10-21T21:48:50+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-email-templates-alerts-cheat-sheet-merge-fields-flow-and-admin-interview-q-a-day-17-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/0b369969-4282-466f-bf47-5184c6d0c9b7.png
tags: ["Salesforce", "Salesforce Admin", "Salesforce Flow"]
brief: "Write the email once, merge in the record data, and let automation send it at the right moment. Email templates and alerts are everyday admin work and a…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-email-templates-alerts-cheat-sheet-merge-fields-flow-and-admin-interview-q-a-day-17-30). This is an automated backup; read and comment on the blog.

*Write the email once, merge in the record data, and let automation send it at the right moment. Email templates and alerts are everyday admin work and a common interview topic.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Template** | Reusable email layout | Merge fields fill it in |
| **Email Alert** | Sends a template | Chosen recipients |
| **Letterhead** | Logo and brand colours | Wraps the template |
| **Org-Wide Address** | Trusted From address | Must be verified |

---

## Interview Q&A

### 1. What is an email template?

A **reusable email with merge fields** that fill in record data automatically.

> **Tip:** Write once, reuse everywhere.

### 2. What template types exist?

**Lightning templates** use a builder. **Classic** ones are text, HTML and Visualforce.

> **Tip:** Lightning is the modern default.

### 3. What is an email alert?

A **saved action that sends a template** to the recipients you choose.

> **Tip:** The alert sends, Flow decides when.

### 4. How do you trigger one?

From a **Flow or an approval process** when your condition is met.

> **Tip:** Use Flow for new work.

### 5. What are merge fields?

**Placeholders** like `{!Contact.FirstName}` swapped for real values when the email is sent.

> **Tip:** Test with a real record.

### 6. What are the limits?

A **daily send limit** applies, and emails can bounce or land in spam.

> **Tip:** Use an org-wide address.

---

## Scenario Question

**"Email the customer when a case is closed. How?"**

1. **Create** a template with merge fields
2. **Create** an email alert using it
3. **Add** it to a Flow on case closed
4. **Test** with a real case

---

## Quick Cheat Sheet

- **Template** = reusable email
- **Alert** = sends it
- **Merge field** = record data
- **Letterhead** = branding
- **Org-wide** = trusted sender
- **Flow** = decides when

## Key Takeaways

- Use merge fields, not typed names
- Send from an org-wide address
- Test before you activate
- One template per purpose

---

**Which email do you automate first? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 17 done, 13 to go.*
