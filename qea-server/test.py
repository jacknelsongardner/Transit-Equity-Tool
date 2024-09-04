import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '65c51cf9f2bb0ada0f12630911da0e9dbcbb959b'

# Define the endpoint and parameters
endpoint = 'https://api.census.gov/data/2019/acs/acs5'
params = {
    'get': 'B11002_001E,B25044_001E',  # Average household size and average vehicles per household
    'for': 'county:53061',  # Snohomish County FIPS code
    'key': api_key
}

# Make the API request
response = requests.get(endpoint, params=params)

print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")


print('sent response')
data = response.json()

# Print the data
print(data)
