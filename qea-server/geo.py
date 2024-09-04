from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import requests


# Coordinates provided
LAT, LON = 0, 1  # Adjust based on your coordinate system

countryCode = '14000US'

def get_geoCode(coordinates):

    address_line, city, state, country, postcode = get_address(coordinates)

    print(coordinates)

    # Define the base URL
    base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address"

    # Define the parameters
    params = {
        'street': address_line,
        'city': city,
        'state': state,
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
    output = countryCode + str(geoid)
    
    return output

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
    

def get_address(coordinates):
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="quality-equity-access-transit-geo")
    
    # Define a function to handle potential timeout
    def geocode_with_timeout(lat, lon):
        try:
            return geolocator.reverse((lat, lon), language='en')
        except GeocoderTimedOut:
            return geocode_with_timeout(lat, lon)

    # Get the location information
    location = geocode_with_timeout(coordinates[LAT], coordinates[LON])
    
    if location:
        # Extract address components
        address = location.raw.get('address', {})
        address_line = address.get('road', '') + ' ' + address.get('house_number', '')
        city = address.get('city', '')
        town = address.get('town', '')
        state = address.get('state', '')
        country = address.get('country', '')
        postcode = address.get('postcode', '')

        if city == '' or city == None:
            city = town

        print(location.raw)

        # Return address as a tuple
        return (address_line.strip(), city, state, country, postcode)
    else:
        return ('Address not found', '', '', '', '')




coordinates = get_coordinates('8905 19th pl SE, Lake Stevens, WA 98258')
geoCode = get_geoCode(coordinates=coordinates)

print(coordinates)
print(get_address(coordinates))
print(geoCode)
