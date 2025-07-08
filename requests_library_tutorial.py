# Learn Python Requests with Real APIs 

# ----------------------------------------
# OpenWeatherMap API – Get Current Weather
# ----------------------------------------

import requests
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
lat = 14.554729
lon = 121.024445

# Add units=metric to get temperature in Celsius
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(type(data))
    print(f"Weather in {data['name']}, {data['sys']['country']}: {data['weather'][0]['description']} | Temp: {data['main']['temp']}°C")
else:
    print("Error:", response.status_code, response.text)

# ----------------------------------------
# POST Request with Form Data – httpbin.org
# ----------------------------------------
import requests
import json
payload = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Sends a POST request with form-encoded data
# The 'Content-Type' header is automatically set to 'application/x-www-form-urlencoded'
r = requests.post('https://httpbin.org/post', data=payload, timeout=5)
data = r.json()
data.pop("origin", None)  # Remove IP
print(json.dumps(data, indent=2))

# ----------------------------------------
# POST Request with JSON Payload – httpbin.org
# ----------------------------------------
import requests
import json
json_payload = {"username": "admin", "password": "1234"}
# Sends a POST request with JSON data
# The Content-Type header will be automatically set to 'application/json'
r = requests.post('https://httpbin.org/post', json=json_payload, timeout=5)
data = r.json()
data.pop("origin", None)  # Remove IP
print(json.dumps(data, indent=2))

# ----------------------------------------
# GET Request with Query Parameters – httpbin.org
# ----------------------------------------
import requests
import json
params_payload = {
    "search": "weather",
    "city": "manila"
}
r = requests.get('https://httpbin.org/get', params=params_payload, timeout=5)
data = r.json()
data.pop("origin", None)  # Remove IP
print(json.dumps(data, indent=2))

# ----------------------------------------
# Error Handling Example – CurrencyFreaks with Wrong Key
# ----------------------------------------
import requests
import json
bad_key = "invalid_key"
url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={bad_key}"

response = requests.get(url)
if response.status_code != 200:
    print("Failed to get exchange rates:", response.status_code)

# # ----------------------------------------
# # Tips and Best Practices
# # ----------------------------------------

# # Always handle status codes.
# # Use timeout= to prevent hanging requests.
# # Use .json() only when the content type is application/json.
# # Never hardcode secrets — use environment variables or config files.
# # For better stability, use try-except blocks in production.