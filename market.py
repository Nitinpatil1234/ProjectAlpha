from exchange import client

def get_candles(symbol="BTCUSDT", interval=client.KLINE_INTERVAL_5MINUTE, limit=200):
    candles = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    return candles


def get_current_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])