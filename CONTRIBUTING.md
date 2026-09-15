# Suggest a destination

Thanks for helping keep this preview set small and useful.

## Before opening a PR

1. Read [lists/inclusion-criteria.md](./lists/inclusion-criteria.md).
2. Confirm the destination is not already in [lists/starter-directories.md](./lists/starter-directories.md) (same root domain).
3. Prefer **one high-quality addition** over a dump of twenty URLs.

## What to include in the PR

- Homepage URL and (if different) submission / pitch URL
- Category (launch, directory, reviews, ai_directory, company_profile, china_discovery, …)
- Languages and regions you can defend
- Pricing note (`free`, `free_entry`, `free_tier`, or paid with a short label)
- 1–2 sentences on **why it belongs** (audience fit, standards, verifiability)
- Update **both** `lists/starter-directories.md` and `lists/starter-directories.csv`
- Set `last_verified` to the PR date and `link_status` to `ok` or `needs_review` after checking URLs
- Regenerate Pages artifacts if you change public-facing content:
  `python3 scripts/site_maintenance.py generate-sitemap && python3 scripts/site_maintenance.py render-changelog`

## What we will reject

- Spam farms, sold-link networks, or “guaranteed dofollow” pitches
- Broken domains
- Uncritical bulk lists without notes
- Changes that only exist to place a promotional backlink with no editorial value

## Product feedback

For NetTree product bugs or feature requests, use the site at [nettree.ai](https://nettree.ai) rather than this list repo when possible.
