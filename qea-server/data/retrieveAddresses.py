import requests
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Define the Overpass API endpoint
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Define the Overpass API query
query = """
[out:json];
area["name"="Snohomish County"]->.searchArea;
(node["addr:housenumber"](area.searchArea);
 way["addr:housenumber"](area.searchArea);
 relation["addr:housenumber"](area.searchArea););
out body;
"""

def get_coordinates(address):
    geolocator = Nominatim(user_agent="quality-equity-access-transit-geo")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Address not found: {address}")
            return None
    except GeocoderTimedOut:
        # Return None to skip processing this address
        print(f"Timeout occurred for address: {address}. Skipping this address.")
        return None
    except Exception as e:
        # Catch all other exceptions to prevent crashing
        print(f"An unexpected error occurred: {e}")
        return None


# Make the request to the Overpass API
response = requests.get(OVERPASS_URL, params={'data': query})

countStop = 100
count = 0

# Check for successful request
if response.status_code == 200:
    data = response.json()
    addresses = data.get('elements', [])

    # Prepare data for CSV
    address_list = []
    for element in addresses:
        
        count = count + 1

        if 'tags' in element and 'addr:housenumber' in element['tags']:
            addr_id = element.get('id', '')
            addr_type = element.get('type', '')
            housenumber = element['tags'].get('addr:housenumber', '')
            street = element['tags'].get('addr:street', '')
            postcode = element['tags'].get('addr:postcode', '')
            city = element['tags'].get('addr:city', '')
            county = element['tags'].get('addr:county', '')
            state = element['tags'].get('addr:state', '')
            country = element['tags'].get('addr:country', '')
            
            address_string = f'{housenumber} {street} {postcode} {city} {country} {state} {country}'
            address_string = address_string.replace("nan", "").strip()
            

            coordinates = get_coordinates(address_string)
            if coordinates != None:
                
                latitude, longitude = coordinates
                

                if addr_id and addr_type and housenumber and street:  # Ensure key fields are not empty
                    address = {
                        'id': addr_id,
                        'type': addr_type,
                        'housenumber': housenumber,
                        'street': street,
                        'city': city,
                        'county': county,
                        'state': state,
                        'country': country,
                        'postcode': postcode,
                        'longitude': longitude,
                        'latitude': latitude,
                        
                    }
                    address_list.append(address)
                else:
                    pass
            else: 
                pass
        if count > countStop:
            break

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(address_list)
    df.to_csv('snohomish_addresses.csv', index=False)
    print(f"Saved {len(address_list)} addresses to 'snohomish_addresses.csv'.")
else:
    print(f"Request failed with status code {response.status_code}")
