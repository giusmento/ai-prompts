from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local_ai_prompts")

@mcp.prompt()
def create_commit(topic:str) -> str:
    """this prompt defines a template for committing a piece of work"""
    return f"""
    Create a git commit with the following template:
    - Title: 
    - Description: {topic}
    - Type: feat, fix, docs, style, refactor, perf, test
    - Main changes: Add here the main changes
    """

@mcp.tool()
def add(a: int, b:int) -> int:
    """ add two numbers """
    return a + b

def main():
    mcp.run()