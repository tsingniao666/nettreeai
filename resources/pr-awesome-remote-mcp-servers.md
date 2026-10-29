# Pull request: awesome-remote-mcp-servers

Target repo: [jaw9c/awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)

## 1. Fork and branch

```bash
gh repo fork jaw9c/awesome-remote-mcp-servers --clone
cd awesome-remote-mcp-servers
git checkout -b add-nettree-public-mcp
```

## 2. Edit README.md

In **Remote MCP Server List**, insert **one row** in alphabetical order by **Name** — after **Netlify**, before **Notion**:

```markdown
| NetTree | Marketing / SEO | `https://nettree.ai/api/mcp` | API Key | [NetTree](https://nettree.ai) |
```

Full table header (for context):

```markdown
| Name | Category | URL | Authentication | Maintainer |
|------|----------|-------------|----------------|------------|
```

## 3. PR title

```text
Add NetTree public MCP (link-destination catalog)
```

## 4. PR body (paste below)

```markdown
## Summary

Adds [NetTree Public](https://nettree.ai/mcp) — a read-only remote MCP server for searching and suggesting public link destinations (directories and similar surfaces) for SaaS / growth teams.

- **URL:** `https://nettree.ai/api/mcp` (Streamable HTTP)
- **Auth:** API Key via `Authorization: Bearer <token>` (per-user keys from NetTree account settings)
- **Registry:** `io.github.tsingniao666/nettree-public` on the [official MCP Registry](https://registry.modelcontextprotocol.io/)
- **Public metadata repo:** https://github.com/tsingniao666/nettreeai (`server.json`)

Tools: `search_link_sources`, `get_link_source`, `suggest_link_sources`. Submission URLs and full operator data remain in the NetTree workspace, not in this public MCP layer.

## Checklist

- [x] Official domain (`nettree.ai`) matches product
- [x] API Key authentication (no open anonymous catalog abuse)
- [x] Listed on official MCP Registry
- [x] Production endpoint stable
```

## 5. Open PR

```bash
git add README.md
git commit -m "Add NetTree public MCP to remote server list"
git push -u origin add-nettree-public-mcp
gh pr create --title "Add NetTree public MCP (link-destination catalog)" --body-file /path/to/body.md
```

Or paste the PR body from section 4 in the GitHub UI.

## Notes

- Maintainers prefer **official** or **production-ready** servers; NetTree is the vendor-maintained public catalog for [nettree.ai](https://nettree.ai).
- Do **not** list Smithery proxy URLs (`*.run.tools`, `server.smithery.ai`).
