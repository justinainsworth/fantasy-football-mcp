# Enhanced Fantasy Football MCP Server

A Model Context Protocol (MCP) server for Yahoo Fantasy Football integration with Claude Desktop. Features advanced lineup optimization, draft assistance, comprehensive league management, and enhanced roster management capabilities.

## 🙏 Attribution

This project is based on the excellent foundation provided by [derekrbreese/fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public). Special thanks to Derek Breese for the initial concept, architecture, and scaffolding that made this enhanced version possible.

## ✨ Enhancements in This Fork

- **Enhanced Roster Management**: Fixed "position already filled" errors with intelligent position change detection
- **Working Waiver Wire Transactions**: Fully functional add/drop player capabilities with proper Yahoo API integration
- **Waiver Status Tracking**: New function to monitor pending waiver claims and their approval status
- **Single-Player Position Changes**: Safer lineup management that changes one player at a time
- **Improved Error Handling**: Comprehensive response parsing and detailed debugging information
- **Fixed Import Dependencies**: Resolved sleeper_api and other module import issues
- **Yahoo API Compliance**: Updated XML formatting to match Yahoo's exact specifications

## Features

- **Multi-League Support**: Manage all your Yahoo Fantasy Football leagues
- **AI-Powered Optimization**: Advanced lineup recommendations with multiple strategies
- **Draft Assistant**: Real-time draft recommendations and analysis
- **Waiver Wire Analysis**: Find top pickups with trending data
- **Position Normalization**: Smart FLEX decisions with position-adjusted scoring
- **Rate Limiting & Caching**: Efficient API usage with built-in optimization

## Quick Start

### Prerequisites

- Python 3.9+
- Claude Desktop
- Yahoo Fantasy Sports account
- Yahoo Developer App credentials

### Installation

1. Clone the repository:
```bash
git clone https://github.com/carterfawson/fantasy-football-mcp.git
cd fantasy-football-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure API credentials:
   - **Yahoo API**: Follow [YAHOO_SETUP.md](YAHOO_SETUP.md) for detailed setup
   - **Reddit API** (optional): See [REDDIT_SETUP.md](REDDIT_SETUP.md) for player sentiment analysis
   - Copy `.env.example` to `.env`
   - Add your API credentials
   - Run authentication: `python utils/setup_yahoo_auth.py`

4. Configure Claude Desktop:
   - Add the MCP server configuration (see [INSTALLATION.md](INSTALLATION.md))
   - Restart Claude Desktop

## Available MCP Tools

### League Management
- `ff_get_leagues` - List all your fantasy football leagues
- `ff_get_league_info` - Get detailed league information
- `ff_get_standings` - View current standings

### Team Management
- `ff_get_roster` - Get your team roster
- `ff_get_matchup` - View matchup details with opponent analysis
- `ff_get_opponent_roster` - Get opponent's roster for matchup planning
- `ff_get_opponent_roster_comparison` - Detailed roster comparison and insights
- `ff_get_optimal_lineup` - Get AI lineup recommendations

### 🆕 Enhanced Roster Management
- `ff_set_lineup` - Set your starting lineup (enhanced with intelligent position change detection)
- `ff_change_player_position` - Move a single player to a different position (safer than full lineup changes)
- `ff_add_player` - Add players from free agents or waiver wire (fully functional)
- `ff_drop_player` - Drop players from your roster
- `ff_get_waiver_status` - Check status of pending waiver claims and transactions

### Player Discovery
- `ff_get_players` - Browse available players
- `ff_get_waiver_wire` - Find top waiver pickups
- `ff_get_draft_rankings` - Get pre-draft rankings

### Draft & Admin
- `ff_get_draft_results` - View draft results
- `ff_get_draft_recommendation` - Get live draft advice
- `ff_refresh_token` - Refresh Yahoo access token

## Project Structure

```
fantasy-football-mcp-public/
├── fantasy_football_multi_league.py  # Main MCP server
├── src/                               # Core modules
│   ├── agents/                        # Specialized agents
│   ├── models/                        # Data models
│   ├── strategies/                    # Lineup strategies
│   └── utils/                         # Utility functions
├── utils/                             # Authentication utilities
├── config/                            # Configuration
└── requirements.txt                   # Dependencies
```

## Configuration

See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

## Security

- Never commit `.env` files or API credentials
- See [SECURITY.md](SECURITY.md) for security policy
- Regularly rotate access tokens

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT - See [LICENSE](LICENSE) file

## Support

For issues or questions, please use the [GitHub Issues](https://github.com/derekrbreese/fantasy-football-mcp-public/issues) page.