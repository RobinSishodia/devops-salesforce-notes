#!/usr/bin/env python3
"""Sync published posts from a Hashnode blog into this repo as Markdown.

- Pulls every published post via Hashnode's public GraphQL API (no token needed)
- Writes each one to posts/<YYYY-MM-DD>-<slug>.md with YAML front matter
- Regenerates README.md with an index table of all posts

Only uses the Python standard library, so no pip install is required.
"""

import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

HOST = os.environ.get("HASHNODE_HOST", "sishodiarobin.hashnode.dev")
API = "https://gql.hashnode.com/"
ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
README = ROOT / "README.md"

QUERY = """
query Posts($host: String!, $after: String) {
  publication(host: $host) {
    title
    url
    posts(first: 20, after: $after) {
      pageInfo { hasNextPage endCursor }
      edges {
        node {
          title
          slug
          url
          brief
          publishedAt
          updatedAt
          readTimeInMinutes
          tags { name slug }
          coverImage { url }
          content { markdown }
        }
      }
    }
  }
}
"""


HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
}


def gql(variables, attempts=4):
    body = json.dumps({"query": QUERY, "variables": variables}).encode()
    last = None
    for i in range(attempts):
        req = urllib.request.Request(API, data=body, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8", "replace")
                status = resp.status
        except urllib.error.HTTPError as e:
            raw, status = e.read().decode("utf-8", "replace"), e.code
        try:
            data = json.loads(raw)
            if data.get("errors"):
                raise RuntimeError(data["errors"])
            return data["data"]["publication"]
        except json.JSONDecodeError:
            last = f"HTTP {status}, non-JSON response: {raw[:300]!r}"
            print(f"Attempt {i + 1} failed: {last}")
            time.sleep(5 * (i + 1))
    raise RuntimeError(last)


def fetch_all():
    posts, after, pub = [], None, None
    while True:
        pub = gql({"host": HOST, "after": after})
        if pub is None:
            raise RuntimeError(f"Publication not found for host {HOST}")
        conn = pub["posts"]
        posts += [e["node"] for e in conn["edges"]]
        if not conn["pageInfo"]["hasNextPage"]:
            break
        after = conn["pageInfo"]["endCursor"]
    return pub, posts


def yaml_str(value):
    return json.dumps(value or "", ensure_ascii=False)


def write_post(post):
    date = post["publishedAt"][:10]
    path = POSTS_DIR / f"{date}-{post['slug']}.md"
    tags = ", ".join(yaml_str(t["name"]) for t in post.get("tags") or [])
    cover = (post.get("coverImage") or {}).get("url", "")
    front = "\n".join([
        "---",
        f"title: {yaml_str(post['title'])}",
        f"date: {post['publishedAt']}",
        f"updated: {post.get('updatedAt') or post['publishedAt']}",
        f"canonical_url: {post['url']}",
        f"cover_image: {cover}",
        f"tags: [{tags}]",
        f"brief: {yaml_str(post.get('brief'))}",
        "---",
        "",
        f"> Originally published at [{HOST}]({post['url']}). "
        "This is an automated backup; read and comment on the blog.",
        "",
    ])
    body = (post.get("content") or {}).get("markdown", "").strip() + "\n"
    new = front + "\n" + body
    if not path.exists() or path.read_text(encoding="utf-8") != new:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def clean_cell(text):
    return re.sub(r"\s+", " ", text or "").replace("|", "\\|").strip()


def write_readme(pub, posts):
    posts = sorted(posts, key=lambda p: p["publishedAt"], reverse=True)
    rows = []
    for p in posts:
        date = p["publishedAt"][:10]
        tags = " ".join(f"`{t['name']}`" for t in (p.get("tags") or [])[:4])
        md = f"posts/{date}-{p['slug']}.md"
        rows.append(
            f"| {date} | [{clean_cell(p['title'])}]({p['url']}) | {tags} | [Markdown]({md}) |"
        )
    content = f"""# 📝 DevOps & Salesforce Notes

Hands-on articles on **Salesforce Administration**, **AWS**, **DevOps** (Docker, Kubernetes, Terraform, CI/CD) and **cloud security**, written by **Robin Sishodia** while learning in public.

🔗 **Read on the blog:** [{HOST}]({pub.get('url') or 'https://' + HOST})
💼 **LinkedIn:** [linkedin.com/in/robinsishodia](https://www.linkedin.com/in/robinsishodia)

## ⚙️ How this repo works

Posts are written on Hashnode. A scheduled **GitHub Actions** workflow ([`sync-blog.yml`](.github/workflows/sync-blog.yml)) runs daily and:

1. Calls the Hashnode GraphQL API with [`scripts/sync_hashnode.py`](scripts/sync_hashnode.py) (pure Python stdlib)
2. Saves every published post as Markdown in [`posts/`](posts/)
3. Rebuilds this README index and commits only when something changed

## 📚 All posts ({len(posts)})

| Date | Title | Tags | Source |
|------|-------|------|--------|
""" + "\n".join(rows) + """

<sub>This index is generated automatically. Edits here will be overwritten.</sub>
"""
    README.write_text(content, encoding="utf-8")


def main():
    POSTS_DIR.mkdir(exist_ok=True)
    pub, posts = fetch_all()
    changed = sum(write_post(p) for p in posts)
    write_readme(pub, posts)
    print(f"Fetched {len(posts)} posts; {changed} new or updated.")


if __name__ == "__main__":
    main()
