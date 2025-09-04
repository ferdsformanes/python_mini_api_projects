# Python Attributes vs Methods Explained with `requests` Response Object!

import requests
import urllib3

# Suppress SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Make a request to download a sample text file (Romeo and Juliet)
response = requests.get('https://automatetheboringstuff.com/files/rj.txt', verify=False)

# SECTION 1: What is dir()?
# dir() lists all attributes (variables) and methods (functions) of an object.
print(dir(response))

# SECTION 2: Attributes - These are data stored in the object.
# You access them directly without parentheses.
print(response.status_code)  # Attribute: shows HTTP status code (e.g., 200)
print(response.text[:210])   # Attribute: shows first 210 characters of response body
print(response.url)          # Attribute: shows final URL after redirects
print(response.headers["Content-Type"])  # Attribute: shows content type of the response

# 🛠️ SECTION 3: Methods - These are functions that perform actions.
# You call them with parentheses.
for line in response.iter_lines(decode_unicode=True):  # Method: iterate line by line
    print(line)
    break  # just show the first line
response.raise_for_status()  # Method: raises error if status code is not OK

# SECTION 4: How to tell attributes from methods
# callable(obj) → returns True if obj can be called like a function (i.e., it's a method)
print(callable(response.status_code))   # False → it's an attribute
print(callable(response.iter_lines))    # True → it's a method

# You can also print them to inspect
print(response.status_code)   # Just prints the value
print(response.iter_lines)    # Shows it's a bound method object

# SECTION 5: Real-world use case combining attributes and methods
if response.status_code == requests.codes.ok: 
    data = response.text
    print(data[:210])      
