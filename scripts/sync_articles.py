#!/usr/bin/env python3
"""从个人网站的 articles.json 同步 README 里的文章表格（<!-- articles:start/end --> 之间）。"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

SOURCE = "https://nepheloovo.github.io/articles.json"
README = Path(__file__).resolve().parent.parent / "README.md"


def cell(s):
    return s.replace("|", "\\|").replace("\n", " ").strip()


def main():
    req = urllib.request.Request(f"{SOURCE}?t={int(time.time())}", headers={"User-Agent": "nepheloovo-readme-sync"})
    with urllib.request.urlopen(req, timeout=30) as r:
        articles = json.load(r)
    articles.sort(key=lambda a: a["date"], reverse=True)
    rows = ["| 日期 | 文章 | 一句话 |", "| --- | --- | --- |"]
    rows += [f"| {a['date']} | [{cell(a['title'])}]({a['url']}) | {cell(a.get('summary', ''))} |" for a in articles]
    doc = README.read_text(encoding="utf-8")
    doc, hit = re.subn(r"(<!-- articles:start -->\n).*?(\n<!-- articles:end -->)",
                       lambda m: m.group(1) + "\n".join(rows) + m.group(2), doc, flags=re.S)
    if not hit:
        sys.exit("README.md 里没找到 <!-- articles:start --> / <!-- articles:end --> 标记。")
    README.write_text(doc, encoding="utf-8")
    print(f"文章表格：{len(articles)} 篇")


if __name__ == "__main__":
    main()
