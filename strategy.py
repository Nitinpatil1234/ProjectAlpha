def get_signal(rsi, price, ema50, ema200):

    # Uptrend
    if ema50 > ema200:

        if rsi < 30 and price > ema50:
            return "BUY"

    # Downtrend
    elif ema50 < ema200:

        if rsi > 70 and price < ema50:
            return "SELL"

    return "HOLD"