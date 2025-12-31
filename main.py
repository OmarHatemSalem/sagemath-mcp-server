#!/usr/bin/env sage -python
from sage.all import *
from sage.interfaces.gap import Gap

from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

# Initialize GAP interface
gap = Gap(use_workspace_cache=False)

# Initialize FastMCP server
mcp = FastMCP(
    name="sagemath-server",
    host="0.0.0.0",
    port=8000,
)

# Define a tool
@mcp.tool()
def get_group_info(g: str) -> Dict[str, Any]:
    """Returns information about a group."""
    grp = gap.Eval(g)

    return {
        "order": grp.Order(),
        "is_abelian": grp.IsAbelian(),
        "generators": grp.Generators(),
        "center": grp.Center(),
    }

def main():
    #Run the MCP server with HTTP transport and mount path /mcp
    mcp.run(transport="streamable-http", mount_path="/mcp")

if __name__ == "__main__":
    main()
