def calculate_position_size(balance, risk_percent, entry_price, stop_loss_price):
    risk_amount = balance * (risk_percent / 100)

    price_difference = abs(entry_price - stop_loss_price)

    if price_difference == 0:
        return 0

    quantity = risk_amount / price_difference

    return round(quantity, 6)