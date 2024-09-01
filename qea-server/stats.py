import numpy as np

def log_normalize(values, min_value=1, max_score=100):
    """
    Normalize a list of values to a logarithmic scale between 0 and max_score.

    Parameters:
    - values: List or array of numerical values to normalize.
    - min_value: Minimum value for logarithmic scaling. (values <= min_value are set to min_value)
    - max_score: Maximum score to map to.

    Returns:
    - List of normalized values between 0 and max_score.
    """
    values = np.array(values)
    # To avoid log(0) and log(negative values), ensure all values are >= min_value
    values = np.clip(values, min_value, None)
    
    # Apply logarithmic transformation
    log_values = np.log(values)
    
    # Normalize log values to a 0-1 range
    log_min = np.log(min_value)
    log_max = np.log(np.max(values))
    normalized_values = (log_values - log_min) / (log_max - log_min)
    
    # Scale to 0-max_score range
    scaled_values = normalized_values * max_score
    
    return scaled_values.tolist()

# Example usage:
transit_scores = [10, 100, 1000, 10000]
normalized_scores = log_normalize(transit_scores)
print(normalized_scores)
