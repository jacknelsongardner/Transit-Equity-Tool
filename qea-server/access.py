from score import calculate_score

walkable_dist = 10

def calculate_access(stopsCount, stops, dists):
    
    stopCount = sum(stopsCount)
    
    # Check if any of the lists are empty to avoid division by zero
    if not stopCount or not stops or not dists:
        raise ValueError("One or more input lists are empty.")

    

    # Calculate the average for each list
    average_stopCount = sum(stopCount) / len(stopCount)
    average_stops = sum(stops) / len(stops)
    average_dists = sum(dists) / len(dists)

    

    stop_weight = 5
    stopCount_weight = 4
    dist_weight = 2

    total_weight = stop_weight + stopCount_weight + dist_weight

    stop_weight = stop_weight/total_weight
    stopCount_weight = stopCount_weight/total_weight
    dist_weight = dist_weight/total_weight


    # PEOPLES SCORES 
    stopsList = [0, 3, 6, 10]
    stopCountList = [0, 25, 50, 100]
    distList = [0, .1, .25, .5]

    output = calculate_score(vals=[average_stops, average_dists, average_stopCount], 
                    weights=[stop_weight, dist_weight, stopCount_weight], 
                    trainSets=[stopsList, distList, stopCountList],
                    names=['stops', 'distance', 'stopCount'])

    return output

if __name__ == "__main__":
    result = calculate_access([50,25],[4,2],[.3,.4])
    avg_stops = result['stops']['val']
    stop_weight = result['stops']['weight']

    avg_stops = result['distance']['val']
    stop_weight = result['distance']['weight']

    avg_stops = result['stopCount']['val']
    stop_weight = result['stopCount']['weight']











