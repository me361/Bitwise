import requests
import pandas as pd
from datetime import datetime, timedelta
import os

class CryptoDataFetcher:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.output_file = "data/crypto_market.csv"

    def get_historical_data(self, coin_id):
        """Fetch 6 months of historical data for a given coin."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)
        
        url = f"{self.base_url}/coins/{coin_id}/market_chart/range"
        params = {
            'vs_currency': 'usd',
            'from': int(start_date.timestamp()),
            'to': int(end_date.timestamp())
        }
        
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data for {coin_id}: {response.text}")
        
        data = response.json()
        df = pd.DataFrame(data['prices'], columns=['timestamp', f'{coin_id}_price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df

    def fetch_and_save_market_data(self):
        """Fetch and combine data for BTC, ETH, and ADA."""
        coins = {
            'bitcoin': 'BTC',
            'ethereum': 'ETH',
            'cardano': 'ADA'
        }
        
        all_data = None
        for coin_id, symbol in coins.items():
            print(f"Fetching data for {symbol}...")
            df = self.get_historical_data(coin_id)
            df.columns = [f"{symbol}_price"]
            
            if all_data is None:
                all_data = df
            else:
                all_data = all_data.join(df)
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Save to CSV
        all_data.to_csv(self.output_file)
        print(f"Market data saved to {self.output_file}")
        return all_data 