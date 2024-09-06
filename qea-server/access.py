from score import calculate_score
from geo import *

walkable_dist = 10


def access_by_address(address):
    
    coordinates = get_coordinates(address)
    
    print(coordinates)
    print(get_address(coordinates))

    stops, distances = get_nearby_stops(coordinates)
    counts = get_bus_counts(stops)

    routes = get_unique_routes_for_stops(stops)

    print(stops)
    print(distances)
    print(counts)
    print(routes)

    result = calculate_access(stops, distances, counts, routes)
    return result


def calculate_access(stopCount, stops, dists, routes):
    # Check if any of the lists are empty to avoid division by zero
    


    # Calculate the average for each list
    

    average_dists = 0

    if dists != [] and dists != {}:
        average_dists = sum(dists) / len(dists)
   


    

    stop_weight = 5
    stopCount_weight = 4
    dist_weight = 2
    routes_weight = 3

    total_weight = stop_weight + stopCount_weight + dist_weight + routes_weight

    stop_weight = stop_weight/total_weight
    stopCount_weight = stopCount_weight/total_weight
    dist_weight = dist_weight/total_weight
    routes_weight = routes_weight/total_weight



    # PEOPLES SCORES 
    stopsList = [0, 30, 60, 120]
    stopCountList = [0, 100, 400, 800]
    distList = [0, .1, .25, .5]
    routesList = [0, 100, 200, 400]

    output = calculate_score(vals=[sum(int(value) for value in stopCount), average_dists, len(stops), len(routes)], 
                    weights=[stop_weight, dist_weight, stopCount_weight, routes_weight], 
                    trainSets=[stopsList, distList, stopCountList, routesList ],
                    names=['stops', 'distance', 'stopCount', 'routes'])

    return output

if __name__ == "__main__":


    stops, distances, counts, routes = access_by_address('8905 19th pl SE, Lake Stevens, WA 98258')

    result = calculate_access(stops, distances, counts, routes)
    avg_stops = result['stops']['val']
    stop_weight = result['stops']['weight']

    distance = result['distance']['val']
    distance_weight = result['distance']['weight']

    routes = result['routes']['val']
    routes_weight = result['routes']['weight']

    numbusses = result['stopCount']['val']
    stop_weight = result['stopCount']['weight']

    print(result)

















