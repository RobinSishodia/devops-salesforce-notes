---
title: "AWS KMS: How Encryption Keys Protect Your Data in AWS"
date: 2026-11-20T16:22:49+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-kms-how-encryption-keys-protect-your-data-in-aws
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/2594b291-6f48-4412-97d1-677fa75e3830.png
tags: ["AWS", "Aws kms", "Cloud Computing", "Devops"]
brief: "Secrets Manager and Parameter Store both lean on one thing underneath: AWS KMS, the Key Management Service. KMS creates and controls the encryption keys…"
series: "DevOps & AWS"
serial: 54
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-kms-how-encryption-keys-protect-your-data-in-aws). This is an automated backup; read and comment on the blog.

Secrets Manager and Parameter Store both lean on one thing underneath: **AWS KMS**, the Key Management Service. KMS creates and controls the encryption keys that many AWS services use to protect your data.

## What KMS does

- It creates and manages **KMS keys**, and these keys never leave the service in plain form.
- Other services, such as S3, EBS and Secrets Manager, call KMS to encrypt and decrypt data for you.
- Every use of a key can be controlled with permissions and recorded in **CloudTrail**.
- Keys are **Regional**. A key lives in the Region where you create it.

## Types of keys

| Type | Who manages it | Notes |
| --- | --- | --- |
| **AWS owned key** | AWS | Used by some services behind the scenes, and you do not see it |
| **AWS managed key** | AWS, in your account | Named like `aws/s3`, rotated automatically, and you cannot change its policy |
| **Customer managed key** | You | You control the key policy, aliases, rotation and deletion |

## Key concepts

- **Key policy**: the main access control for a key. IAM policies can only grant access if the key policy allows it.
- **Alias**: a friendly name such as `alias/demo-key`, which points to a key.
- **Symmetric key**: one key for both encrypt and decrypt. It is the default type.
- **Envelope encryption**: KMS encrypts a small **data key**, and the data key encrypts the large data. The direct Encrypt call is limited to 4 KB.
- **Key rotation**: for customer managed keys you can turn on automatic rotation.

## Hands-on: try it in your own account

1. Create a key: `aws kms create-key --description "demo key"` and note the `KeyId`.
2. Add an alias: `aws kms create-alias --alias-name alias/demo-key --target-key-id <KeyId>`
3. Make a file: `echo "hello kms" > hello.txt`
4. Encrypt it: `aws kms encrypt --key-id alias/demo-key --plaintext fileb://hello.txt --query CiphertextBlob --output text | base64 --decode > hello.enc`
5. Decrypt it: `aws kms decrypt --ciphertext-blob fileb://hello.enc --query Plaintext --output text | base64 --decode`
6. Turn on rotation: `aws kms enable-key-rotation --key-id <KeyId>`
7. In the console, open the key and read its **key policy**.
8. Clean up: `aws kms delete-alias --alias-name alias/demo-key`, then `aws kms schedule-key-deletion --key-id <KeyId> --pending-window-in-days 7`

## Common mistakes

- Scheduling a key for deletion while data still depends on it. Once the key is gone, that data cannot be decrypted.
- Using a broad permission such as `kms:*` when a role only needs to encrypt and decrypt.
- Forgetting that the key policy must allow access, even when the IAM policy does.
- Trying to encrypt large files directly instead of using envelope encryption.
- Leaving practice keys behind. A customer managed key is billed per month, plus requests.

## Key takeaways

- KMS creates and controls the keys that protect your data across AWS.
- The key policy decides who can use a key, so write it carefully.
- Use customer managed keys when you need control over policy, rotation and deletion.
- Plan before you delete a key, and clean up practice keys.

Tomorrow I'll look at AWS Backup and how to protect your data with scheduled backups.

*Part of #120DaysOfAWS.*
