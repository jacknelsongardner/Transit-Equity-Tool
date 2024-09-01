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
            return None
    except GeocoderTimedOut:
        return "Geocoding service timed out. Try again."



address = "8905 19th pl SE, Lake Stevens, Washington 98258"
coordinates = get_coordinates(address)
if coordinates:
    print(f"The coordinates of the address are: Latitude: {coordinates[LAT]}, Longitude: {coordinates[LON]}")
else:
    print("Address not found.")
