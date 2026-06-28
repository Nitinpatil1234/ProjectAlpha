from market import get_candles, get_current_price
from indicators import calculate_rsi, calculate_ema, calculate_atr
from strategy import get_signal
from risk import calculate_position_size
from logger import log_signal
from trade_manager import calculate_trade_levels
from trade_history import log_trade_result
from orders import (
    open_trade,
    get_trade,
    check_trade,
    close_trade
)


def run_bot():

    symbol = "BTCUSDT"

    # Get Market Data
    candles = get_candles(symbol)
    close_prices = [float(candle[4]) for candle in candles]
    current_price = get_current_price(symbol)

    # Calculate Indicators
    rsi = calculate_rsi(close_prices)
    ema50 = calculate_ema(close_prices, 50)
    ema200 = calculate_ema(close_prices, 200)
    atr = calculate_atr(candles)

    # Determine Trend
    if ema50 > ema200:
        trend = "BULLISH"
    elif ema50 < ema200:
        trend = "BEARISH"
    else:
        trend = "SIDEWAYS"

    # Generate Signal
    signal = get_signal(
        rsi,
        current_price,
        ema50,
        ema200
    )

    balance = 10000
    risk_percent = 1

    stop_loss = None
    take_profit = None
    position_size = 0

    # Trade Calculation
    if signal in ["BUY", "SELL"]:

        stop_loss, take_profit = calculate_trade_levels(
            signal,
            current_price,
            atr
        )

        position_size = calculate_position_size(
            balance,
            risk_percent,
            current_price,
            stop_loss
        )

        trade_opened = open_trade(
            signal,
            current_price,
            stop_loss,
            take_profit,
            position_size
        )

        if trade_opened:
            print("\n✅ Paper Trade Opened Successfully")
        else:
            print("\n⚠️ Trade Already Open")

    # Logger
    log_signal(
        symbol,
        current_price,
        ema50,
        ema200,
        rsi,
        atr,
        trend,
        signal,
        position_size
    )

    # Trade Levels
    if signal in ["BUY", "SELL"]:
        print("\n========== TRADE LEVELS ==========")
        print(f"Entry Price   : {current_price:.2f}")
        print(f"Stop Loss     : {stop_loss:.2f}")
        print(f"Take Profit   : {take_profit:.2f}")
        print("==================================")
    else:
        print("\nNo trade setup found.")

    # Open Trade
    trade = get_trade()

    if trade:
        print("\n========== OPEN TRADE ==========")
        print(f"Signal        : {trade['signal']}")
        print(f"Entry Price   : {trade['entry']:.2f}")
        print(f"Stop Loss     : {trade['stop_loss']:.2f}")
        print(f"Take Profit   : {trade['take_profit']:.2f}")
        print(f"Position Size : {trade['position_size']}")
        print(f"Status        : {trade['status']}")
        print("================================")

        result = check_trade(current_price)

        if result:
         print("\n================================")
         print(f"TRADE CLOSED : {result}")
         print("================================")

        log_trade_result(
            trade["signal"],
            trade["entry"],
            current_price,
            result,
            trade["position_size"]
        )

        close_trade()