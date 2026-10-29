# NetTree public MCP — directory listing guide

Remote endpoint: `https://nettree.ai/api/mcp` (Streamable HTTP)  
Docs: [nettree.ai/mcp](https://nettree.ai/mcp) · [GitHub Pages mirror](../docs/mcp-server.html)  
API keys: NetTree account → **Settings → Account → MCP API key** (active users only)

Registry name: **`io.github.tsingniao666/nettree-public`** (published — [search API](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.tsingniao666/nettree-public))

This repo (`tsingniao666/nettreeai`) holds **`server.json`** for the official MCP Registry. Application code stays private.

---

## Priority checklist (2026)

Do these in order after Registry publish:

| Priority | Directory | Action | Notes |
| --- | --- | --- | --- |
| ✅ Done | [Official MCP Registry](https://registry.modelcontextprotocol.io/) | `mcp-publisher publish` | Source of truth; PulseMCP / others may sync from here |
| **1** | [Glama](https://glama.ai/mcp/servers) | Add or **claim** listing | Link repo `nettreeai`, docs `nettree.ai/mcp`, registry id |
| **2** | [mcpservers.org](https://mcpservers.org/submit) | Free submit form | Category: **Marketing** or **SEO** |
| **3** | [mcp.directory](https://mcp.directory/submit) | Submit or wait for registry import | Same URLs + Bearer auth note |
| **4** | [awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) | GitHub PR | Copy-paste: [pr-awesome-remote-mcp-servers.md](./pr-awesome-remote-mcp-servers.md) |
| **5** | [PulseMCP](https://www.pulsemcp.com/) | Wait / watch for registry sync | Direct submissions have been paused at times |
| Optional | [awesome-mcp-servers](https://github.com/punkpezza/awesome-mcp-servers) | PR if you want broader awesome-list reach | Remote + API Key row in appropriate section |
| Optional | [mcp.so](https://mcp.so/) | Paid fast-track only | Budget + follow-up if listing quality matters |
| Low | Smithery | Optional claim on [smithery.ai](https://www.smithery.ai/future) | **Proxy/hosting shut down Oct 31, 2026** — directory may remain; always use **direct** `https://nettree.ai/api/mcp`, never `*.run.tools` |

---

## Copy-paste listing fields

Use everywhere (forms, PRs, Glama):

| Field | Value |
| --- | --- |
| Name | NetTree Public |
| Endpoint | `https://nettree.ai/api/mcp` |
| Transport | Streamable HTTP |
| Authentication | API Key — header `Authorization: Bearer <MCP API key>` |
| Key source | https://nettree.ai/app/settings/account#mcp (active NetTree accounts) |
| Documentation | https://nettree.ai/mcp |
| Public repo | https://github.com/tsingniao666/nettreeai |
| Registry id | `io.github.tsingniao666/nettree-public` |
| Tools | `search_link_sources`, `get_link_source`, `suggest_link_sources` |

**Important:** the literal `Bearer ` prefix is required in the Authorization header.

---

## Registry maintenance

Bump `version` in [server.json](../server.json) when tools or limits change, then:

```bash
cd /path/to/nettreeai
./mcp-publisher validate
./mcp-publisher publish
```

Initial publish (reference):

```bash
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
./mcp-publisher login github   # as tsingniao666
./mcp-publisher publish
```

---

## Glama (step-by-step)

1. Sign in at [glama.ai/mcp/servers](https://glama.ai/mcp/servers).
2. Add server or claim if auto-indexed from GitHub / Registry.
3. Set homepage `https://nettree.ai/mcp`, repository `https://github.com/tsingniao666/nettreeai`.
4. Confirm remote URL is **`https://nettree.ai/api/mcp`** (not a proxy).
5. Note auth: Bearer API key from NetTree account settings.

---

## mcpservers.org / mcp.directory

- **URL / endpoint:** `https://nettree.ai/api/mcp`
- **Landing page:** `https://nettree.ai/mcp`
- **Category:** Marketing, SEO, or Research (pick closest)
- **Auth:** API Key / Bearer token (user-issued, not a shared public key)

---

## Smithery (deprioritized)

Smithery is [shutting down proxy and managed identity on Oct 31, 2026](https://www.smithery.ai/future); clients must use **vendor official URLs**. NetTree’s official URL is `https://nettree.ai/api/mcp`. You do **not** need Smithery hosting. If the public directory still lists your server, ensure the page shows this direct URL only.

---

## Cursor / Claude Desktop snippet

```json
"nettree-public": {
  "url": "https://nettree.ai/api/mcp",
  "headers": {
    "Authorization": "Bearer YOUR_MCP_API_KEY"
  }
}
```
