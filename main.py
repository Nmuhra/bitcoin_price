import requests

# Set the URL for the API endpoint
api_url = 'https://api.coindesk.com/v1/bpi/currentprice/ZAR.json'

# Make a GET request to the API
response = requests.get(api_url)

# Convert the response to a Python dictionary
data = response.json()

# Get the current price of Bitcoin in South African Rand
price = data['bpi']['ZAR']['rate']

# Print the current price
print(f'Bitcoin:\n R{price}')
