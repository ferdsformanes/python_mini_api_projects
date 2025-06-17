import requests

# Your API key
API_KEY = ''

# Correct base URL for Meraki API
url = 'https://api.meraki.com/api/v1/organizations'

# Headers including the API key
headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

# Disable SSL certificate verification
try:
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an error for bad status codes

    organizations = response.json()
    
    # Print the organization names and IDs
    for org in organizations:
        print(f"Organization Name: {org['name']}, Organization ID: {org['id']}")
except requests.exceptions.SSLError as e:
    print(f"SSLError: {e}")
except requests.exceptions.RequestException as e:
    print(f"HTTP Request Error: {e}")
