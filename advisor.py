import pandas as pd
import json
from datetime import datetime, timedelta

class CryptoAdvisor:
    def __init__(self, market_data_file="data/crypto_market.csv", portfolio_file="user/portfolio.json"):
        self.market_data = pd.read_csv(market_data_file, index_col='timestamp', parse_dates=True)
        with open(portfolio_file, 'r') as f:
            self.portfolio = json.load(f)
        
    def calculate_portfolio_value(self):
        """Calculate current portfolio value based on latest prices."""
        latest_prices = self.market_data.iloc[-1]
        total_value = sum(
            self.portfolio.get(coin, 0) * latest_prices[f"{coin}_price"]
            for coin in ["BTC", "ETH", "ADA"]
        )
        return total_value

    def get_price_changes(self, days=7):
        """Calculate price changes over specified period."""
        current_prices = self.market_data.iloc[-1]
        past_prices = self.market_data.iloc[-days]
        
        changes = {}
        for coin in ["BTC", "ETH", "ADA"]:
            price_col = f"{coin}_price"
            pct_change = ((current_prices[price_col] - past_prices[price_col]) 
                         / past_prices[price_col] * 100)
            changes[coin] = pct_change
        
        return changes

    def calculate_moving_averages(self, days=[7, 30]):
        """Calculate moving averages for specified periods."""
        mas = {}
        for coin in ["BTC", "ETH", "ADA"]:
            price_col = f"{coin}_price"
            coin_mas = {}
            for day in days:
                ma = self.market_data[price_col].rolling(window=day).mean().iloc[-1]
                coin_mas[f"{day}d"] = ma
            mas[coin] = coin_mas
        return mas

    def generate_advice(self):
        """Generate personalized investment advice based on analysis."""
        changes = self.get_price_changes()
        mas = self.calculate_moving_averages()
        portfolio_value = self.calculate_portfolio_value()
        
        advice = []
        
        # Portfolio composition advice
        total_allocation = sum(self.portfolio.values())
        for coin in ["BTC", "ETH", "ADA"]:
            allocation = (self.portfolio.get(coin, 0) / total_allocation) * 100
            if allocation > 50:
                advice.append(f"Your {coin} allocation ({allocation:.1f}%) is quite high. "
                            "Consider diversifying to reduce risk.")
            elif allocation < 10 and allocation > 0:
                advice.append(f"Your {coin} position ({allocation:.1f}%) is relatively small. "
                            "Consider increasing it if you believe in its long-term potential.")

        # Technical analysis based advice
        for coin in ["BTC", "ETH", "ADA"]:
            ma_data = mas[coin]
            current_price = self.market_data[f"{coin}_price"].iloc[-1]
            
            if current_price > ma_data["30d"] * 1.1:
                advice.append(f"{coin} is trading significantly above its 30-day moving average. "
                            "Consider taking some profits.")
            elif current_price < ma_data["30d"] * 0.9:
                advice.append(f"{coin} is trading significantly below its 30-day moving average. "
                            "This might present a buying opportunity if you're bullish long-term.")

        return {
            "portfolio_value": portfolio_value,
            "price_changes": changes,
            "moving_averages": mas,
            "advice": advice
        } 