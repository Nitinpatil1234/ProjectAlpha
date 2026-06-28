from exchange import client

account = client.get_account()

for balance in account["balances"]:
    if float(balance["free"]) > 0:
        print(balance)