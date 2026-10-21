---
title: "Salesforce Sandboxes & Change Sets Cheat Sheet: Types, Validation and Admin Interview Q&A (Day 16/30)"
date: 2026-10-21T09:18:25+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-sandboxes-change-sets-cheat-sheet-types-validation-and-admin-interview-q-a-day-16-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/18b9c4e0-d2c0-4960-a653-ec1e1ef9572d.png
tags: ["Salesforce", "Salesforce Admin", "Devops"]
brief: "Build safely away from live users, then move the changes to production the controlled way. Sandboxes and change sets are core admin deployment topics and a…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-sandboxes-change-sets-cheat-sheet-types-validation-and-admin-interview-q-a-day-16-30). This is an automated backup; read and comment on the blog.

*Build safely away from live users, then move the changes to production the controlled way. Sandboxes and change sets are core admin deployment topics and a favourite interview question.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Sandbox** | Safe copy of production | Build and test here |
| **Outbound Set** | Built in the source org | Uploaded to the target |
| **Inbound Set** | Arrives in the target org | Validate, then deploy |
| **Validation** | Dry run with tests | Saves nothing |

---

## Interview Q&A

### 1. What is a sandbox?

A **copy of production metadata** where you build and test changes safely, away from live users.

> **Tip:** Never build in production.

### 2. What are the sandbox types?

**Developer and Developer Pro** copy metadata. **Partial Copy** adds sample data. **Full** copies everything.

> **Tip:** Match the type to the test.

### 3. What is a change set?

A **bundle of metadata components** you send from one org to another connected org.

> **Tip:** Metadata only, not data.

### 4. Outbound vs inbound?

**Outbound** is built and uploaded in the source org. **Inbound** waits in the target org to be validated and deployed.

> **Tip:** Outbound out, inbound in.

### 5. Why validate first?

A validation **runs the checks and tests without saving changes**, so you know the deploy will pass.

> **Tip:** Validate, then deploy.

### 6. What are the limits?

Change sets work **only between connected orgs**, some components are unsupported, and there is **no version history or easy rollback**.

> **Tip:** Name the limits, then mention Git and CI/CD.

---

## Scenario Question

**"Move a new validation rule and layout to production. How?"**

1. **Build** and test it in a sandbox
2. **Add** both to an outbound change set
3. **Upload** to production and validate
4. **Deploy** in a quiet window

---

## Quick Cheat Sheet

- **Sandbox** = safe copy of prod
- **Outbound** = sent from source
- **Inbound** = received in target
- **Validate** = dry run
- **Apex** = 75% test coverage
- **Limits** = no rollback

## Key Takeaways

- Build in a sandbox only
- Add every dependency to the set
- Validate before you deploy
- Deploy outside business hours

---

**What was your first deployment? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 16 done, 14 to go.*
