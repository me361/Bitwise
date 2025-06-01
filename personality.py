from colorama import Fore, Style

class BitwisePersonality:
    def __init__(self):
        self.name = "Bitwise"
        
    def format_price_change(self, change):
        """Format price change with color."""
        if change > 0:
            return f"{Fore.GREEN}+{change:.2f}%{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}{change:.2f}%{Style.RESET_ALL}"

    def welcome_message(self):
        return (
            f"{Fore.CYAN}Welcome to Bitwise - Your Analytical Crypto Advisor{Style.RESET_ALL}\n"
            "I analyze market data and provide measured, data-driven insights.\n"
            "Type 'help' to see available commands."
        )

    def format_portfolio_summary(self, value, changes):
        """Format portfolio summary with colors."""
        summary = [
            f"\n{Fore.CYAN}Portfolio Overview:{Style.RESET_ALL}",
            f"Total Value: ${value:,.2f}",
            "\nPrice Changes (7d):"
        ]
        
        for coin, change in changes.items():
            summary.append(f"{coin}: {self.format_price_change(change)}")
            
        return "\n".join(summary)

    def format_moving_averages(self, mas):
        """Format moving averages information."""
        lines = [f"\n{Fore.CYAN}Moving Averages:{Style.RESET_ALL}"]
        
        for coin, averages in mas.items():
            lines.append(f"\n{coin}:")
            for period, value in averages.items():
                lines.append(f"  {period} MA: ${value:,.2f}")
                
        return "\n".join(lines)

    def format_advice(self, advice_list):
        """Format investment advice with a wise tone."""
        if not advice_list:
            return f"\n{Fore.YELLOW}I have no specific recommendations at this time. Continue monitoring the market conditions.{Style.RESET_ALL}"
        
        formatted = [f"\n{Fore.CYAN}Investment Insights:{Style.RESET_ALL}"]
        for advice in advice_list:
            formatted.append(f"• {advice}")
            
        return "\n".join(formatted)

    def help_message(self):
        return """
Available commands:
- portfolio: View your current portfolio and its value
- analysis: Get detailed market analysis and advice
- update: Update market data
- help: Show this help message
- exit: Exit the program
"""

    def goodbye_message(self):
        return (
            f"\n{Fore.CYAN}Thank you for consulting with Bitwise. "
            "May your investments be wise and profitable.{Style.RESET_ALL}"
        ) 