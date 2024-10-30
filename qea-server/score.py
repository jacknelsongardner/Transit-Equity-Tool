import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import math



def log_normalize(values):
    
    
    
    # Replace zero values with a small number
    values = np.array([max(value, 1e-10) for value in values])  # Using a safer small value
    
    min_value = np.min(values)
    max_value = np.max(values)
    
    # Log transform the values
    log_values = np.log(values)
    
    # Get the min and max log values
    log_min = np.min(log_values)
    log_max = np.max(log_values)
    
    # Avoid division by very small numbers
    log_range = log_max - log_min
    if log_range == 0:
        log_range = 1  # Fallback to prevent division by zero
    
    # Return a function that normalizes any given value
    def transform(value):
        log_value = np.log(np.array([max(value, min_value)]))
        log_min_value = np.log(np.array([min_value]))
        log_max_value = np.log(np.array([max_value]))

        transformed_value = (log_value - log_min) / (log_max_value - log_min_value)
        return max(0, min(transformed_value, 1))  # Ensure the value stays within [0, 1]

    return transform


def calculate_score(vals, weights, trainSets, names):

    output = {}

    adjustedVals = []
    
    adjustedTotal = 0




    for index in range(len(vals)):
        val = vals[index]
        weight = weights[index]
        train = trainSets[index]
        name = names[index]

        logFunc = log_normalize(train)
        logVal = logFunc(val)

        adjustedVals.append(logVal)
        output[name] = {'score':round(logVal*100, 0), 'metric weight':round(weight*10, 1), 'normalized value':val, 'log function max':max(train), 'log function min':min(train)}

    for index in range(len(adjustedVals)):
        adjustedTotal += adjustedVals[index] * weights[index]

    output['score'] = round(adjustedTotal * 100, 0)

    return output


# Example usage:

if __name__ == "__main__":
        

    transit_scores = [1, 100, 1000, 10000]
    normalizeFunc = log_normalize(transit_scores)

    

    input = 10
    output = normalizeFunc(input)
    print(output)

    input = 110
    output = normalizeFunc(input)
    print(output)

    input = 1100
    output = normalizeFunc(input)
    print(output)

    input = 1100000
    output = normalizeFunc(input)
    print(output)
