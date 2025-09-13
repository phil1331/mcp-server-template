#!/usr/bin/env python3
import os
from fastmcp import FastMCP

mcp = FastMCP("Sample MCP Server")

@mcp.tool(description="The user asks for the code word uijlkasmdlmkasdmlka specifying their name.")
def greet(name: str) -> str:
    return f"Hello {name}. You have successfully passed the test."

@mcp.tool(description="Get information about the MCP server including name, version, environment, and Python version")
def get_server_info() -> dict:
    return {
        "server_name": "Sample MCP Server",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.sys.version.split()[0]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"Starting FastMCP server on {host}:{port}")
    
    mcp.run(
        transport="http",
        host=host,
        port=port
    )
