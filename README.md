# AI Prompts MCP Server

A Model Context Protocol (MCP) server that provides access to curated AI prompts for various development tasks including PRD creation, task generation, and documentation creation.

## Overview

This MCP server exposes a collection of structured AI prompts that can be used by Claude and other AI assistants

## Installation

### Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

1. **Install uv (if not already installed):**

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd ai-prompts
   ```

3. **Install dependencies using uv:**

   ```bash
   uv sync
   ```

## Usage

### Running the Server

The MCP server can be run using uv:

```bash
uv run run ai-prompts
```

### Development Mode

For development and testing, you can run the server with MCP inspector for debugging:

```bash
# Run MCP Dev
mcp dev ./src/server.py
```

This will start the MCP inspector web interface at `http://localhost:6274` where you can:

- Test server capabilities interactively
- Browse available resources and tools
- Debug MCP protocol messages
- Validate server responses

### Configuring with Claude Desktop

Add the following configuration to your Claude Desktop config file:

**For macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "ai-prompts": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/ai-prompts",
      "env": {}
    }
  }
}
```

Replace `/path/to/ai-prompts` with the actual path to your project directory.

**Alternative configuration using the direct download from Github:**

```json
{
  "mcpServers": {
    "ai-prompts": {
      "command": "uvx",
      "args": [
        "--from",
        "git+http://github.com/giusmento/ai-prompts.git",
        "ai-prompts"
      ],
      "env": {}
    }
  }
}
```

**Claude code**

```bash
claude mcp add ai-prompts -- uvx --from git+http://github.com/giusmento/ai-prompts.git ai-prompts
```
