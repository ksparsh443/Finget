import yfinance as yf


class MarketDataFetcher:
    def get_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.history(period="1mo")


fetcher = MarketDataFetcher()
print(fetcher.get_stock_data("AAPL"))
