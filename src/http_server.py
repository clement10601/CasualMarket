#!/usr/bin/env python3
"""
Streamable HTTP server for MCP.

This module provides an HTTP interface for the MCP server using FastMCP's
streamable HTTP transport.
"""

from .server import mcp
from .utils.logging import get_logger, setup_logging

setup_logging()
logger = get_logger(__name__)


def main() -> None:
    """Start the MCP server using streamable HTTP transport."""
    logger.info("Starting CasualMarket MCP Server with streamable HTTP support")
    logger.info("Server will be available at http://0.0.0.0:8000")
    logger.info("Streamable HTTP endpoint: http://0.0.0.0:8000/mcp")

    mcp.run(transport="http", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
