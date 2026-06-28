import time
from engine import run_bot


def start_scheduler():

    while True:

        print("\n================================")
        print("Starting New Trading Cycle...")
        print("================================")

        try:
            run_bot()

        except Exception as e:
            print(f"ERROR: {e}")

        print("\nWaiting 5 minutes...\n")

        time.sleep(300)