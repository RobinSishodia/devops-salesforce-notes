---
title: "Amazon Route 53 Basics: DNS Records, Alias Records and Routing Policies"
date: 2026-11-27T03:26:24+00:00
canonical_url: https://sishodiarobin.hashnode.dev/amazon-route-53-basics-dns-records-alias-records-and-routing-policies
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/ed564bbe-b6e8-48d9-b3ee-6f7e7f235cc5.png
tags: ["AWS", "Amazon Route 53", "Cloud Computing", "Devops"]
brief: "Amazon Route 53 is the AWS DNS service. It turns names like app.example.com into IP addresses or AWS resources, and it can also send users to different…"
series: "DevOps & AWS"
serial: 59
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/amazon-route-53-basics-dns-records-alias-records-and-routing-policies). This is an automated backup; read and comment on the blog.

Amazon Route 53 is the AWS DNS service. It turns names like `app.example.com` into IP addresses or AWS resources, and it can also send users to different places by rule. It is a global service and sits in front of many of the services in this series.

## What it does

- **Registers domains** and hosts **DNS zones** for them.
- Answers DNS queries with the **records** you create.
- Can **check the health** of endpoints and stop sending traffic to unhealthy ones.
- Supports **routing policies** such as simple, weighted, latency-based and failover.

## Key concepts

| Piece | What it is |
| --- | --- |
| **Hosted zone** | The container for a domain's DNS records |
| **Record** | One DNS entry, such as A, AAAA, CNAME or MX |
| **Alias record** | A Route 53 record that points to an AWS resource, with no extra charge for queries |
| **TTL** | How long resolvers cache an answer |
| **Routing policy** | The rule that decides which answer is returned |
| **Health check** | A probe that marks an endpoint healthy or unhealthy |

## Good to know

- Use an **alias record** for the root of a domain, such as `example.com`, because a CNAME is not allowed there.
- A **low TTL** makes changes spread faster, but causes more queries.
- **Simple** routing returns one value or a set of values.
- **Weighted** routing splits traffic, which helps with canary releases.
- **Failover** routing sends traffic to a backup when the primary health check fails.
- **Latency-based** routing picks the Region with the lowest latency for the user.
- A **private hosted zone** answers names only inside your VPCs.

## Hands-on: try it in your own account

1. Open **Route 53** and choose **Hosted zones**. Use a domain you own, or create a **private hosted zone** for a practice name such as `demo.internal` linked to a VPC.
2. Choose **Create record**.
3. Create an **A record** named `app` with a test IP address and a TTL of **60 seconds**.
4. Open the record and test it with the **Test record** button, or query it with `dig` or `nslookup`.
5. Create a second record with a **weighted** policy and a different weight to see how answers are split.
6. Change the value and watch the answer update after the TTL.
7. Clean up: delete the records and the practice hosted zone, because hosted zones have a monthly charge.

## Common mistakes

- Using a CNAME at the root of a domain instead of an alias record.
- Leaving a very high TTL and waiting hours for a change.
- Forgetting that a hosted zone has a monthly cost.
- Creating records in a public zone when the name should stay private.
- Setting up failover without a health check.

## Key takeaways

- Route 53 turns names into answers and can route by policy.
- Use alias records for AWS resources and the domain root.
- Pick the TTL to match how often you change records.
- Add health checks to failover routing and clean up practice zones.

Tomorrow I'll start a new AWS topic.

*Part of #120DaysOfAWS.*
