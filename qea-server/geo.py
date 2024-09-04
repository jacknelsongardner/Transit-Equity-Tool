from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut



# Coordinates provided
LAT, LON = 0, 1  # Adjust based on your coordinate system




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


