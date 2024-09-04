import requests

# Define the base URL
base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address"

# Define the parameters
params = {
    'street': '8905 19th place',
    'city': 'Lake Stevens',
    'state': 'WA',
    'benchmark': 'Public_AR_Current',
    'vintage': 'Current_Current',
    'layers': '8',
    'format': 'json'
}

# Make the GET request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response
    pass
    #print(response.json())
else:
    print(f"Error: {response.status_code}")


geoid = response.json()['result']['addressMatches'][0]['geographies']['Census Tracts'][0]['GEOID']
print(geoid)
