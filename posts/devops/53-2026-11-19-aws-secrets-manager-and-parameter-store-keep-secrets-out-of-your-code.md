---
title: "AWS Secrets Manager and Parameter Store: Keep Secrets Out of Your Code"
date: 2026-11-19T17:07:19+00:00
canonical_url: https://sishodiarobin.hashnode.dev/aws-secrets-manager-and-parameter-store-keep-secrets-out-of-your-code
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/dcbe97b9-a87e-4f57-9bab-dff221ac0920.png
tags: ["AWS", "Secrets Manager", "Cloud Computing", "Devops"]
brief: "Systems Manager gave me a way into instances without SSH. The next question is where an application should keep its database password and settings so they…"
series: "DevOps & AWS"
serial: 53
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/aws-secrets-manager-and-parameter-store-keep-secrets-out-of-your-code). This is an automated backup; read and comment on the blog.

Systems Manager gave me a way into instances without SSH. The next question is where an application should keep its **database password and settings** so they never end up in code. AWS has two good answers: **Secrets Manager** and **Parameter Store**.

## The two services

- **AWS Secrets Manager** stores secrets such as database credentials and API keys, encrypts them with **AWS KMS**, and can **rotate** them automatically.
- **Systems Manager Parameter Store** stores configuration values and secrets in a **path-style hierarchy**, such as `/myapp/prod/db-host`.
- Both are accessed with an API call and controlled with **IAM permissions**.

## How they compare

|  | Secrets Manager | Parameter Store |
| --- | --- | --- |
| **Best for** | Credentials that need rotation | App settings and simple secrets |
| **Rotation** | Built in, using Lambda | Not built in |
| **Encryption** | Always, with KMS | Only for the **SecureString** type |
| **Cost** | Billed per secret per month, plus API calls | Standard parameters are free; Advanced parameters cost extra |
| **Size** | Larger values | Standard parameters are up to 4 KB |

Check the current pricing page before you rely on these numbers.

## Parameter types

- **String** for plain text such as a hostname
- **StringList** for comma-separated values
- **SecureString** for values encrypted with KMS

## Access with IAM

- The caller needs permission such as `secretsmanager:GetSecretValue` or `ssm:GetParameter`.
- For encrypted values it also needs permission to use the KMS key, such as `kms:Decrypt`.
- Give an application role only the paths or secrets it needs.

## Hands-on: try it in your own account

Use a fake value only. Never put a real password in a practice exercise.

1. Store a plain parameter: `aws ssm put-parameter --name /demo/app/db-host --value mydb.example.internal --type String`
2. Store an encrypted one: `aws ssm put-parameter --name /demo/app/db-password --value FakePassw0rd --type SecureString`
3. Read it back: `aws ssm get-parameter --name /demo/app/db-password --with-decryption`
4. List by path: `aws ssm get-parameters-by-path --path /demo/app --with-decryption`
5. Create a secret: `aws secretsmanager create-secret --name demo/db-credentials --secret-string '{"username":"admin","password":"FakePassw0rd"}'`
6. Read it: `aws secretsmanager get-secret-value --secret-id demo/db-credentials`
7. In the console, open the secret and look at the **Rotation** settings.
8. Clean up: `aws ssm delete-parameter --name /demo/app/db-host`, the same for `/demo/app/db-password`, and `aws secretsmanager delete-secret --secret-id demo/db-credentials --force-delete-without-recovery`

## Common mistakes

- Hardcoding passwords in code, in environment files or in a repository.
- Storing a secret as a plain **String** parameter.
- Giving a role access to every secret instead of the ones it needs.
- Printing secret values in logs or in screenshots.
- Forgetting to delete practice secrets, which keep costing money.

## Key takeaways

- Keep secrets out of code, and fetch them at runtime.
- Use Secrets Manager when you need rotation, and Parameter Store for settings and simple secrets.
- Use SecureString for anything sensitive in Parameter Store.
- Limit access by path or secret name, and clean up after practice.

Tomorrow I'll look at AWS KMS and how the encryption keys behind these services work.

*Part of #120DaysOfAWS.*
