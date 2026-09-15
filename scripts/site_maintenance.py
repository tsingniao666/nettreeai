#!/usr/bin/env python3
"""Generate sitemap, render changelog, verify directory links, and weekly freshness updates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
CSV_PATH = ROOT / "lists" / "starter-directories.csv"
CHANGELOG_PATH = DATA / "changelog.json"
CONFIG_PATH = Path(__file__).resolve().parent / "site_config.json"

PAGE_PRIORITIES = {
    "index.html": 1.0,
    "saas-directories.html": 0.9,
    "starter-directories.html": 0.85,
    "submitted-vs-live.html": 0.85,
    "free-backlink-evidence-log.html": 0.85,
    "saas-launch-checklist.html": 0.8,
    "github-pages-backlink-guide.html": 0.8,
    "changelog.html": 0.75,
    "zh/index.html": 0.7,
    "zh/saas-directories.html": 0.65,
}


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def today_iso() -> str:
    return date.today().isoformat()


def discover_html_pages() -> list[Path]:
    pages = sorted(DOCS.rglob("*.html"))
    return [page for page in pages if page.name != "404.html"]


def page_url(base_url: str, page: Path) -> str:
    rel = page.relative_to(DOCS).as_posix()
    if rel == "index.html":
        return f"{base_url.rstrip('/')}/"
    if rel == "zh/index.html":
        return f"{base_url.rstrip('/')}/zh/"
    return f"{base_url.rstrip('/')}/{rel}"


def generate_sitemap(base_url: str | None = None) -> Path:
    config = load_config()
    base = (base_url or config["base_url"]).rstrip("/")
    today = today_iso()

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for page in discover_html_pages():
        rel = page.relative_to(DOCS).as_posix()
        priority = PAGE_PRIORITIES.get(rel, 0.6)
        loc = page_url(base, page)
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{today}</lastmod>",
                "    <changefreq>weekly</changefreq>",
                f"    <priority>{priority:.2f}</priority>",
                "  </url>",
            ]
        )

    lines.append("</urlset>")
    sitemap_path = DOCS / "sitemap.xml"
    sitemap_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return sitemap_path


def load_changelog() -> list[dict]:
    if not CHANGELOG_PATH.exists():
        return []
    with CHANGELOG_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_changelog(entries: list[dict]) -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    with CHANGELOG_PATH.open("w", encoding="utf-8") as handle:
        json.dump(entries, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def render_changelog_html() -> Path:
    config = load_config()
    base = config["base_url"].rstrip("/")
    entries = load_changelog()

    body_entries = []
    for entry in entries:
        items = "".join(f"<li>{item}</li>" for item in entry["items"])
        body_entries.append(
            f'        <article class="changelog-entry">\n'
            f'          <time datetime="{entry["date"]}">{entry["date"]}</time>\n'
            f"          <ul>{items}</ul>\n"
            f"        </article>"
        )

    latest = entries[0]["date"] if entries else today_iso()
    html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Changelog | NetTree Open Resources</title>
    <meta name="description" content="Updates to NetTree open resources: directory reviews, new guides, verification checks, and GitHub Pages improvements." />
    <link rel="canonical" href="{base}/changelog.html" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Changelog | NetTree Open Resources" />
    <meta property="og:description" content="See what changed in the NetTree open backlink resource hub." />
    <meta property="og:url" content="{base}/changelog.html" />
    <meta property="og:image" content="{config["og_image"]}" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,550;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="./assets/site.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="wrap brand-row">
        <a class="logo" href="./">NetTree</a>
        <nav class="nav" aria-label="Primary">
          <a href="./">Home</a>
          <a href="./saas-directories.html">SaaS directories</a>
          <a href="./submitted-vs-live.html">Submitted vs Live</a>
          <a href="./free-backlink-evidence-log.html">Evidence log</a>
          <a href="./changelog.html" aria-current="page">Changelog</a>
          <a href="{config["product_url"]}">Product</a>
          <a href="{config["github_repo"]}">GitHub</a>
        </nav>
      </div>
    </header>
    <main>
      <section class="hero hero-compact">
        <div class="wrap">
          <p class="eyebrow">Maintained in the open</p>
          <h1 class="wide">Changelog</h1>
          <p class="lede">A public record of updates to NetTree open resources—directory reviews, new guides, verification checks, and GitHub Pages improvements.</p>
          <p class="updated-badge">Last updated: {latest}</p>
        </div>
      </section>
      <section>
        <div class="wrap changelog-list">
{chr(10).join(body_entries)}
        </div>
      </section>
    </main>
    <footer class="site-footer">
      <div class="wrap">
        <p>Product home: <a href="{config["product_url"]}">{config["product_url"]}</a> · Source: <a href="{config["github_repo"]}">{config["github_repo"].replace("https://", "")}</a></p>
      </div>
    </footer>
  </body>
</html>
"""
    output = DOCS / "changelog.html"
    output.write_text(html, encoding="utf-8")
    return output


