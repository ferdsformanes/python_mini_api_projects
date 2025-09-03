# 📺 VIDEO TITLE: Python Attributes vs Methods Explained with `requests` Response Object!

import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt', verify=False)

# 📦 SECTION 1: What is dir()?
# dir() lists all attributes and methods of an object.
print(dir(response))

# 🧠 SECTION 2: Attributes - These are data stored in the object.
# You access them directly without parentheses.
print(response.status_code)  # Attribute: shows HTTP status code (e.g., 200)
print(response.text[:210])   # Attribute: shows first 210 characters of response body
print(response.url)          # Attribute: shows final URL after redirects

# 🛠️ SECTION 3: Methods - These are functions that perform actions.
# You call them with parentheses.
print(response.json())           # Method: parses response body as JSON
response.raise_for_status()      # Method: raises error if status code is not OK

# 🔍 SECTION 4: How to tell attributes from methods
# Use callable() to check if it's a method (returns True)
print(callable(response.status_code))  # False → it's an attribute
print(callable(response.json))         # True → it's a method

# You can also print them to inspect
print(response.status_code)  # Just prints the value
print(response.json)         # Shows it's a bound method

# 🧪 SECTION 5: Real-world use case combining attributes and methods
if response.status_code == requests.codes.ok:  # requests.codes.ok is a constant for 200
    data = response.json()                     # Use method to parse JSON
    print(data)