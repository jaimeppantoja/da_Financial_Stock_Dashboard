import yfinance as yf

# def fetch_company_news(ticker_symbol):
#     # Create a ticker object
#     ticker = yf.Ticker(ticker_symbol)

#     # Get news headlines
#     news = ticker.news

#     # Return the news
#     return news

def fetch_company_news(ticker_symbol):
    try:
        # Create a ticker object
        ticker = yf.Ticker(ticker_symbol)

        # Get news headlines
        news = ticker.news

        # Ensure news is not None
        if news is None:
            return []
        return news
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


