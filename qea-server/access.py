from score import calculate_score, log_normalize
from geo import *

walkable_dist = 10


def access_by_address(address):
    
    coordinates = get_coordinates(address)
    address = get_address(coordinates)

    stops, distances = get_nearby_stops(coordinates)
    counts = get_bus_counts(stops)

    routes = get_unique_routes_for_stops(stops)

    

    result = calculate_access(counts, stops, distances, routes)
    return result


def calculate_access(stopCounts, stops, dists, routes):
    # Check if any of the lists are empty to avoid division by zero
   

    stop_weight = 5
    stopCount_weight = 4
    routes_weight = 3
    total_weight = stop_weight + stopCount_weight + routes_weight

    stop_weight = stop_weight/total_weight
    stopCount_weight = stopCount_weight/total_weight
    routes_weight = routes_weight/total_weight

    # Distance values determine 
    distNorm = [.1,.25,.5]
    
    distFunc = log_normalize(distNorm)
    
    adjustedDists = [round(1 - distFunc(dist), 2) for dist in dists]
   


    # Values adjusted by 
    adjustedStops = [adjustedDists[index] * 1 for index in range(len(adjustedDists))]
    adjustedRoutes = [adjustedDists[index] * routes[index] for index in range(len(adjustedDists))]
    adjustedStopCounts = [adjustedDists[index] * int(stopCounts[index]) for index in range(len(adjustedDists))]
    
    print(dists)
    print(adjustedDists)

    print(adjustedStops)
    print(adjustedRoutes)
    print(adjustedStopCounts)



    # PEOPLES SCORES 
    stopsList = [1, 30, 60, 120]
    stopCountList = [1, 100, 400, 800]
    routesList = [1, 100, 200, 400]

    output = calculate_score(vals=[sum(adjustedDists), sum(adjustedStops), sum(adjustedRoutes)], 
                    weights=[stop_weight, stopCount_weight, routes_weight], 
                    trainSets=[stopsList, stopCountList, routesList ],
                    names=['stops', 'stopCount', 'routes'])

    return output

if __name__ == "__main__":


    output = access_by_address('8905 19th pl SE, Lake Stevens, WA 98258')
    print(output)

















