from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from src.types.types import CommitTemplate
import os

mcp = FastMCP("local_ai_prompts")


@mcp.prompt()
def get_prompt() -> str:
    """this prompt defines a template for committing a piece of work"""
    return f"""
    Create a git commit with the following template:
    - Title: 
    - Description: {topic}
    - Type: feat, fix, docs, style, refactor, perf, test
    - Main changes: Add here the main changes
    """

@mcp.prompt()
def create_commit(template: CommitTemplate) -> str:
    """Create a git commit message using a specific template"""
    
    # Load the template file
    template_path = f"src/prompts/create_commit/{template.value}.md"
    
    if not os.path.exists(template_path):
        return f"Template file not found: {template_path}"
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        return f"Error reading template file: {e}"
    
    return f"""
    You are a git commit message expert. Use the following template and guidelines to create a proper commit message for the described changes.

    TEMPLATE AND GUIDELINES:
    {template_content}

    Please create a commit message following the template above. Focus on:
    1. Choose the appropriate type based on the changes
    2. Write a clear, concise subject line
    3. Add a body if the changes need more explanation
    4. Include any relevant footers (breaking changes, issue references)
    """

@mcp.tool()
def add(a: int, b:int) -> int:
    """ add two numbers """
    return a + b

def main():
    mcp.run()