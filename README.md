# GAP MCP Server

A Model Context Protocol (MCP) server that provides access to GAP (Groups, Algorithms, Programming) functionality through SageMath. This server enables AI assistants and other MCP clients to perform group theory computations and retrieve information about mathematical groups.

## Purpose

This server bridges the gap between MCP clients (such as AI assistants) and the powerful GAP system for computational discrete algebra. It exposes GAP's group theory capabilities through a simple HTTP-based MCP interface, allowing clients to:

- Query group properties
- Compute group invariants
- Analyze group structures
- Perform algebraic computations

## Available Tools

### `get_group_info`

Returns comprehensive information about a mathematical group.

**Parameters:**
- `g` (string): A GAP expression representing a group (e.g., `"SymmetricGroup(4)"`, `"AlternatingGroup(5)"`)

**Returns:**
- `order`: The order (number of elements) of the group
- `is_abelian`: Boolean indicating whether the group is abelian (commutative)
- `generators`: The generators of the group
- `center`: The center of the group (elements that commute with all other elements)

**Example:**
```python
# Query the symmetric group S4
get_group_info("SymmetricGroup(4)")

# Query the alternating group A5
get_group_info("AlternatingGroup(5)")

# Query a dihedral group
get_group_info("DihedralGroup(8)")
```

## Running the Server

### Using Docker (Recommended)

1. **Build the Docker image:**
   ```bash
   docker build -t gap-mcp-server .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 gap-mcp-server
   ```

The server will be accessible at `http://localhost:8000/mcp`

### Running Locally

**Prerequisites:**
- SageMath installed on your system
- Python 3.8 or higher
- Recommended: Use a conda environment or virtual environment to isolate dependencies

**Steps:**

1. **Install dependencies:**
   ```bash
   sage -pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   sage -python main.py
   ```

The server will start on `http://0.0.0.0:8000/mcp`

## Connecting to the Server

This server uses the MCP protocol with streamable-HTTP transport. To connect from an MCP client:

- **Server URL:** `http://localhost:8000/mcp`
- **Transport:** streamable-http
- **Port:** 8000


