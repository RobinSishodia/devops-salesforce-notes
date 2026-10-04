---
title: "Building a Salesforce CI/CD Pipeline with GitHub Actions and Scratch Orgs"
date: 2026-10-01T10:48:20+00:00
canonical_url: https://sishodiarobin.hashnode.dev/building-a-salesforce-ci-cd-pipeline-with-github-actions-and-scratch-orgs
cover_image: https://cdn.hashnode.com/uploads/covers/6693dc4e158429a5c6ab492f/2c6b9ae1-df24-4a14-a975-a9660b8dc57d.png
tags: ["Salesforce", "Devops", "github-actions", "ci-cd", "salesforce development"]
brief: "Most Salesforce teams still move changes between orgs by hand: build in a sandbox, add components to a change set, upload, validate, deploy, and hope nothing was missed. I wanted to see what the \"real"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/building-a-salesforce-ci-cd-pipeline-with-github-actions-and-scratch-orgs). This is an automated backup; read and comment on the blog.

Most Salesforce teams still move changes between orgs by hand: build in a sandbox, add components to a change set, upload, validate, deploy, and hope nothing was missed. I wanted to see what the "real" DevOps way looks like on the Salesforce platform, so I built a small metadata CI/CD pipeline from scratch using **Salesforce DX, GitHub Actions and scratch orgs**.

In this post I'll walk through what the pipeline does, how it's wired together, and the one problem that cost me the most time.

**Repo:** [github.com/RobinSishodia/salesforce-devops-pipeline](https://github.com/RobinSishodia/salesforce-devops-pipeline)

## The goal

Every pull request into `main` should be checked automatically before anyone merges it:

1. Spin up a brand-new, empty **scratch org**
2. **Deploy** all the metadata from the branch into it
3. Run the **Apex tests** with code coverage
4. **Delete** the scratch org, pass or fail

If the deploy or any test fails, the PR shows a red check and the change doesn't go in. This is the same "validate before merge" idea used in any CI pipeline, applied to Salesforce metadata.

## What you need

- A **Salesforce Developer Edition org** with **Dev Hub** enabled (Setup → Dev Hub). The Dev Hub is the org that is allowed to create scratch orgs.
- The **Salesforce CLI** (`sf`), VS Code and Git
- A **GitHub repository** for the Salesforce DX project
- A **connected app** in the Dev Hub configured for **JWT (certificate-based) login**, so GitHub Actions can log in without a browser

## Project structure

The repo is a standard Salesforce DX project:

```
force-app/main/default/            # metadata source (Apex, objects, LWC...)
config/project-scratch-def.json    # what the scratch org should look like
sfdx-project.json                  # project manifest
.github/workflows/validate-pr.yml  # the pipeline
```

Working "source-first" like this is the key shift: the Git repo, not an org, is the source of truth.

## Step 1: Let GitHub Actions log in to the Dev Hub

CI can't click through a browser login, so I used the **JWT bearer flow**:

1. Generate a private key and self-signed certificate with OpenSSL
2. Upload the certificate to a connected app in the Dev Hub and pre-authorize the user
3. Store the secrets in GitHub (**Settings → Secrets and variables → Actions**):
   - `SF_JWT_KEY` – the private key
   - `SF_CONSUMER_KEY` – the connected app's consumer key
   - `SF_USERNAME` – the Dev Hub username
   - `SF_INSTANCE_URL` – the org's login URL

Nothing sensitive lives in the repo; the workflow only reads these secrets at run time.

## Step 2: The workflow

Here's the full `validate-pr.yml`:

```yaml
name: Validate PR against Scratch Org

on:
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install Salesforce CLI
        run: npm install --global @salesforce/cli

      - name: Authenticate to Dev Hub (JWT)
        run: |
          echo "${{ secrets.SF_JWT_KEY }}" > server.key
          sf org login jwt \
            --client-id ${{ secrets.SF_CONSUMER_KEY }} \
            --jwt-key-file server.key \
            --username ${{ secrets.SF_USERNAME }} \
            --instance-url ${{ secrets.SF_INSTANCE_URL }} \
            --alias DevHub --set-default-dev-hub

      - name: Create scratch org
        env:
          SF_SCRATCH_SIGNUP_CONNECTED_APP: PlatformCLI
          SF_SCRATCH_SIGNUP_CALLBACK_URL: http://localhost:1717/OauthRedirect
        run: |
          sf org create scratch \
            --definition-file config/project-scratch-def.json \
            --alias ci-scratch --duration-days 1 --set-default

      - name: Deploy metadata to scratch org
        run: sf project deploy start --target-org ci-scratch

      - name: Run Apex tests
        run: |
          sf apex run test \
            --target-org ci-scratch \
            --code-coverage --result-format human \
            --wait 20 --test-level RunLocalTests

      - name: Delete scratch org
        if: always()
        run: sf org delete scratch --target-org ci-scratch --no-prompt
```

A few details worth calling out:

- **`--duration-days 1`** keeps scratch orgs short-lived, so a failed cleanup doesn't tie up the Dev Hub's active scratch org allocation for long.
- **`RunLocalTests`** runs every test in the org except managed-package tests, which is what a production deployment requires anyway.
- **`if: always()`** on the delete step means the scratch org is cleaned up even when the deploy or tests fail.

## The problem that took the longest

Creating the scratch org kept failing even though the JWT login to the Dev Hub worked fine.

The cause: newer Developer Edition orgs use **External Client Apps** instead of classic connected apps, and the CLI couldn't use my app to sign in to the *new scratch org* it had just created. The fix was to tell the CLI to use Salesforce's built-in **PlatformCLI** app for the scratch-org signup step:

```yaml
env:
  SF_SCRATCH_SIGNUP_CONNECTED_APP: PlatformCLI
  SF_SCRATCH_SIGNUP_CALLBACK_URL: http://localhost:1717/OauthRedirect
```

After that, the full cycle ran end to end: create → deploy → test → delete.

## The result

I opened a pull request with a change, and GitHub Actions validated it automatically against a fresh scratch org. All checks passed, and the PR showed a green tick before merge. Every future change now gets the same treatment, with no manual change sets.

## What I learned

- **Git as the source of truth** makes Salesforce changes reviewable, just like application code.
- **Scratch orgs are disposable test environments**: every run starts clean, so there's no "works in my sandbox" drift.
- **JWT auth plus GitHub secrets** is the standard way to give CI access to an org safely.
- **Read the CLI error carefully.** The scratch-org failure looked like an auth problem but was really about which app the CLI uses for signup.

## What's next

The next part of this project is the **release side**: protecting the `main` branch so only validated PRs can merge, and adding **Copado** to manage environments and promote changes through a pipeline (dev → QA → production). I'll write that up in the next post.

If you're an admin moving into Salesforce DevOps, I'd love to hear how your team handles deployments. Connect with me on [LinkedIn](https://www.linkedin.com/in/robinsishodia).
