# AI Prompts MCP Server

A Model Context Protocol (MCP) server that provides access to curated AI prompts for various development tasks including PRD creation, task generation, and documentation creation.

## Overview

This MCP server exposes a collection of structured AI prompts that can be used by Claude and other AI assistants to help with:

- **Product Requirements Document (PRD) Creation**: Structured prompts for generating comprehensive PRDs
- **Task List Generation**: Converting PRDs into actionable developer task lists
- **Documentation Creation**: Prompts for creating data dictionaries and other technical documentation

## Available Prompts

### Build-PRD Category

- **Rule: Generating a Product Requirements Document (PRD)**: Guide for creating detailed PRDs based on user requirements
- **Rule: Generating a Task List from a PRD**: Convert PRDs into step-by-step implementation tasks

### Documentation Category

- **Rule: Generating a Data Dictionary**: Create comprehensive data dictionaries for business understanding
- **Rule: Create PPT Webapp**: Structured approach for PowerPoint web application development

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

4. **Make the server executable (optional):**
   ```bash
   chmod +x server.py
   ```

## Usage

### Running the Server

The MCP server can be run using uv:

```bash
uv run python server.py
```

Or directly with Python (if made executable):

```bash
./server.py
```

Or using the installed script:

```bash
uv run ai-prompts-server
```

### Development Mode

For development and testing, you can run the server with MCP inspector for debugging:

```bash
# Install MCP inspector (one-time setup)
npm install -g @modelcontextprotocol/inspector

# Run server in development mode with inspector
npx @modelcontextprotocol/inspector uv run python server.py
```

This will start the MCP inspector web interface at `http://localhost:5173` where you can:

- Test server capabilities interactively
- Browse available resources and tools
- Debug MCP protocol messages
- Validate server responses

### Configuring with Claude Desktop

Add the following configuration to your Claude Desktop config file:

**For macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**For Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

**Alternative configuration using the installed script:**

```json
{
  "mcpServers": {
    "ai-prompts": {
      "command": "uv",
      "args": ["run", "ai-prompts-server"],
      "cwd": "/path/to/ai-prompts",
      "env": {}
    }
  }
}
```

### Configuring with Other MCP Clients

For other MCP-compatible clients, use:

- **Command**: `uv`
- **Args**: `["run", "python", "server.py"]`
- **Working Directory**: Path to the ai-prompts directory

## MCP Capabilities

### Resources

The server provides prompt resources accessible via URIs:

- `prompt://rule_generating_a_product_requirements_document_prd` - PRD creation guide
- `prompt://rule_generating_a_task_list_from_a_prd` - Task list generation guide
- `prompt://rule_generating_a_data_dictionary` - Data dictionary creation guide
- `prompt://rule_create_ppt_webapp` - PPT webapp development guide

### Tools

#### `search_prompts`

Search for prompts by keywords or category.

- **Parameters:**
  - `query` (required): Search terms to match in titles and descriptions
  - `category` (optional): Filter by specific category

#### `get_prompt`

Retrieve a specific prompt by its ID.

- **Parameters:**
  - `prompt_id` (required): The ID of the prompt to retrieve

#### `list_categories`

List all available prompt categories with counts.

- **Parameters:** None

## Example Usage

Once configured with Claude Desktop, you can use these prompts by asking Claude:

- "Use the PRD creation prompt to help me build requirements for a user authentication system"
- "Search for prompts related to documentation"
- "Get the task generation prompt and help me break down this PRD"
- "Show me all available prompt categories"

## Prompt Structure

Each prompt file includes:

1. **Frontmatter** (optional): YAML metadata including description and configuration
2. **Goal**: Clear objective of the prompt
3. **Process**: Step-by-step instructions
4. **Structure**: Expected output format
5. **Target Audience**: Intended users (typically developers)
6. **Examples**: Clarifying questions and sample outputs

## Development

### Adding New Prompts

1. Create a new `.md` file in the appropriate category directory
2. Include frontmatter if needed:
   ```yaml
   ---
   description: Brief description of the prompt
   globs:
   alwaysApply: false
   ---
   ```
3. Follow the established prompt structure
4. Restart the MCP server to load new prompts

### File Organization

```
ai-prompts/
├── build-prd/           # PRD and task-related prompts
├── documentation/       # Documentation creation prompts
├── server.py           # MCP server implementation
├── pyproject.toml      # uv project configuration and dependencies
└── README.md          # This file
```

### Add to claude code

claude mcp add ai-prompt -- /Users/giuseppemento/.local/bin/uv run --with mcp mcp run /Users/giuseppemento/private-repos/ai-prompts/local.py

## Troubleshooting

### Server Won't Start

- Check Python version: `python --version` (requires 3.8+)
- Verify dependencies: `uv sync`
- Check file permissions on server.py
- Ensure uv is installed: `uv --version`

### Prompts Not Loading

- Ensure prompt files are in recognized directories
- Check file encoding (should be UTF-8)
- Verify proper markdown structure

### Claude Desktop Integration Issues

- Verify the path in claude_desktop_config.json is correct
- Restart Claude Desktop after configuration changes
- Check Claude Desktop logs for error messages

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add new prompts following the established structure
4. Test with the MCP server
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:

1. Check the troubleshooting section above
2. Review existing GitHub issues
3. Create a new issue with detailed information about your problem
