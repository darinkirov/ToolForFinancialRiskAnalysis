class FinancialInstrument:
    def __init__(self, symbol, price, volatility):
        self.symbol = symbol
        self.price = price
        self.volatility = volatility

    def calculate_value_at_risk(self, confidence_level=0.95):
        # Calculate Value at Risk (VaR) using a simple method (e.g., Normal Distribution)
        # VaR = z * sigma * sqrt(time_period)
        z_score = 1.645  # For 95% confidence level (can be adjusted)
        time_period = 1  # Assuming daily time period for simplicity
        var = z_score * self.volatility * (time_period ** 0.5)
        return var

    def calculate_expected_shortfall(self, confidence_level=0.95):
        # Calculate Expected Shortfall (ES) using VaR and assuming normal distribution
        var = self.calculate_value_at_risk(confidence_level)
        es = var / confidence_level
        return es

# Example usage:
if __name__ == "__main__":
    # Create instances of financial instruments
    stock_A = FinancialInstrument("AAPL", 150.0, 0.2)  # Symbol, Price, Volatility
    stock_B = FinancialInstrument("GOOG", 2500.0, 0.3)

    # Calculate risk metrics
    var_A = stock_A.calculate_value_at_risk()
    es_A = stock_A.calculate_expected_shortfall()
    var_B = stock_B.calculate_value_at_risk()
    es_B = stock_B.calculate_expected_shortfall()

    # Print results
    print(f"Financial Instrument: {stock_A.symbol}")
    print(f"Value at Risk (VaR) at 95% confidence level: ${var_A:.2f}")
    print(f"Expected Shortfall (ES) at 95% confidence level: ${es_A:.2f}\n")

    print(f"Financial Instrument: {stock_B.symbol}")
    print(f"Value at Risk (VaR) at 95% confidence level: ${var_B:.2f}")
    print(f"Expected Shortfall (ES) at 95% confidence level: ${es_B:.2f}")
