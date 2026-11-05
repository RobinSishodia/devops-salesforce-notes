#!/usr/bin/env python3
"""Sync published posts from a Hashnode blog into this repo as Markdown.

Hashnode's GraphQL API became a paid (Pro) feature in 2026, so this script
uses the blog's free public RSS feed instead:

- Reads the feed from FEED_FILE (a committed copy of <blog>/rss.xml) or,
  if that isn't set, downloads it (full post content is in <content:encoded>)
- Converts each post's HTML to Markdown and writes
  posts/<category>/<NN>-<YYYY-MM-DD>-<slug>.md, where <category> is
  salesforce, devops or other and NN is the post's serial number within
  its category (oldest = 01)
- Rebuilds README.md from every file under posts/, so older posts that drop
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
# Posts that existed on the blog before the oldest post kept in this repo
# (they were never in the feed, so only the numbering has to account for them)
OLDER_NOT_IN_REPO = {"devops": 14}
CATEGORIES = {
    "salesforce": ("Salesforce Admin 30-Day Series", "Salesforce"),
    "devops": ("DevOps & AWS Learning Notes", "DevOps & AWS"),
    "salesforce-120": ("120 Days of Salesforce", "Salesforce 120"),
}
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


def classify(title):
    if re.search(r"Day \d+/120", title) and "120DaysOfAWS" not in title:
        return "salesforce-120"
    if re.search(r"From Operations to Salesforce", title, re.I):
        return "other"
    if re.search(r"CI/CD Pipeline with GitHub", title, re.I):
        return "devops"
    if re.search(r"salesforce|lookup vs master", title, re.I):
        return "salesforce"
    return "devops"


def render(p, category, serial):
    body = html_to_md(
        p["html"], heading_style="ATX", bullets="-",
        code_language_callback=code_language,
    ).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    head = [
        "---",
        f"title: {q(p['title'])}",
        f"date: {p['published']}",
        f"canonical_url: {p['url']}",
        f"cover_image: {p['cover']}",
        f"tags: [{', '.join(q(t) for t in p['tags'])}]",
        f"brief: {q(p['brief'])}",
    ]
    if category in CATEGORIES:
        head += [f"series: {q(CATEGORIES[category][0])}", f"serial: {serial}"]
    head += [
        "---",
        "",
        f"> Originally published at [{HOST}]({p['url']}). "
        "This is an automated backup; read and comment on the blog.",
        "",
        body,
        "",
    ]
    return "\n".join(head)


def with_series(text_, category, serial):
    """Add or refresh the series/serial lines in an existing file's front matter."""
    lines = text_.split("\n")
    end = lines.index("---", 1)
    front = [l for l in lines[1:end]
             if not l.startswith("series: ") and not l.startswith("serial: ")]
    if category in CATEGORIES:
        front += [f"series: {q(CATEGORIES[category][0])}", f"serial: {serial}"]
    return "\n".join(["---"] + front + lines[end:])


def post_from_file(path):
    m = read_front_matter(path)
    url = m.get("canonical_url", "")
    return {
        "title": json.loads(m.get("title", '""')),
        "url": url,
        "slug": url.rstrip("/").rsplit("/", 1)[-1],
        "published": m.get("date", ""),
        "date": m.get("date", "")[:10],
        "tags": json.loads(m.get("tags", "[]") or "[]"),
    }


