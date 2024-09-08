from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import requests
import psycopg2


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

    print(response.json())

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



transit_conn = psycopg2.connect(
    dbname='transit_db',
    user='jack',
    password='xfiles',
    host='localhost',
    port='5432'
)

demo_conn = psycopg2.connect(
    dbname='demographic_info',
    user='jack',
    password='xfiles',
    host='localhost',
    port='5432'
)


# Create a cursor object
cur = demo_conn.cursor()

# Function to get values from geo_info table for a specific geo_id
def get_demographic_info(geo_id, year):
    year = str(year)

    query = """
        SELECT Household_Income_by_Race, avg_cars_per_person, avg_persons_per_household
        FROM geo_info
        WHERE ID_Geography = %s AND Year = %s
        LIMIT 1;
    """
    cur.execute(query, (geo_id, year))
    result = cur.fetchone()

    income = 54632 # average income for WA
    cars = 3 # average cars per household for WA
    persons = 3 # average people per household for WA

    if result:
        income = int(result[0])
        cars = float(result[1])
        persons = float(result[2])

    return income, cars, persons

from math import radians, cos, sin, asin, sqrt

# Haversine formula to calculate distance between two lat/lon pairs
def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    
    # Radius of Earth in miles (3956 miles)
    miles = 3956 * c
    return miles

# Calculate the bounding box (lat/lon range) for a given distance
def calculate_bounding_box(lat, lon, distance_miles=1):
    # Convert miles to degrees of latitude and longitude
    miles_per_degree_lat = 69.0  # Approximate miles per degree of latitude
    miles_per_degree_lon = 69.0 * cos(radians(lat))  # Longitude depends on latitude

    lat_diff = distance_miles / miles_per_degree_lat
    lon_diff = distance_miles / miles_per_degree_lon

    # Return the bounding box as (min_lat, max_lat, min_lon, max_lon)
    return lat - lat_diff, lat + lat_diff, lon - lon_diff, lon + lon_diff


# Method to get stops within 0.5 miles of input coordinates
def get_nearby_stops(coordinates):
    cursor = transit_conn.cursor()
    try:
        input_lat, input_lon = coordinates
        # Calculate the bounding box for 0.5 miles
        min_lat, max_lat, min_lon, max_lon = calculate_bounding_box(input_lat, input_lon)
        
        # Query to get stops within the bounding box
        
        cursor.execute("""
            SELECT stop_id, stop_name, stop_lat, stop_lon 
            FROM transit_stops
            WHERE stop_lat BETWEEN %s AND %s
            AND stop_lon BETWEEN %s AND %s;
            """, (min_lat, max_lat, min_lon, max_lon))
        
        stops = cursor.fetchall()
        
        nearby_stops = []
        nearby_distances = []

        for stop in stops:
            stop_id, stop_name, stop_lat, stop_lon = stop
            distance = haversine(input_lat, input_lon, stop_lat, stop_lon)
            
            # If the distance is less than 0.5 miles, add the stop to the result
            if distance <= 0.5:
                nearby_stops.append(stop_id)
                nearby_distances.append(distance)
                
                '''
                 nearby_stops.append({
                    'stop_id': stop_id,
                    'stop_name': stop_name,
                    'stop_lat': stop_lat,
                    'stop_lon': stop_lon,
                    'distance_miles': distance
                })
                '''
               
        
        return nearby_stops, nearby_distances
    
    except Exception as e:
        print(f"Error fetching stops: {e}")
        return []
    finally:
        cursor.close()

def get_bus_counts(stop_ids):
    # Connect to your PostgreSQL database
    
    cursor = transit_conn.cursor()

    # Prepare a dictionary to store stop_id and their bus counts
    bus_counts = []

    for stop_id in stop_ids:
        # Query to count the number of buses at a given stop_id
        query = """
        SELECT COUNT(DISTINCT trip_id) 
        FROM transit_stop_times 
        WHERE stop_id = %s;
        """
        cursor.execute(query, (stop_id,))
        count = cursor.fetchone()[0]
        bus_counts.append(count)

    # Close the cursor and connection
    cursor.close()

    return bus_counts


def get_unique_routes_for_stops(stop_ids):
    """
    Get the number of unique routes for multiple stop_ids.

    :param stop_ids: A list of stop_ids to query.
    :return: A dictionary where the keys are stop_ids and the values are the count of unique routes.
    """
    
    
    cur = transit_conn.cursor()
    try:
        # Define the query
        query = """
            SELECT stop_id, COUNT(DISTINCT route_id) AS unique_routes_count
            FROM transit_stop_times
            JOIN transit_trips ON transit_stop_times.trip_id = transit_trips.trip_id
            WHERE stop_id = ANY(%s)
            GROUP BY stop_id
        """
        
        # Execute the query
        cur.execute(query, (stop_ids,))
        
        # Fetch all results
        results = cur.fetchall()
        
        # Organize the results into a dictionary
        routes_count = [count for stop_id, count in results]
        
        return routes_count
        
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return None
        
    finally:
        # Close the cursor and connection
        cur.close()

if __name__ == "__main__":
    coordinates = get_coordinates('8905 19th pl SE, Lake Stevens, WA 98258')
    geoCode = get_geoCode(coordinates=coordinates)

    print(coordinates)
    print(get_address(coordinates))
    print(geoCode)
    print(get_demographic_info(geoCode, 2022))



    stops, distances = get_nearby_stops(coordinates)
    counts = get_bus_counts(stops)

    routes = get_unique_routes_for_stops(stops)

    print(stops)
    print(distances)
    print(counts)
    print(routes)
