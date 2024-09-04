from score import calculate_score

walkable_dist = 10

def calculate_access(stops, routes, dists):
    
    stops_weight = 5
    routes_weight = 4
    dist_weight = 2


    adjusted_stops = stops

    total_weight = routes_weight + stops_weight + dist_weight

    stops_weight = stops_weight/total_weight
    routes_weight = routes_weight/total_weight
    dist_weight = dist_weight/total_weight

    


    # PEOPLES SCORES 
    routesList = [0, ]
    stopList = [0, 25, 50, 100]
    distList = [10, 5, 2.5, 0]

    output = calculate_score(vals=[routes, dists, stops], 
                    weights=[routes_weight, dist_weight, stops_weight], 
                    trainSets=[routesList, distList, stopList],
                    names=['routes', 'distance', 'stops'])

    return output

if __name__ == "__main__":
    calculate_access(100, 4, )











