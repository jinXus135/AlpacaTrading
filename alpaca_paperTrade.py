import requests, json, time

from config import *



#URL = "https://paper-api.alpaca.markets"
#Account_URL = "{}/v2/account".format(URL)
#orders_URL = "{}/v2/orders".format(URL)

headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": sec}
def get_account():
    page = requests.get(Account_URL, headers= headers)

    return json.loads(page.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "Symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    page = requests.post(orders_URL, json = data, headers=headers)
    return json.loads(page.content)

def get_watchlist():
    myList = requests.get(watchlist_URL, headers = headers)
    return json.loads(myList.content)


#testing the create_order function
#response = create_order("AAPL",30, "buy", "market", "gtc")
#print(response)

response = get_watchlist()
print(response)