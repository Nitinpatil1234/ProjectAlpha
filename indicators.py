import pandas as pd
from ta.volatility import AverageTrueRange


def calculate_rsi(close_prices, period=14):
    close = pd.Series(close_prices)

    delta = close.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]

def calculate_ema(close_prices, period=50):
    close = pd.Series(close_prices)
    ema = close.ewm(span=period, adjust=False).mean()
    return ema.iloc[-1]

def calculate_atr(candles, period=14):

    import pandas as pd

    df = pd.DataFrame(
        candles,
        columns=[
            "Open Time",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Close Time",
            "Quote Asset Volume",
            "Trades",
            "Taker Buy Base",
            "Taker Buy Quote",
            "Ignore"
        ]
    )

    df["High"] = df["High"].astype(float)
    df["Low"] = df["Low"].astype(float)
    df["Close"] = df["Close"].astype(float)

    atr = AverageTrueRange(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        window=period
    )

    return atr.average_true_range().iloc[-1]