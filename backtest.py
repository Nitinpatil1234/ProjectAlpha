from market import get_candles
from indicators import calculate_rsi, calculate_ema
from strategy import get_signal


def update_drawdown(balance, max_balance, max_drawdown):

    if balance > max_balance:
        max_balance = balance

    drawdown = (
        (max_balance - balance)
        / max_balance
    ) * 100

    if drawdown > max_drawdown:
        max_drawdown = drawdown

    return max_balance, max_drawdown


def run_backtest():

    candles = get_candles(
    "BTCUSDT",
    limit=10000
)

    wins = 0
    losses = 0
    expired = 0
    total_signals = 0

    starting_balance = 100.0
    balance = 100.0

    max_balance = balance
    max_drawdown = 0

    for i in range(200, len(candles) - 30):

        close_prices = [
            float(candle[4])
            for candle in candles[:i]
        ]

        current_price = close_prices[-1]

        rsi = calculate_rsi(close_prices)
        ema50 = calculate_ema(close_prices, 50)
        ema200 = calculate_ema(close_prices, 200)

        signal = get_signal(
            rsi,
            current_price,
            ema50,
            ema200
        )

        if signal == "HOLD":
            continue

        total_signals += 1

        entry_price = current_price

        # BUY Trade
        if signal == "BUY":

            take_profit = entry_price * 1.0125
            stop_loss = entry_price * 0.99

            trade_closed = False

            for candle in candles[i:i + 30]:

                high_price = float(candle[2])
                low_price = float(candle[3])

                if high_price >= take_profit:

                    wins += 1
                    balance *= 1.0105

                    max_balance, max_drawdown = update_drawdown(
                        balance,
                        max_balance,
                        max_drawdown
                    )

                    trade_closed = True
                    break

                elif low_price <= stop_loss:

                    losses += 1
                    balance *= 0.988

                    max_balance, max_drawdown = update_drawdown(
                        balance,
                        max_balance,
                        max_drawdown
                    )

                    trade_closed = True
                    break

            if not trade_closed:
                expired += 1

        # SELL Trade
        elif signal == "SELL":

            take_profit = entry_price * 0.9875
            stop_loss = entry_price * 1.01

            trade_closed = False

            for candle in candles[i:i + 30]:

                high_price = float(candle[2])
                low_price = float(candle[3])

                if low_price <= take_profit:

                    wins += 1
                    balance *= 1.0125

                    max_balance, max_drawdown = update_drawdown(
                        balance,
                        max_balance,
                        max_drawdown
                    )

                    trade_closed = True
                    break

                elif high_price >= stop_loss:

                    losses += 1
                    balance *= 0.99

                    max_balance, max_drawdown = update_drawdown(
                        balance,
                        max_balance,
                        max_drawdown
                    )

                    trade_closed = True
                    break

            if not trade_closed:
                expired += 1

    total_trades = wins + losses

    if total_trades > 0:
        win_rate = (wins / total_trades) * 100
    else:
        win_rate = 0

    profit_percent = (
        (balance - starting_balance)
        / starting_balance
    ) * 100

    print("\n========== BACKTEST ==========")
    print(f"Total Candles : {len(candles)}")
    print(f"Signals       : {total_signals}")
    print(f"Wins          : {wins}")
    print(f"Losses        : {losses}")
    print(f"Expired       : {expired}")
    print(f"Total Trades  : {total_trades}")
    print(f"Win Rate      : {win_rate:.2f}%")
    print("--------------------------------")
    print(f"Start Balance : ${starting_balance:.2f}")
    print(f"End Balance   : ${balance:.2f}")
    print(f"Profit %      : {profit_percent:.2f}%")
    print(f"Max Drawdown  : {max_drawdown:.2f}%")
    print("==============================")


if __name__ == "__main__":
    run_backtest()