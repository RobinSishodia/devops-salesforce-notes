---
title: "My First Hands-On DevOps Lab: Learning Linux, Git, and GitHub from Scratch"
date: 2026-10-30T23:50:49+00:00
canonical_url: https://sishodiarobin.hashnode.dev/my-first-hands-on-devops-lab-learning-linux-git-and-github-from-scratch
cover_image: 
tags: []
brief: "When I started learning DevOps, I wanted to understand everything together: Linux, Git, cloud infrastructure, automation, containers, and deployments. But…"
---

> Originally published at [sishodiarobin.hashnode.dev](https://sishodiarobin.hashnode.dev/my-first-hands-on-devops-lab-learning-linux-git-and-github-from-scratch). This is an automated backup; read and comment on the blog.

When I started learning DevOps, I wanted to understand everything together: Linux, Git, cloud infrastructure, automation, containers, and deployments. But I also wanted to understand every command I typed.

So I began with a small hands-on lab on an Ubuntu server. My starting point was a directory called `devops-lab` and a terminal.

This article captures the foundation: navigating Linux, working with files, and understanding how changes move from a local Git repository to GitHub. The commands below form a simple practice exercise you can adapt to your own lab.

## Why start with a small lab?

A deployment pipeline eventually runs commands on a machine, reads files, and works with a version of your code. Learning those basics makes the larger workflow easier to understand.

My goal at this stage is to explain what a command does, run it, inspect the result, and repeat it without blindly copying instructions.

## 1. Know where you are

In my Ubuntu lab, I started by checking my current directory:

```bash
pwd
```

The output was:

```text
/home/ubuntu/devops-lab
```

`pwd` means **print working directory**. It tells you where commands will operate unless you supply another path.

To create a similar workspace from your home directory:

```bash
mkdir -p ~/devops-lab
cd ~/devops-lab
pwd
```

Here is what each command does:

- `mkdir -p` creates the directory if it does not already exist.
- `~` refers to your user's home directory.
- `cd` changes your current directory.
- `pwd` confirms your location.

That final check is useful. Before creating or editing files, I want to know exactly where I am.

## 2. Create a file and inspect it

For a small practice example, create a README:

```bash
printf '# My DevOps Lab\n\nLearning Linux and Git through practice.\n' > README.md
cat README.md
ls -l
```

`printf` writes the text, while `>` redirects that output into a file. Be careful: `>` replaces an existing file's contents.

`cat` displays the file, and `ls -l` lists directory contents with details such as permissions, owner, and size.

To add another line without replacing the file:

```bash
printf '\nFirst topic: Linux and Git fundamentals.\n' >> README.md
cat README.md
```

The difference between `>` and `>>` is small to type but important to understand: one replaces content; the other appends it.

## 3. Start tracking the project with Git

Git records versions of a project's tracked files. GitHub hosts repositories remotely so they can be shared and used for collaboration.

From inside the practice directory:

```bash
git init
git status
```

`git init` creates a Git repository in the directory. It does not upload anything to GitHub.

`git status` shows the repository's current state. At this point, a new README will normally appear as an untracked file.

Before creating your first commit, configure your commit identity if you have not already done so:

```bash
git config user.name "Your Name"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
```

Replace those values with your own details. You can use the no-reply address provided in your GitHub email settings.

These commands set the identity for this repository. They do not sign you in to GitHub.

## 4. Understand staging and committing

This was one of the most useful distinctions for me.

A file can exist in my project without being included in the next commit. Staging lets me choose which changes to record.

```bash
git add README.md
git diff --staged
git commit -m "Add initial DevOps lab notes"
git status
```

The sequence matters:

1. `git add README.md` stages the file's current contents.
2. `git diff --staged` lets me review what the next commit will contain.
3. `git commit` records the staged changes in the local repository.
4. `git status` shows whether any changes remain.

If I edit the file again after staging it, I need to stage the new changes too if I want them in that commit.

A commit message should explain the change. “Add initial DevOps lab notes” tells me more than “update.”

## 5. Connect the local repository to GitHub

For this practice workflow, first create an **empty GitHub repository**, without adding a README, license, or .gitignore through GitHub. That keeps the initial push straightforward.

Then replace the placeholder URL below with your repository URL:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git remote -v
git push -u origin main
```

Here is what these commands mean:

| Command | Purpose |
| --- | --- |
| `git branch -M main` | Rename the current branch to `main` |
| `git remote add origin ...` | Store the remote repository URL under the name `origin` |
| `git remote -v` | Show the configured remote URLs |
| `git push -u origin main` | Push the branch and set its upstream tracking relationship |

Authentication must be configured separately. Use a supported GitHub authentication method, such as an HTTPS credential manager or SSH. Never put tokens or private keys in your project files.

If `origin` already exists, inspect it with `git remote -v` before changing anything. If the remote repository already contains commits, its history may need to be integrated before you can push.

## 6. The difference between commit and push

My simplest explanation is:

> A commit records staged changes locally. A push sends local commits to a remote repository.

That means a successful commit does not automatically update GitHub.

For another practice change:

```bash
printf '\nKey lesson: commit is local; push updates the remote.\n' >> README.md
git diff
git add README.md
git diff --staged
git commit -m "Document the difference between commit and push"
git push
```

After the upstream is configured, `git push` can usually use that tracking relationship without repeating the remote and branch names.

The workflow is:

**Edit → Review → Stage → Review staged changes → Commit → Push**

## 7. Verify the result

A command finishing without an obvious error is a starting point. I also want to check the result.

```bash
git status
git log --oneline -5
git remote -v
```

These checks answer different questions:

- **Status:** Do I have uncommitted changes?
- **Log:** Which commits exist locally?
- **Remote:** Which repository am I connected to?

Finally, open the repository on GitHub and check that the expected file and latest commit appear.

A clean working tree means there are no outstanding changes relative to the current commit. By itself, it does not prove that every commit has been pushed.

## What this lab is teaching me

The biggest lesson is to connect every action with its purpose.

Before running a command, I try to answer:

- Where am I running it?
- What will it change?
- How will I verify the result?
- What does the output tell me?

I also want to build good habits early: review changes before committing, write useful commit messages, and keep credentials out of version control.

A README is a useful place to record the lab's purpose, commands, results, and lessons. That makes it easier to return later and explain what I actually learned.

## What comes next

My next goal is to build on this foundation with a small application, then gradually introduce a web server, scripting, containers, and a CI/CD pipeline.

For this stage, the milestone is clear: work confidently in a Linux directory, inspect a file change, record it with Git, and understand how that commit reaches GitHub.

I am documenting the process as I learn, one practical step at a time.
