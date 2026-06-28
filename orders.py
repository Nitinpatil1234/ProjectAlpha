current_trade = None


def open_trade(signal, entry_price, stop_loss, take_profit, position_size):

    global current_trade

    if current_trade is not None:
        return False

    current_trade = {
        "signal": signal,
        "entry": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "position_size": position_size,
        "status": "OPEN"
    }

    return True


def get_trade():
    return current_trade


def close_trade():
    global current_trade
    current_trade = None


def check_trade(current_price):

    global current_trade

    if current_trade is None:
        return None

    signal = current_trade["signal"]

    if signal == "BUY":

        if current_price <= current_trade["stop_loss"]:
            return "LOSS"

        if current_price >= current_trade["take_profit"]:
            return "WIN"

    elif signal == "SELL":

        if current_price >= current_trade["stop_loss"]:
            return "LOSS"

        if current_price <= current_trade["take_profit"]:
            return "WIN"

    return None