# NetTree public MCP — directory listing guide

Remote endpoint: `https://nettree.ai/api/mcp` (Streamable HTTP)  
Docs: [nettree.ai/mcp](https://nettree.ai/mcp) · [GitHub Pages mirror](../docs/mcp-server.html)  
API keys: NetTree account → **Settings → Account → MCP API key** (active users only)

This repo (`tsingniao666/nettreeai`) holds **`server.json`** for the official MCP Registry. Application code stays private.

## What you can automate vs what needs a human

| Directory | How | Agent can finish? |
| --- | --- | --- |
| [Official MCP Registry](https://registry.modelcontextprotocol.io/) | `mcp-publisher publish` from this repo (GitHub login as `tsingniao666`) | **No** — device login |
| [PulseMCP](https://www.pulsemcp.com/) | Ingests official Registry (submissions often paused) | After Registry publish |
| [Glama](https://glama.ai/) | Add / claim MCP server; links GitHub + registry | **No** — web account |
| [Smithery](https://smithery.ai/new) | Submit public URL; set **Authorization** header for scan | **No** — web + live scan with your key |
| [mcp.directory](https://mcp.directory/submit) | Form or registry import | **No** — form / wait for import |
| [mcpservers.org](https://mcpservers.org/submit) | Free submit form (Marketing category fits) | **No** — form |
| [awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) | PR adding one row | **No** — needs `gh auth` + PR |
| [mcp.so](https://mcp.so/) | Paid fast-track only (when used) | **No** — payment |

## 1. Official MCP Registry (do this first)

```bash
cd /path/to/nettreeai
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
./mcp-publisher validate
./mcp-publisher login github   # as tsingniao666
./mcp-publisher publish
```

Verify:

```bash
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.tsingniao666/nettree-public"
```

## 2. Smithery (remote URL)

1. Open [smithery.ai/new](https://smithery.ai/new)
2. URL: `https://nettree.ai/api/mcp`
3. Transport: Streamable HTTP
4. Add header `Authorization: Bearer <your MCP API key>` so the scanner can list tools
5. Homepage: `https://nettree.ai/mcp` · GitHub: this repo

## 3. Glama

1. [Glama MCP](https://glama.ai/mcp/servers) → add or claim server
2. Point repository to `https://github.com/tsingniao666/nettreeai`
3. After Registry publish, confirm sync from official metadata

## 4. awesome-remote-mcp-servers (PR)

Add a row (adjust table format to match current README):

```markdown
| [NetTree Public](https://nettree.ai/mcp) | SaaS link-destination catalog (search / suggest) | Streamable HTTP + Bearer API key |
```

## 5. mcpservers.org / mcp.directory

Use product URL `https://nettree.ai/mcp`, endpoint `https://nettree.ai/api/mcp`, category **Marketing** or **SEO**, auth **Bearer token** (user-issued from NetTree account).

## Cursor snippet (for README / docs)

```json
"nettree-public": {
  "url": "https://nettree.ai/api/mcp",
  "headers": {
    "Authorization": "Bearer YOUR_MCP_API_KEY"
  }
}
```

**Important:** the `Bearer ` prefix is required.

## Version bumps

When tools or limits change, bump `version` in `server.json` and run `mcp-publisher publish` again.
