# Claude Code Configuration

## Virtual Environment Setup

This project uses a Python virtual environment with Python 3.11 to ensure proper dependency management and compatibility with the MCP (Model Context Protocol) SDK.

### Virtual Environment Details
- **Location**: `./venv/`
- **Python Version**: Python 3.11 (required for MCP SDK compatibility)
- **Dependencies**: Installed from `pyproject.toml` (not `requirements.txt`)

### Running the MCP Server

**Recommended approach**: Use the provided startup script:
```bash
./start_server.sh
```

**Manual approach**:
```bash
source venv/bin/activate
python fantasy_football_multi_league.py
```

### Development Commands

When developing or debugging, always activate the virtual environment first:
```bash
source venv/bin/activate
```

Then run commands like:
- `python utils/setup_yahoo_auth.py` - Setup Yahoo authentication
- `python utils/verify_setup.py` - Verify installation
- `pytest` - Run tests (if installed with dev dependencies)
- `ruff check` - Run linting
- `black .` - Format code

### Claude Desktop Configuration

Update your Claude Desktop configuration to use the startup script:

```json
{
  "mcpServers": {
    "fantasy-football": {
      "command": "/absolute/path/to/fantasy-football-mcp-public/start_server.sh",
      "env": {
        "YAHOO_ACCESS_TOKEN": "your_access_token",
        "YAHOO_REFRESH_TOKEN": "your_refresh_token",
        "YAHOO_CONSUMER_KEY": "your_consumer_key",
        "YAHOO_CONSUMER_SECRET": "your_consumer_secret",
        "YAHOO_GUID": "your_yahoo_guid"
      }
    }
  }
}
```

### Project Structure Note

The project has both `requirements.txt` and `pyproject.toml`. Use `pyproject.toml` for proper dependency management as it includes the correct MCP SDK version and dependency constraints.