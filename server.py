#!/usr/bin/env python3
"""
AI Prompts MCP Server

A Model Context Protocol server that provides access to curated AI prompts
for various development tasks including PRD creation, task generation,
and documentation creation.
"""

import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("AI Prompts Server")

# Global cache for prompts
prompts_cache: Dict[str, Dict[str, Any]] = {}

def load_prompts():
    """Load all prompt files from the repository."""
    prompts_dir = Path(__file__).parent
    prompt_files = []
    
    # Find all .md files
    for pattern in ["**/*.md", "**/*.prompt.md"]:
        prompt_files.extend(prompts_dir.glob(pattern))
    
    # Filter out README files and git directories
    prompt_files = [f for f in prompt_files if not any(part.startswith('.') for part in f.parts) 
                   and f.name.lower() != "readme.md"]
    
    for file_path in prompt_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse frontmatter if present
            frontmatter = {}
            body = content
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1].strip()
                    body = parts[2].strip()
                    
                    # Simple YAML parsing for basic fields
                    for line in frontmatter_text.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            frontmatter[key.strip()] = value.strip()
            
            # Extract title from first heading
            title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem
            
            # Clean the title for ID generation
            prompt_id = re.sub(r'[^\w\-]', '_', title.lower().replace(' ', '_'))
            
            # Handle duplicate IDs by appending file stem
            if prompt_id in prompts_cache:
                prompt_id = f"{prompt_id}_{file_path.stem}"
            
            # Store prompt data
            prompts_cache[prompt_id] = {
                'id': prompt_id,
                'title': title,
                'description': frontmatter.get('description', ''),
                'category': file_path.parent.name,
                'file_path': str(file_path.relative_to(prompts_dir)),
                'content': body,
                'frontmatter': frontmatter
            }
            
            logger.info(f"Loaded prompt: {prompt_id} from {file_path}")
            
        except Exception as e:
            logger.error(f"Error loading prompt from {file_path}: {e}")

# Load prompts on startup
load_prompts()

@mcp.resource("prompt://{prompt_id}")
async def get_prompt_resource(prompt_id: str) -> str:
    """Get a specific prompt resource."""
    if prompt_id not in prompts_cache:
        raise ValueError(f"Prompt not found: {prompt_id}")
    
    return prompts_cache[prompt_id]['content']

@mcp.tool()
async def search_prompts(query: str, category: Optional[str] = None) -> str:
    """Search for prompts by keywords or category.
    
    Args:
        query: Search query (searches in titles and descriptions)
        category: Filter by category (optional)
    """
    query_lower = query.lower()
    results = []
    
    for prompt_id, prompt_data in prompts_cache.items():
        # Check category filter
        if category and prompt_data['category'] != category:
            continue
        
        # Check query match
        if query:
            searchable_text = (
                prompt_data['title'].lower() + " " +
                prompt_data['description'].lower() + " " +
                prompt_data['category'].lower()
            )
            if query_lower not in searchable_text:
                continue
        
        results.append({
            'id': prompt_id,
            'title': prompt_data['title'],
            'category': prompt_data['category'],
            'description': prompt_data['description'],
            'file_path': prompt_data['file_path']
        })
    
    if not results:
        return "No prompts found matching your search criteria."
    
    response = f"Found {len(results)} prompts:\n\n"
    for r in results:
        response += f"**{r['id']}**: {r['title']} ({r['category']})\n"
        response += f"   Description: {r['description']}\n"
        response += f"   File: {r['file_path']}\n\n"
    
    return response

@mcp.tool()
async def get_prompt(prompt_id: str) -> str:
    """Get a specific prompt by ID.
    
    Args:
        prompt_id: The ID of the prompt to retrieve
    """
    if prompt_id not in prompts_cache:
        return f"Error: Prompt '{prompt_id}' not found"
    
    prompt_data = prompts_cache[prompt_id]
    response = f"# {prompt_data['title']}\n\n"
    response += f"**Category**: {prompt_data['category']}\n"
    response += f"**File**: {prompt_data['file_path']}\n\n"
    response += prompt_data['content']
    
    return response

@mcp.tool()
async def list_categories() -> str:
    """List all available prompt categories."""
    categories = list(set(p['category'] for p in prompts_cache.values()))
    categories.sort()
    
    category_info = []
    for category in categories:
        count = len([p for p in prompts_cache.values() if p['category'] == category])
        category_info.append(f"- **{category}**: {count} prompts")
    
    return "Available categories:\n\n" + "\n".join(category_info)

@mcp.tool()
async def list_prompts() -> str:
    """List all available prompts."""
    if not prompts_cache:
        return "No prompts available."
    
    response = f"Available prompts ({len(prompts_cache)} total):\n\n"
    
    # Group by category
    categories = {}
    for prompt_id, prompt_data in prompts_cache.items():
        category = prompt_data['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(prompt_data)
    
    for category in sorted(categories.keys()):
        response += f"## {category}\n"
        for prompt_data in categories[category]:
            response += f"- **{prompt_data['id']}**: {prompt_data['title']}\n"
        response += "\n"
    
    return response

def main():
    """Main entry point."""
    mcp.run()

if __name__ == "__main__":
    main()