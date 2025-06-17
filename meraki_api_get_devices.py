import requests
import pandas as pd

# Your API key
API_KEY = ''  # Replace with your actual API key
# Organization ID
ORG_ID = 'YOUR_ORG_ID_HERE'  # Replace with your actual organization ID

# Base URL for Meraki API
url = f'https://api.meraki.com/api/v1/organizations/{ORG_ID}/devices'

# Headers including the API key
headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

# Make the API request
try:
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()  # Raise an error for bad status codes

    # Convert response to JSON
    devices = response.json()

    # Convert JSON to DataFrame
    df = pd.DataFrame(devices)

    # Output total number of devices
    total_devices = len(df)
    print(f"Total number of devices: {total_devices}")

    # Save DataFrame to CSV
    output_file = 'meraki_devices.csv'
    df.to_csv(output_file, index=False)
    print(f"Devices list saved to {output_file}")

except requests.exceptions.SSLError as e:
    print(f"SSLError: {e}")
except requests.exceptions.RequestException as e:
    print(f"HTTP Request Error: {e}")
