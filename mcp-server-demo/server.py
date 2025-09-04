from mcp.server.fastmcp import FastMCP

import resources as res_tools
# Create an MCP server
mcp = FastMCP("EmojiUsage")

# Exitence queries
@mcp.tool()
def get_possible_contexts():
    """
    Returns list of possible contexts or feelings associated to an emoji.
    """
    return res_tools.get_contexts()

@mcp.tool()
def get_possible_contexts():
    """
    Returns list of possible social media plaftorms where emoji usage is recognized.
    """
    return res_tools.get_platforms()

@mcp.tool()
def is_valid_emoji():
    """
    Validates wether a given emoji string exists within the emoji usage dataset.
    """
    return res_tools.get_emoji_exists()




# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

@mcp.prompt()
def summarize(text: str) ->str:
    return f"Summarize the following:\n\n{text}"