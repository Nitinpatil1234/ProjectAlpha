def calculate_trade_levels(signal, entry_price, atr, atr_multiplier=1.5, risk_reward=2):

    if signal == "BUY":

        stop_loss = entry_price - (atr * atr_multiplier)

        take_profit = entry_price + (
            (entry_price - stop_loss) * risk_reward
        )

    elif signal == "SELL":

        stop_loss = entry_price + (atr * atr_multiplier)

        take_profit = entry_price - (
            (stop_loss - entry_price) * risk_reward
        )

    else:
        return None, None

    return round(stop_loss, 2), round(take_profit, 2)