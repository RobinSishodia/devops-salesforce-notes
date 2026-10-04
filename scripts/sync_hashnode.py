#!/usr/bin/env python3
"""Sync published posts from a Hashnode blog into this repo as Markdown.

Hashnode's GraphQL API became a paid (Pro) feature in 2026, so this script
uses the blog's free public RSS feed instead:

- Reads <blog>/rss.xml (full post content is in <content:encoded>)
- Converts each post's HTML to Markdown and writes posts/<YYYY-MM-DD>-<slug>.md
- Rebuilds README.md from every file in posts/, so older posts that drop
  out of the feed are kept

Dependency: markdownify (installed by the workflow).
"""

import json
import os
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

from markdownify import markdownify as html_to_md

HOST = os.environ.get("HASHNODE_HOST", "sishodiarobin.hashnode.dev")
FEED = f"https://{HOST}/rss.xml"
ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
README = ROOT / "README.md"
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}
HEADERS = {
    "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
}


def fetch(url, attempts=4):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8", "replace")
            if raw.lstrip().startswith("<?xml") or "<rss" in raw[:500]:
                return raw
            last = f"Not an RSS feed: {raw[:200]!r}"
        except urllib.error.URLError as e:
            last = str(e)
        print(f"Attempt {i + 1} failed: {last}")
        time.sleep(5 * (i + 1))
    raise RuntimeError(last)


def text(item, tag):
    el = item.find(tag, NS)
    return (el.text or "").strip() if el is not None else ""


def parse_feed(xml):
    root = ET.fromstring(xml)
    posts = []
    for item in root.iter("item"):
        url = text(item, "link")
        published = parsedate_to_datetime(text(item, "pubDate"))
        enclosure = item.find("enclosure")
        tags = []
        for c in item.findall("category"):
            # old posts stored all hashtags in one category; split them
            for t in re.split(r"[#,]", c.text or ""):
                t = re.sub(r"[^\w\s.+-]", "", t).strip()
                if t and t.lower() not in (x.lower() for x in tags):
                    tags.append(t)
        posts.append({
            "title": text(item, "title"),
            "url": url,
            "slug": url.rstrip("/").rsplit("/", 1)[-1],
            "date": published.strftime("%Y-%m-%d"),
            "published": published.isoformat(),
            "brief": re.sub(r"\s+", " ", text(item, "description")),
            "tags": tags,
            "cover": enclosure.get("url", "") if enclosure is not None else "",
            "html": text(item, "content:encoded"),
        })
    return posts


def q(value):
    return json.dumps(value or "", ensure_ascii=False)


def code_language(pre):
    code = pre.find("code")
    for cls in (code.get("class") or []) if code else []:
        m = re.match(r"lang(?:uage)?-(\w+)", cls)
        if m and m.group(1) != "plaintext":
            return m.group(1)
    return ""


def write_post(p):
    path = POSTS_DIR / f"{p['date']}-{p['slug']}.md"
    body = html_to_md(
        p["html"], heading_style="ATX", bullets="-",
        code_language_callback=code_language,
    ).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    content = "\n".join([
        "---",
        f"title: {q(p['title'])}",
        f"date: {p['published']}",
        f"canonical_url: {p['url']}",
        f"cover_image: {p['cover']}",
        f"tags: [{', '.join(q(t) for t in p['tags'])}]",
        f"brief: {q(p['brief'])}",
        "---",
        "",
        f"> Originally published at [{HOST}]({p['url']}). "
        "This is an automated backup; read and comment on the blog.",
        "",
        body,
        "",
    ])
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def read_front_matter(path):
    meta = {}
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[0] == "---":
        for line in lines[1:]:
            if line == "---":
                break
            key, _, val = line.partition(": ")
            meta[key] = val
    return meta


def cell(s):
    return re.sub(r"\s+", " ", s or "").replace("|", "\\|").strip()


def write_readme():
    entries = []
    for f in sorted(POSTS_DIR.glob("*.md"), reverse=True):
        m = read_front_matter(f)
        title = json.loads(m.get("title", '""'))
        tags = json.loads(m.get("tags", "[]") or "[]")
        tag_str = " ".join(f"`{t}`" for t in tags[:4])
        entries.append(
            f"| {f.name[:10]} | [{cell(title)}]({m.get('canonical_url', '')}) "
            f"| {tag_str} | [Markdown](posts/{f.name}) |"
        )
    content = f"""# 📝 DevOps & Salesforce Notes

Hands-on articles on **Salesforce Administration**, **AWS**, **DevOps** (Docker, Kubernetes, Terraform, CI/CD) and **cloud security**, written by **Robin Sishodia** while learning in public.

🔗 **Read on the blog:** [{HOST}](https://{HOST})
💼 **LinkedIn:** [linkedin.com/in/robinsishodia](https://www.linkedin.com/in/robinsishodia)

## ⚙️ How this repo works

Posts are written on Hashnode. A scheduled **GitHub Actions** workflow ([`sync-blog.yml`](.github/workflows/sync-blog.yml)) runs daily and:

1. Reads the blog's RSS feed with [`scripts/sync_hashnode.py`](scripts/sync_hashnode.py)
2. Converts each post from HTML to Markdown and saves it in [`posts/`](posts/)
3. Rebuilds this README index and commits only when something changed

## 📚 All posts ({len(entries)})

| Date | Title | Tags | Source |
|------|-------|------|--------|
""" + "\n".join(entries) + """

<sub>This index is generated automatically. Edits here will be overwritten.</sub>
"""
    README.write_text(content, encoding="utf-8")


def main():
    POSTS_DIR.mkdir(exist_ok=True)
    posts = parse_feed(fetch(FEED))
    changed = sum(write_post(p) for p in posts)
    write_readme()
    print(f"Feed had {len(posts)} posts; {changed} new or updated.")


if __name__ == "__main__":
    main()
