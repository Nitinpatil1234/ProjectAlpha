from market import get_candles
from indicators import (
    calculate_rsi,
    calculate_ema,
    calculate_adx
)
from strategy import get_signal
from volume import (
    calculate_average_volume,
    get_current_volume
)


def run_backtest():

    candles = get_candles("BTCUSDT")

    wins = 0
    losses = 0
    expired = 0
    total_signals = 0

    for i in range(200, len(candles) - 30):

        close_prices = [
            float(candle[4])
            for candle in candles[:i]
        ]

        current_price = close_prices[-1]

        rsi = calculate_rsi(close_prices)
        ema50 = calculate_ema(close_prices, 50)
        ema200 = calculate_ema(close_prices, 200)

        adx = calculate_adx(candles[:i])

        average_volume = calculate_average_volume(
            candles[:i]
        )

        current_volume = get_current_volume(
            candles[:i]
        )

        signal = get_signal(
            rsi,
            current_price,
            ema50,
            ema200
        )

        # ADX Filter
        # if adx <= 25:
        #     signal = "HOLD"

        # Volume Filter
        # if current_volume < (average_volume * 0.8):
        #     signal = "HOLD"

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
                    trade_closed = True
                    break

                elif low_price <= stop_loss:
                    losses += 1
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
                    trade_closed = True
                    break

                elif high_price >= stop_loss:
                    losses += 1
                    trade_closed = True
                    break

            if not trade_closed:
                expired += 1

    total_trades = wins + losses

    if total_trades > 0:
        win_rate = (wins / total_trades) * 100
    else:
        win_rate = 0

    print("\n========== BACKTEST ==========")
    print(f"Total Candles : {len(candles)}")
    print(f"Signals       : {total_signals}")
    print(f"Wins          : {wins}")
    print(f"Losses        : {losses}")
    print(f"Expired       : {expired}")
    print(f"Total Trades  : {total_trades}")
    print(f"Win Rate      : {win_rate:.2f}%")
    print("==============================")


if __name__ == "__main__":
    run_backtest()