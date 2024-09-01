import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import random



# Define the function to get coordinates
def get_coordinates(address):
    geolocator = Nominatim(user_agent="quality-equity-access-transit-geo")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except GeocoderTimedOut:
        return "Geocoding service timed out. Try again."


# Load the input CSV with addresses
input_csv = 'snohomish_addresses.csv'
addresses_df = pd.read_csv(input_csv)

# Prepare a DataFrame to store the results
results = []

# Iterate over each row in the input DataFrame
for _, row in addresses_df.iterrows():
    address = f"{row.get('housenumber', '')},{row.get('street', '')}, {row.get('city', '')}, {row.get('county', '')}, {row.get('state', '')}, {row.get('country', '')}, {row.get('postcode', '')}"
    
    print(address)

    address = address.replace("nan,", "").strip()
    address = address.replace("nan", "").strip()
    
    print(address)

    address_id = row['id']

    coordinates = get_coordinates(address)
    latitude = None
    longitude = None
    
    if coordinates != None:
        latitude, longitude = coordinates

    if latitude is not None and longitude is not None:
        results.append({'id': address_id, 'latitude': latitude, 'longitude': longitude})
    else:
        pass
    

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a new CSV file
output_csv = 'snohomish_coordinates.csv'
results_df.to_csv(output_csv, index=False)
print(f"Saved coordinates to '{output_csv}'.")
