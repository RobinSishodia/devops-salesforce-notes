---
title: "The Salesforce Security Model Explained: OWD, Roles, Sharing Rules and More"
date: 2026-10-04T20:22:10+00:00
canonical_url: https://sishodiarobin.hashnode.dev/the-salesforce-security-model-explained-owd-roles-sharing-rules-and-more
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/6f286a06-ea1b-4783-a01f-cc2392918012.png
tags: ["Salesforce", "Salesforce Admin", "Security", "crm"]
brief: "\"Why can't this user see that record?\" is one of the most common questions a Salesforce admin gets. The answer is almost always somewhere in the security model, which works in layers. Once you know th"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/the-salesforce-security-model-explained-owd-roles-sharing-rules-and-more). This is an automated backup; read and comment on the blog.

"Why can't this user see that record?" is one of the most common questions a Salesforce admin gets. The answer is almost always somewhere in the **security model**, which works in layers. Once you know the layers, troubleshooting becomes a checklist.

## Layer 1: Org-level access

Who can log in at all, and when.

- Active user and license
- Login hours and login IP ranges (on profiles)
- Multi-factor authentication
- Session settings

## Layer 2: Object-level access

Can the user work with this *type* of record at all? Controlled by **profiles** and **permission sets** with Create, Read, Edit, Delete, View All and Modify All.

If a user has no Read on Opportunity, nothing else matters. They won't see any opportunities.

## Layer 3: Field-level security

Within an object, which **fields** can the user see or edit? Also set on profiles and permission sets.

Removing a field from a page layout only hides it from that layout. It does **not** secure it. The field can still appear in reports, list views and the API. Use field-level security for real restrictions.

## Layer 4: Record-level access (sharing)

Which individual **records** can the user see? This is where most of the complexity lives.

### Organization-Wide Defaults (OWD)

OWD sets the **baseline** for each object:

- **Private** – only the owner (and people above them in the role hierarchy) can see it
- **Public Read Only** – everyone can see, only the owner can edit
- **Public Read/Write** – everyone can see and edit
- **Controlled by Parent** – for detail records in a master-detail relationship

Rule of thumb: **set OWD to the most restrictive level anyone needs, then open access up.** Sharing can only grant access, never take it away.

### Role hierarchy

Users higher in the hierarchy can see records owned by users below them (for standard objects this is always on; for custom objects it is controlled by the "Grant Access Using Hierarchies" setting). Roles reflect *data visibility*, not necessarily the org chart.

### Sharing rules

Sharing rules open access to groups of users:

- **Owner-based** – share records owned by the Sales India role with the Support India role
- **Criteria-based** – share all Cases where `Region = APAC` with a public group

### Teams and manual sharing

- **Account, Opportunity and Case Teams** give specific people access to specific records.
- **Manual sharing** lets an owner share one record with someone.

### Restriction rules

Restriction rules go the other way: they **limit** which records a user can see even when they would otherwise have access. They're useful for cases like letting users see only the records relevant to their region.

## A troubleshooting checklist

When a user can't see or edit something:

1. Is the user active with the right license?
2. Does their profile or a permission set grant **object** access?
3. Is **field-level security** hiding the field?
4. What is the **OWD** for the object?
5. Where are they in the **role hierarchy** relative to the owner?
6. Does a **sharing rule**, team or manual share apply?
7. Is a **restriction rule** limiting them?

Use **Sharing Settings**, the record's **Sharing Hierarchy** button and the **"View Summary"** on a user's permissions to check quickly.

## Profiles vs permission sets

Salesforce is moving towards **permission sets and permission set groups** as the main way to grant access, with profiles kept minimal. I'll cover that in a dedicated post later this month.

Get the layers straight and most "I can't see it" tickets take minutes instead of hours.
