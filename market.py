from exchange import client
import time


def get_candles(
    symbol="BTCUSDT",
    interval=client.KLINE_INTERVAL_5MINUTE,
    limit=10000
):

    candles = []

    end_time = None

    while len(candles) < limit:

        batch = client.get_klines(
            symbol=symbol,
            interval=interval,
            limit=1000,
            endTime=end_time
        )

        if not batch:
            break

        candles = batch + candles

        end_time = batch[0][0] - 1

        print(f"Downloaded {len(candles)} candles...")

        time.sleep(0.2)

    return candles[-limit:]


def get_current_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])