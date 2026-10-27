---
title: "Salesforce Data Backup & Recovery Cheat Sheet: Data Export, Recycle Bin and Admin Interview Q&A (Day 21/30)"
date: 2026-10-27T13:39:21+00:00
canonical_url: https://sishodiarobin.hashnode.dev/salesforce-data-backup-recovery-cheat-sheet-data-export-recycle-bin-and-admin-interview-q-a-day-21-30
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/3d95ec16-33f2-4ca1-9a85-d78d31dad1ee.png
tags: ["Salesforce", "Salesforce Admin", "Backup"]
brief: "Back up before you need it. Deleted data is only safe while a copy exists. Backup and recovery questions come up in almost every admin interview. A Setup…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/salesforce-data-backup-recovery-cheat-sheet-data-export-recycle-bin-and-admin-interview-q-a-day-21-30). This is an automated backup; read and comment on the blog.

*Back up before you need it. Deleted data is only safe while a copy exists. Backup and recovery questions come up in almost every admin interview.*

---

## The 4 Building Blocks

| Block | What it is | Key point |
| --- | --- | --- |
| **Data Export** | Zip of CSV files | Weekly or monthly |
| **Recycle Bin** | Deleted records kept | 15 days to restore |
| **Metadata** | Setup is not in export | Use sandboxes or Git |
| **Recovery** | Restore from your files | Plan before you need it |

---

## Interview Q&A

### 1. What is Data Export?

A Setup tool that creates a **zip of CSV files** of your data, weekly or monthly.

> **Tip:** It exports records only.

### 2. How long are export files kept?

The download link **expires after 48 hours**, so download it quickly.

> **Tip:** Save a copy elsewhere.

### 3. What is the Recycle Bin?

It holds **deleted records for 15 days** so you can restore them.

> **Tip:** Hard delete skips it.

### 4. Is metadata in the export?

**No.** Data Export saves records, not setup. Use sandboxes, change sets or Git.

> **Tip:** Back up data and setup.

### 5. Can Salesforce restore lost data?

The old recovery service was **retired**, so keep your own backups.

> **Tip:** Do not rely on support.

### 6. What other backup options exist?

**Data Loader, reports, the paid Backup and Restore, or AppExchange tools.**

> **Tip:** Pick by size and speed.

---

## Scenario Question

**"A user deleted 500 accounts by mistake. What now?"**

1. **Check** the Recycle Bin first
2. **Restore** the deleted records
3. **Use** the last export if they were purged
4. **Schedule** regular exports

---

## Quick Cheat Sheet

- **Export** = records zip
- **Recycle Bin** = 15 days
- **Link** = 48 hours
- **Metadata** = separate
- **Hard delete** = gone
- **Schedule** = weekly

## Key Takeaways

- Schedule exports, do not wait
- Test your restore plan
- Back up data and metadata
- Limit who can delete

---

**When did you last test a restore? Tell me in the comments!**

*Following my 30-day daily blogging journey. Day 21 done, 9 to go.*
