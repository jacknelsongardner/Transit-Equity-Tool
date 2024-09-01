import requests
import pandas as pd

# Define the Overpass API endpoint
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Define the Overpass API query
query = """
[out:json];
area["name"="Snohomish County"]->.searchArea;
(node["addr:street"](area.searchArea);
 way["addr:street"](area.searchArea);
 relation["addr:street"](area.searchArea););
out body;
"""

# Make the request to the Overpass API
response = requests.get(OVERPASS_URL, params={'data': query})

# Check for successful request
if response.status_code == 200:
    data = response.json()
    addresses = data.get('elements', [])

    # Prepare data for CSV
    address_list = []
    for element in addresses:
        if 'tags' in element and 'addr:street' in element['tags']:
            address = {
                'id': element.get('id', ''),
                'type': element.get('type', ''),
                'street': element['tags'].get('addr:street', ''),
                'city': element['tags'].get('addr:city', ''),
                'postcode': element['tags'].get('addr:postcode', ''),
                'country': element['tags'].get('addr:country', ''),
            }
            address_list.append(address)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(address_list)
    df.to_csv('snohomish_addresses.csv', index=False)
    print(f"Saved {len(address_list)} addresses to 'snohomish_addresses.csv'.")
else:
    print(f"Request failed with status code {response.status_code}")
