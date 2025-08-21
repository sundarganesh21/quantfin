import yfinance as yf
import datetime as dt
df = yf.download(tickers = "SPY", start = dt.date(2025,1,1), end = dt.date(2025,8,16), interval = "1d")
df.head()