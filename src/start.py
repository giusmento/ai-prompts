from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local_ai_prompts")

@mcp.prompt()
def add_note_to_file(topic:str) -> str:
    """Add a note to a specified file."""
    return f"Note added {topic}"

@mcp.tool()
def add(a: int, b:int) -> int:
    """ add two numbers """
    return a + b

def main():
    mcp.run()