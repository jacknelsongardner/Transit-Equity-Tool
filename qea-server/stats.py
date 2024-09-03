import numpy as np

def log_normalize(values, min_value=1):
    """
    Normalize a list of values to a logarithmic scale between 0 and 1.

    Parameters:
    - values: List or array of numerical values to normalize.
    - min_value: Minimum value for logarithmic scaling. (values <= min_value are set to min_value)

    Returns:
    - A function that normalizes input values based on the original list.
    """
    values = np.array(values)
    values = np.clip(values, min_value, None)
    
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
        else: return transformed_value

    
    return transform

# Example usage:

if __name__ == "__main__":
        
    transit_scores = [10, 100, 1000, 10000]
    normalizeFunc = log_normalize(transit_scores)

    input = 11000
    output = normalizeFunc(input)
    print(output)
