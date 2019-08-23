from yahoofinancials import YahooFinancials
import pandas as pd

def getDailyHistoricalPrices(stockCode, startDate, endDate):
    yahoo_financials = YahooFinancials(stockCode)
    historical_stock_prices = yahoo_financials.get_historical_price_data(startDate, endDate, 'daily')
    stock_prices = pd.DataFrame.from_dict(historical_stock_prices[stockCode]['prices'])
    stock_prices.rename(columns={"formatted_date": "Date", "open": "Open", "volume": "Volume", "adjclose": "Adj Close", "high": "High", "close": "Close", "low": "Low"},  inplace=True)
    return stock_prices
