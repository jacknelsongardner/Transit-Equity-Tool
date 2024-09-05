import numpy as np
import geopandas as gpd
from shapely.geometry import Point






def log_normalize(values):
    """
    Normalize a list of values to a logarithmic scale between 0 and 1.

    Parameters:
    - values: List or array of numerical values to normalize.
    - min_value: Minimum value for logarithmic scaling. (values <= min_value are set to min_value)

    Returns:
    - A function that normalizes input values based on the original list.
    """

    # checking for zeros
    for value in range(len(values)):
        if values[value] == 0:
            values[value] = .00000000000000001

    values = np.array(values)
            


    min_value = np.min(values)
    
    # Log transform the values
    log_values = np.log(values)
    
    
    # Get the min and max log values
    log_min = np.min(log_values)
    log_max = np.max(log_values)
    
    # Return a function that normalizes any given value
    def transform(value):
        log_value = np.log(max(value, min_value))
        transformed_value = (log_value - log_min) / (log_max - log_min)
        if transformed_value > 1:
            return 1
        elif transformed_value < 0:
            return 0
        else: return transformed_value

    
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
        output[name] = {'val':logVal,'weight':weight}

    for index in range(len(adjustedVals)):
        adjustedTotal += adjustedVals[index] * weights[index]

    output['total'] = adjustedTotal 

    return output


# Example usage:

if __name__ == "__main__":
        

    transit_scores = [0, 100, 1000, 10000]
    normalizeFunc = log_normalize(transit_scores)

    input = 11000
    output = normalizeFunc(input)
    print(output)
