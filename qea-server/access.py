from score import calculate_score

walkable_dist = 10

def calculate_access(stopCount, stops, dists):
    
    stops_weight = 5
    stops_weight = 4
    dist_weight = 2


    adjusted_stops = stopCount

    total_weight = stops_weight + stops_weight + dist_weight

    stops_weight = stops_weight/total_weight
    stops_weight = stops_weight/total_weight
    dist_weight = dist_weight/total_weight

    


    # PEOPLES SCORES 
    stopsList = [0, 3, 6, 10]
    stopCountList = [0, 25, 50, 100]
    distList = [0, .1, .25, .5]

    output = calculate_score(vals=[stops, dists, stopCount], 
                    weights=[stops_weight, dist_weight, stops_weight], 
                    trainSets=[stopsList, distList, stopCountList],
                    names=['stops', 'distance', 'stopCount'])

    return output

if __name__ == "__main__":
    print(calculate_access([50],[4],[.3]))