def sync_files(feed_posts):
    """Write every post into posts/<category>/ with its serial number."""
    existing = {}
    for f in POSTS_DIR.rglob("*.md"):
        info = post_from_file(f)
        if info["slug"]:
            existing[info["slug"]] = (f, info)
    fresh = {p["slug"]: p for p in feed_posts}
    items = {}
    for slug, (f, info) in existing.items():
        items[slug] = dict(info)
    for slug, p in fresh.items():
        items[slug] = p
    order = {}
    for cat in list(CATEGORIES) + ["other"]:
        group = sorted(
            (i for i in items.values() if classify(i["title"]) == cat),
            key=lambda i: i["published"],
        )
        base = OLDER_NOT_IN_REPO.get(cat, 0)
        for n, i in enumerate(group, start=base + 1):
            order[i["slug"]] = (cat, n)
    changed = 0
    for slug, i in items.items():
        cat, n = order[slug]
        name = f"{n:02d}-{i['date']}-{slug}.md" if cat in CATEGORIES else f"{i['date']}-{slug}.md"
        target = POSTS_DIR / cat / name
        if slug in fresh:
            content = render(fresh[slug], cat, n)
        else:
            old_path = existing[slug][0]
            content = with_series(old_path.read_text(encoding="utf-8"), cat, n)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            changed += 1
        if slug in existing and existing[slug][0] != target and existing[slug][0].exists():
            existing[slug][0].unlink()
            changed += 1
    return changed


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
    groups = {"salesforce": [], "devops": [], "salesforce-120": [], "other": []}
    for f in sorted(POSTS_DIR.rglob("*.md"), reverse=True):
        m = read_front_matter(f)
        title = json.loads(m.get("title", '""'))
        tags = json.loads(m.get("tags", "[]") or "[]")
        tag_str = " ".join(f"`{t}`" for t in tags[:4])
        cat = f.parent.name
        rel = f.relative_to(ROOT).as_posix()
        serial = m.get("serial", "")
        groups.setdefault(cat, []).append(
            f"| {serial} | {f.name[3:13] if serial else f.name[:10]} "
            f"| [{cell(title)}]({m.get('canonical_url', '')}) "
            f"| {tag_str} | [Markdown]({rel}) |"
        )
    head = "| # | Date | Title | Tags | Source |\n|---|------|-------|------|--------|\n"
    sections = []
    for cat, label in (("salesforce", "Salesforce Admin 30-Day Series"),
                       ("devops", "DevOps & AWS Learning Notes"),
                       ("salesforce-120", "120 Days of Salesforce")):
        sections.append(f"## 📚 {label} ({len(groups[cat])} in this repo)\n\n" + head + "\n".join(groups[cat]))
    if groups["other"]:
        sections.append("## 📚 Other\n\n" + head + "\n".join(groups["other"]))
    total = sum(len(v) for v in groups.values())
    content = f"""# 📝 DevOps & Salesforce Notes

Hands-on articles on **Salesforce Administration**, **AWS**, **DevOps** (Docker, Kubernetes, Terraform, CI/CD) and **cloud security**, written by **Robin Sishodia** while learning in public.

🔗 **Read on the blog:** [{HOST}](https://{HOST})
💼 **LinkedIn:** [linkedin.com/in/robinsishodia](https://www.linkedin.com/in/robinsishodia)

## ⚙️ How this repo works

Posts are written on Hashnode. A **GitHub Actions** workflow ([`sync-blog.yml`](.github/workflows/sync-blog.yml)) runs whenever the feed file is updated and:

1. Converts a committed copy of the blog RSS feed ([`feed/rss.xml`](feed/rss.xml)) with [`scripts/sync_hashnode.py`](scripts/sync_hashnode.py)
2. Turns each post from HTML into Markdown and saves it under [`posts/salesforce/`](posts/salesforce/), [`posts/salesforce-120/`](posts/salesforce-120/) or [`posts/devops/`](posts/devops/), numbered by publish order within each series
3. Rebuilds this README index and commits only when something changed

Total posts in this repo: {total}

""" + "\n\n".join(sections) + """

<sub>This index is generated automatically. Edits here will be overwritten.</sub>
"""
    README.write_text(content, encoding="utf-8")


def main():
    POSTS_DIR.mkdir(exist_ok=True)
    feed_file = os.environ.get("FEED_FILE")
    if feed_file:
        if not Path(feed_file).exists():
            print(f"{feed_file} not found yet; nothing to sync.")
            return
        print(f"Reading feed from {feed_file}")
        xml = Path(feed_file).read_text(encoding="utf-8")
    else:
        xml = fetch(FEED)
    posts = parse_feed(xml)
    changed = sync_files(posts)
    write_readme()
    print(f"Feed had {len(posts)} posts; {changed} new or updated.")


if __name__ == "__main__":
    main()
