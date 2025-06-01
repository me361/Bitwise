# Bitwise Crypto Advisor

A terminal-based cryptocurrency advisor that provides personalized investment insights based on market analysis.

## Features

- Real-time cryptocurrency market data from CoinGecko API
- Portfolio tracking and analysis
- Technical analysis with moving averages
- Personalized investment advice
- Color-coded terminal interface

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Create or modify your portfolio in `user/portfolio.json`:
```json
{
    "BTC": 0.5,
    "ETH": 2.0,
    "ADA": 1000.0
}
```

2. Run the advisor:
```bash
python run.py
```

## Available Commands

- `portfolio`: View your current portfolio and its value
- `analysis`: Get detailed market analysis and advice
- `update`: Update market data
- `help`: Show help message
- `exit`: Exit the program

## Data Sources

- Market data is fetched from the CoinGecko API
- Historical data covers the past 6 months
- Data is cached locally in `data/crypto_market.csv`