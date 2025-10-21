import requests
import urllib3

# Ignore SSL warnings for the sandbox (self-signed certs)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Sandbox credentials
HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

# Create a requests session
session = requests.Session()

# Step 1: Login and get JSESSIONID
login_url = f"{HOST}/j_security_check"
payload = {"j_username": USERNAME, "j_password": PASSWORD}
resp = session.post(login_url, data=payload, verify=False)

if resp.status_code != 200 or "JSESSIONID" not in session.cookies:
    raise Exception("Login failed!")

print("JSESSIONID", session.cookies.get("JSESSIONID"))

print("Logged in successfully")

# Step 2: Retrieve device list
devices_url = f"{HOST}/dataservice/device"
resp = session.get(devices_url, verify=False)

if resp.status_code != 200:
    raise Exception(f"Failed to retrieve devices: {resp.status_code}, {resp.text}")

devices = resp.json()

# Print all top-level keys in the JSON response
print(devices.keys())

print("Retrieved devices:")
for d in devices["data"]:
    print(f"- {d['host-name']}, ({d['deviceId']})")
