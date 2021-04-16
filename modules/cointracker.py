import requests
import json

base_api_uri = "https://api.coingecko.com/api/v3"

def test_connection():
    request = base_api_uri + "/ping"
    response = requests.get(request)
    message = json.loads(response.text)
    return message['gecko_says']

def get_coinlist():
    request = base_api_uri + "/coins/list?include_platform=false"
    response = requests.get(request)
    results = json.loads(response.text)
    return results

def price_check(coin):
    search_term = coin.lower().replace(' ','-')
    request = base_api_uri + "/simple/price?ids=" + search_term + "&vs_currencies=usd"
    response = requests.get(request)
    results = json.loads(response.text)
    token_price = float(results[search_term]['usd'])
    value = "$" + str(token_price)
    return value

def wallet_value(coin,qty):
    search_term = coin.lower().replace(' ','-')
    request = base_api_uri + "/simple/price?ids=" + search_term + "&vs_currencies=usd"
    response = requests.get(request)
    results = json.loads(response.text)
    token_price = float(results[search_term]['usd'])
    quant = float(qty)
    raw_value = token_price * quant
    value = "$" + str(round(raw_value, 2))
    return value