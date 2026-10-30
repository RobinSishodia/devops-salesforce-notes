---
title: "Salesforce Web-to-Lead & Web-to-Case Cheat Sheet: Forms, Limits, reCAPTCHA and Admin Interview Q&A (Day 24/30)"
date: 2026-10-30T17:30:07+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-web-to-lead-web-to-case-cheat-sheet-forms-limits-recaptcha-and-admin-interview-q-a-day-24-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/65d6c959-fb8c-4885-8020-82d51ec19302.png
tags: ["Salesforce", "Salesforce Admin", "crm"]
brief: "Turn website visitors into records without lifting a finger. Web-to-Lead and Web-to-Case come up in almost every admin interview. A generated HTML form…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-web-to-lead-web-to-case-cheat-sheet-forms-limits-recaptcha-and-admin-interview-q-a-day-24-30). This is an automated backup; read and comment on the blog.

*Turn website visitors into records without lifting a finger. Web-to-Lead and Web-to-Case come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Web-to-Lead** | HTML form makes leads | 500 per day |
| **Web-to-Case** | HTML form makes cases | 5,000 per day |
| **Form Fields** | Standard plus custom | Use the field ID |
| **Protection** | reCAPTCHA and routing | Stop the spam |

---

## Interview Q&A

### 1. What is Web-to-Lead?

A **generated HTML form** that creates leads from your website.

> **Tip:** No hand coding needed.

### 2. What are the daily limits?

**Web-to-Lead allows 500 a day.** Web-to-Case allows 5,000 a day.

> **Tip:** Plan for busy days.

### 3. How do you add custom fields?

Add the field to the HTML using its **field ID**.

> **Tip:** Test after adding.

### 4. What stops spam?

Turn on **reCAPTCHA** and validate the fields.

> **Tip:** Bots love open forms.

### 5. How do leads get an owner?

**Lead assignment rules** route them, or the default owner takes them.

> **Tip:** Rules run automatically.

### 6. Can customers get a reply?

**Yes**, auto-response rules email them on creation.

> **Tip:** Keep the template clear.

---

## Scenario Question

**"Website enquiries must become leads for sales. How?"**

1. **Generate** the form in Setup
2. **Add** reCAPTCHA and a return URL
3. **Set** assignment and auto-response
4. **Test** with a sample submit

---

## Quick Cheat Sheet

- **Form** = generated HTML
- **Lead cap** = 500 a day
- **Case cap** = 5,000 a day
- **Spam** = reCAPTCHA
- **Owner** = assignment rule
- **Reply** = auto-response

## Key Takeaways

- Generate the form, do not hand build
- Protect it with reCAPTCHA
- Route and reply automatically
- Test before going live

---

**Which form is on your site? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 24 done, 6 to go.*
