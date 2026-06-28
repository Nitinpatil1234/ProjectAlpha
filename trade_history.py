import csv
import os
from datetime import datetime

TRADE_HISTORY_FILE = "logs/trade_history.csv"


def log_trade_result(
    signal,
    entry_price,
    exit_price,
    result,
    position_size
):

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(TRADE_HISTORY_FILE)

    pnl = round(
        (exit_price - entry_price) * position_size,
        2
    )

    if signal == "SELL":
        pnl = -pnl

    with open(TRADE_HISTORY_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Signal",
                "Entry",
                "Exit",
                "Result",
                "Position Size",
                "PnL"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            signal,
            round(entry_price, 2),
            round(exit_price, 2),
            result,
            position_size,
            pnl
        ])

    print("\n===== TRADE RECORDED =====")
    print(f"Result : {result}")
    print(f"PnL    : {pnl}")
    print("==========================")