def check_url(url: str, timeout: float = 12.0) -> str:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "NetTreeLinkChecker/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            code = response.getcode()
            if code and code < 400:
                return "ok"
            return f"http_{code}"
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405}:
            return check_url_get(url, timeout)
        return f"http_{exc.code}"
    except Exception:
        return check_url_get(url, timeout)


def check_url_get(url: str, timeout: float = 12.0) -> str:
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": "NetTreeLinkChecker/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            code = response.getcode()
            return "ok" if code and code < 400 else f"http_{code}"
    except urllib.error.HTTPError as exc:
        return f"http_{exc.code}"
    except Exception:
        return "error"


def read_csv_rows() -> tuple[list[str], list[dict[str, str]]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    return fieldnames, rows


def write_csv_rows(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def check_directory_links(limit: int | None = None) -> dict:
    fieldnames, rows = read_csv_rows()
    for column in ("last_verified", "link_status"):
        if column not in fieldnames:
            fieldnames.append(column)

    checked = 0
    ok_count = 0
    issues: list[str] = []
    today = today_iso()

    target_rows = rows[:limit] if limit else rows
    for row in target_rows:
        homepage = row.get("homepage_url", "").strip()
        submission = row.get("submission_url", "").strip()
        statuses = []
        for url in {homepage, submission}:
            if not url:
                continue
            status = check_url(url)
            statuses.append(status)
            checked += 1
            if status == "ok":
                ok_count += 1
            else:
                issues.append(f"{row.get('name', 'unknown')}: {url} -> {status}")

        row["last_verified"] = today
        row["link_status"] = "ok" if statuses and all(s == "ok" for s in statuses) else "needs_review"

    write_csv_rows(fieldnames, rows)
    return {"checked_urls": checked, "ok": ok_count, "issues": issues, "rows": len(target_rows)}


def weekly_freshness(dry_run: bool = False) -> dict:
    generate_sitemap()
    render_changelog_html()

    link_summary = check_directory_links(limit=3)
    today = today_iso()
    entries = load_changelog()

    summary_items = [
        f"Regenerated sitemap.xml with lastmod {today}.",
        f"Verified {link_summary['rows']} directory entries ({link_summary['ok']}/{link_summary['checked_urls']} URLs responded cleanly).",
    ]
    if link_summary["issues"]:
        summary_items.append(
            "Flagged destinations for review: " + ", ".join(issue.split(":")[0] for issue in link_summary["issues"][:3])
        )

    if entries and entries[0].get("date") == today:
        entries[0]["items"] = summary_items + [item for item in entries[0]["items"] if item not in summary_items]
    else:
        entries.insert(0, {"date": today, "items": summary_items})

    if not dry_run:
        save_changelog(entries)
        render_changelog_html()
        generate_sitemap()

    return {"date": today, "items": summary_items, "link_summary": link_summary}


def ping_search_engines(base_url: str) -> None:
    sitemap = urljoin(base_url.rstrip("/") + "/", "sitemap.xml")
    endpoints = [
        f"https://www.google.com/ping?sitemap={sitemap}",
        f"https://www.bing.com/ping?sitemap={sitemap}",
    ]
    for endpoint in endpoints:
        try:
            with urllib.request.urlopen(endpoint, timeout=10) as response:
                print(f"Ping {endpoint}: {response.getcode()}")
        except Exception as exc:
            print(f"Ping failed for {endpoint}: {exc}", file=sys.stderr)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="NetTree site maintenance utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    sitemap_cmd = sub.add_parser("generate-sitemap", help="Generate docs/sitemap.xml")
    sitemap_cmd.add_argument("--base-url")

    sub.add_parser("render-changelog", help="Render docs/changelog.html from data/changelog.json")

    links_cmd = sub.add_parser("check-links", help="Verify starter directory URLs")
    links_cmd.add_argument("--limit", type=int)

    fresh_cmd = sub.add_parser("weekly-freshness", help="Weekly freshness update")
    fresh_cmd.add_argument("--dry-run", action="store_true")

    ping_cmd = sub.add_parser("ping-search-engines", help="Ping Google and Bing with sitemap URL")
    ping_cmd.add_argument("--base-url")

    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "generate-sitemap":
        path = generate_sitemap(args.base_url)
        print(f"Wrote {path}")
    elif args.command == "render-changelog":
        path = render_changelog_html()
        print(f"Wrote {path}")
    elif args.command == "check-links":
        summary = check_directory_links(limit=args.limit)
        print(json.dumps(summary, indent=2))
    elif args.command == "weekly-freshness":
        summary = weekly_freshness(dry_run=args.dry_run)
        print(json.dumps(summary, indent=2))
    elif args.command == "ping-search-engines":
        config = load_config()
        ping_search_engines(args.base_url or config["base_url"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
