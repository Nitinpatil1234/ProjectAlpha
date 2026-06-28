import csv


def generate_report():

    try:

        with open("logs/trade_history.csv", "r") as file:

            reader = csv.DictReader(file)

            trades = list(reader)

        total_trades = len(trades)

        if total_trades == 0:
            print("No completed trades found.")
            return

        wins = sum(
            1 for trade in trades
            if trade["Result"] == "WIN"
        )

        losses = total_trades - wins

        win_rate = (wins / total_trades) * 100

        total_pnl = sum(
            float(trade["PnL"])
            for trade in trades
        )

        average_pnl = total_pnl / total_trades

        print("\n========== PERFORMANCE REPORT ==========")
        print(f"Total Trades : {total_trades}")
        print(f"Wins         : {wins}")
        print(f"Losses       : {losses}")
        print(f"Win Rate     : {win_rate:.2f}%")
        print(f"Total PnL    : {total_pnl:.2f}")
        print(f"Average PnL  : {average_pnl:.2f}")
        print("========================================")

    except FileNotFoundError:
        print("trade_history.csv not found.")