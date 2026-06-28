def get_signal(rsi, price, ema50, ema200):

    # Uptrend
    if ema50 > ema200:

        if rsi < 35:
            return "BUY"

    # Downtrend
    elif ema50 < ema200:

        if rsi > 65:
            return "SELL"

    return "HOLD"