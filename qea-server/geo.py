from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

LAT = 0
LON = 1


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



address = "513 State Route 9 Northeast Lake Stevens,  WA 98258"
coordinates = get_coordinates(address)
if coordinates:
    print(f"The coordinates of the address are: Latitude: {coordinates[LAT]}, Longitude: {coordinates[LON]}")
else:
    print("Address not found.")


print('finished')
