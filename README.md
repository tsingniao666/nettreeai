# NetTree

**Turn one URL into a backlink strategy your team can defend.**

[![Website](https://img.shields.io/badge/website-nettree.ai-0B3D2E?style=flat)](https://nettree.ai)
[![Open docs](https://img.shields.io/badge/open%20docs-GitHub%20Pages-2F6F4E?style=flat)](https://tsingniao666.github.io/nettreeai/)
[![Last updated](https://img.shields.io/badge/updated-2026--09--15-2F6F4E?style=flat)](./docs/changelog.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](./LICENSE)
[![Starter list](https://img.shields.io/badge/starter%20directories-20-2F6F4E)](./lists/starter-directories.md)
[![SaaS directories](https://img.shields.io/badge/awesome%20SaaS%20directories-reviewed-2F6F4E)](./lists/saas-directories.md)
[![Free template](https://img.shields.io/badge/free%20resource-backlink%20evidence%20log-2F6F4E)](./resources/backlink-evidence-log.csv)

**Product:** [https://nettree.ai](https://nettree.ai)  
**Open docs (GitHub Pages):** [https://tsingniao666.github.io/nettreeai/](https://tsingniao666.github.io/nettreeai/)

NetTree reads a public website, builds a living profile, and matches it to evidence-backed backlink opportunities—so your team knows **what to pursue**, **why it fits**, and **what to review** before acting.

This GitHub repository is the **public presence** for NetTree: product orientation, methodology notes, and a **limited starter directory sample**. It is not a dump of every submission site on the internet, and it is not a license to spam.

If this open resource hub saves your team time, **star the repo** or **fork the CSV templates**—it helps others discover honest backlink documentation.

---

## Open resource hub (SEO-friendly web versions)

Markdown sources live in this repo; browser-friendly Pages versions are maintained for search indexing and citation:

| Resource | Web page | Source |
|----------|----------|--------|
| Hub home | [Pages home](https://tsingniao666.github.io/nettreeai/) | [docs/index.html](./docs/index.html) |
| SaaS directories shortlist | [saas-directories.html](https://tsingniao666.github.io/nettreeai/saas-directories.html) | [lists/saas-directories.md](./lists/saas-directories.md) |
| Starter directories (20 rows) | [starter-directories.html](https://tsingniao666.github.io/nettreeai/starter-directories.html) | [lists/starter-directories.md](./lists/starter-directories.md) |
| Submitted vs Live | [submitted-vs-live.html](https://tsingniao666.github.io/nettreeai/submitted-vs-live.html) | [methodology/submitted-vs-live.md](./methodology/submitted-vs-live.md) |
| SaaS launch checklist | [saas-launch-checklist.html](https://tsingniao666.github.io/nettreeai/saas-launch-checklist.html) | [resources/saas-launch-submission-checklist.md](./resources/saas-launch-submission-checklist.md) |
| GitHub Pages backlink guide | [github-pages-backlink-guide.html](https://tsingniao666.github.io/nettreeai/github-pages-backlink-guide.html) | — |
| Free evidence log | [free-backlink-evidence-log.html](https://tsingniao666.github.io/nettreeai/free-backlink-evidence-log.html) | [resources/backlink-evidence-log.md](./resources/backlink-evidence-log.md) |
| Changelog | [changelog.html](https://tsingniao666.github.io/nettreeai/changelog.html) | [data/changelog.json](./data/changelog.json) |
| 中文 mirror | [zh/](https://tsingniao666.github.io/nettreeai/zh/) | [docs/zh/](./docs/zh/) |

---

## Why this exists

1. **Open presence** — a clear, crawlable description of what NetTree is (and is not).
2. **Website entry** — every meaningful surface points to [nettree.ai](https://nettree.ai).
3. **Discoverable sample data** — a curated Markdown + CSV preview others can read, fork, or cite—with inclusion criteria so it stays honest.
4. **Maintained freshness** — scheduled link rechecks, changelog entries, and sitemap updates signal ongoing maintenance.

The full matching library, site profiles, drafts, and verification workflow live in the product—not in this repo.

---

## What NetTree does

| Step | Outcome |
|------|---------|
| **Understand** | Start from a URL. Infer positioning, language, markets, audiences, and search language—you review before it drives recommendations. |
| **Match** | Rank destinations by topic, language, region, source type, and available evidence—not one generic spreadsheet for everyone. |
| **Explain** | See fit rationale, gaps, and risk before an opportunity enters a queue. No data → no invented confidence. |
| **Prove** | AI helps prepare drafts; humans keep accounts and the final click. **Submitted** is activity; **Live** is a verified result. |

Deep dives in this repo:

- [Human in the loop](./methodology/human-in-the-loop.md)
- [Submitted vs Live](./methodology/submitted-vs-live.md)

---

## Starter directories (public preview)

A maintained sample of **20** launch platforms, software directories, review catalogs, AI directories, and Chinese-language discovery surfaces:

- [lists/starter-directories.md](./lists/starter-directories.md) — human-readable tables + notes
- [lists/starter-directories.csv](./lists/starter-directories.csv) — same rows for spreadsheets / scripts (`last_verified`, `link_status`)
- [lists/inclusion-criteria.md](./lists/inclusion-criteria.md) — what belongs (and what does not)

Use the sample as a **starting lens**, not as “submit to all.” Prefer fit, then verify whether a listing actually went live.

Searching for SaaS launch sites or AI tool directories? Start with the decision-oriented [Awesome SaaS directories shortlist](./lists/saas-directories.md), then use the full 20-row preview when you need the underlying fields.

---

## Quick start (product)

1. Open [https://nettree.ai](https://nettree.ai)
2. Map your site from a public URL
3. Review the inferred profile
4. Inspect matched opportunities and evidence
5. Keep human judgment on submission; verify outcomes

Free plan includes a limited public-library preview. Registration unlocks deeper fit evidence, saved work, and workflows. NetTree does **not** auto-submit on your behalf.

---

## Free backlink evidence log

Fork or download a small, portable template for separating a published link from a verified one:

- [Backlink Evidence Log (CSV)](./resources/backlink-evidence-log.csv) — ready to duplicate in a spreadsheet.
- [Field guide and responsible GitHub example](./resources/backlink-evidence-log.md) — what to record, how to verify it, and how to document an owned repository or GitHub Pages asset without spam.
- [Read it on GitHub Pages](https://tsingniao666.github.io/nettreeai/free-backlink-evidence-log.html) — browser-friendly overview and download link.
- [SaaS launch submission checklist](./resources/saas-launch-submission-checklist.md) — a forkable preflight for launch platforms, directories, and owned GitHub assets.

The template is deliberately useful without an account. If it saves your team time, fork it, adapt it, and share improvements that make the evidence trail clearer for everyone.

---

## Repository layout

```text
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── data/
│   └── changelog.json              # Changelog source for Pages
├── docs/                           # GitHub Pages site
│   ├── index.html
│   ├── saas-directories.html
│   ├── starter-directories.html
│   ├── submitted-vs-live.html
│   ├── saas-launch-checklist.html
│   ├── github-pages-backlink-guide.html
│   ├── free-backlink-evidence-log.html
│   ├── changelog.html              # Generated from data/changelog.json
│   ├── sitemap.xml                 # Generated on deploy
│   ├── robots.txt
│   ├── assets/
│   └── zh/
├── scripts/
│   ├── site_maintenance.py
│   └── site_config.json
├── lists/
│   ├── inclusion-criteria.md
│   ├── saas-directories.md
│   ├── starter-directories.md
│   └── starter-directories.csv
├── resources/
│   ├── backlink-evidence-log.csv
│   ├── backlink-evidence-log.md
│   └── saas-launch-submission-checklist.md
└── methodology/
    ├── human-in-the-loop.md
    └── submitted-vs-live.md
```

---

## SEO & maintenance setup

After pushing, complete these one-time steps:

1. **GitHub Pages** — Settings → Pages → source: GitHub Actions (already configured). Primary public URL: `https://tsingniao666.github.io/nettreeai/` (keeps cross-domain links from `github.io` to `nettree.ai`).
2. **Google Search Console** — Verify `tsingniao666.github.io/nettreeai` and submit `sitemap.xml`.
3. **Bing Webmaster Tools** — Import from Search Console or verify separately.
4. **Repository About** — Set Website to `https://nettree.ai` and Topics: `backlinks`, `seo`, `saas`, `link-building`, `growth`.
5. **Enable Discussions** — Use the Q&A template in [`.github/DISCUSSION_TEMPLATE/`](./.github/DISCUSSION_TEMPLATE/).

Automated maintenance:

- **Weekly** — [freshness workflow](./.github/workflows/freshness.yml) updates sitemap, changelog, and spot-checks directory links.
- **Bi-weekly** — [directory link check](./.github/workflows/directory-link-check.yml) verifies all starter URLs.
- **Releases** — Tag `vYYYY.MM.DD` to publish CSV assets via [release workflow](./.github/workflows/release-template.yml).

Local commands:

```bash
python3 scripts/site_maintenance.py generate-sitemap
python3 scripts/site_maintenance.py render-changelog
python3 scripts/site_maintenance.py check-links
```

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). We welcome careful, criteria-aligned additions to the starter list—not bulk URL dumps.

---

## 中文简介

NetTree（[nettree.ai](https://nettree.ai)）把公开网站变成可辩护的外链计划：先建站点画像，再按证据匹配目的地，人工确认后再执行，并把 **已提交** 与 **已上线（可验证）** 分开。

本仓库用于项目公开露出、官网入口，以及一份**有限且带收录标准**的 starter 目录样本（Markdown + CSV）。完整情报库与工作流在产品内，不在此开源业务代码仓库中。

- 中文 Pages：[docs/zh/](https://tsingniao666.github.io/nettreeai/zh/)
- 样本列表：[lists/starter-directories.md](./lists/starter-directories.md)
- 收录标准：[lists/inclusion-criteria.md](./lists/inclusion-criteria.md)
- 方法说明：[methodology/](./methodology/)
- 免费验链记录模板：[resources/backlink-evidence-log.csv](./resources/backlink-evidence-log.csv)
- SaaS 目录短名单：[lists/saas-directories.md](./lists/saas-directories.md)

---

## Disclaimer

Listings, backlinks, and search rankings are decided by third-party sites and search engines. NetTree and this repository improve decision quality and documentation; they do not guarantee outcomes. Links in third-party pages may use `nofollow` / `ugc` / other attributes.

---

## License

[MIT](./LICENSE) — documentation and curated list files in this repository.
