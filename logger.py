import csv
import os
from datetime import datetime

LOG_FILE = "logs/trades.csv"


def log_signal(symbol, price, ema50, ema200, rsi, atr, trend, signal, position_size):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Symbol",
                "Price",
                "EMA50",
                "EMA200",
                "Trend",
                "RSI",
                "ATR",
                "Signal",
                "Position Size"
            ])

        writer.writerow([
            now,
            symbol,
            round(price, 2),
            round(ema50, 2),
            round(ema200, 2),
            trend,
            round(rsi, 2),
            round(atr, 2),
            signal,
            position_size
        ])

    print("\n========== TRADE LOG ==========")
    print(f"Time          : {now}")
    print(f"Symbol        : {symbol}")
    print(f"Price         : {price:.2f}")
    print(f"EMA50         : {ema50:.2f}")
    print(f"EMA200        : {ema200:.2f}")
    print(f"Trend         : {trend}")
    print(f"RSI           : {rsi:.2f}")
    print(f"ATR           : {atr:.2f}")
    print(f"Signal        : {signal}")
    print(f"Position Size : {position_size}")
    print("================================")