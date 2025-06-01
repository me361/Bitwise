from colorama import init, Fore, Style
from data_fetcher import CryptoDataFetcher
from advisor import CryptoAdvisor
from personality import BitwisePersonality
import sys

class BitwiseChatbot:
    def __init__(self):
        init()  # Initialize colorama
        self.personality = BitwisePersonality()
        self.data_fetcher = CryptoDataFetcher()
        self.advisor = None
        
    def initialize(self):
        """Initialize the chatbot by fetching initial data."""
        print(f"{Fore.YELLOW}Initializing Bitwise and fetching market data...{Style.RESET_ALL}")
        try:
            self.data_fetcher.fetch_and_save_market_data()
            self.advisor = CryptoAdvisor()
            print(self.personality.welcome_message())
        except Exception as e:
            print(f"{Fore.RED}Error initializing Bitwise: {str(e)}{Style.RESET_ALL}")
            sys.exit(1)

    def update_data(self):
        """Update market data."""
        try:
            self.data_fetcher.fetch_and_save_market_data()
            self.advisor = CryptoAdvisor()
            print(f"{Fore.GREEN}Market data updated successfully.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error updating market data: {str(e)}{Style.RESET_ALL}")

    def show_portfolio(self):
        """Display portfolio information."""
        try:
            value = self.advisor.calculate_portfolio_value()
            changes = self.advisor.get_price_changes()
            print(self.personality.format_portfolio_summary(value, changes))
        except Exception as e:
            print(f"{Fore.RED}Error displaying portfolio: {str(e)}{Style.RESET_ALL}")

    def show_analysis(self):
        """Display detailed market analysis and advice."""
        try:
            analysis = self.advisor.generate_advice()
            print(self.personality.format_portfolio_summary(
                analysis['portfolio_value'], 
                analysis['price_changes']
            ))
            print(self.personality.format_moving_averages(analysis['moving_averages']))
            print(self.personality.format_advice(analysis['advice']))
        except Exception as e:
            print(f"{Fore.RED}Error generating analysis: {str(e)}{Style.RESET_ALL}")

    def run(self):
        """Main chat loop."""
        self.initialize()
        
        while True:
            try:
                command = input(f"\n{Fore.CYAN}Bitwise>{Style.RESET_ALL} ").strip().lower()
                
                if command == 'exit':
                    print(self.personality.goodbye_message())
                    break
                elif command == 'help':
                    print(self.personality.help_message())
                elif command == 'portfolio':
                    self.show_portfolio()
                elif command == 'analysis':
                    self.show_analysis()
                elif command == 'update':
                    self.update_data()
                else:
                    print(f"{Fore.YELLOW}Unknown command. Type 'help' for available commands.{Style.RESET_ALL}")
                    
            except KeyboardInterrupt:
                print(self.personality.goodbye_message())
                break
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}") 