import requests

headers = {
  'X-CMC_PRO_API_KEY' : apikey,
  "Accepts" : "application/json"
}

params = {
  "starts" : "1",
  "limit" : "5",
  "convert" : "USD"
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

json = requests.get(url, params=params, headers=headers).json()
print(json)
