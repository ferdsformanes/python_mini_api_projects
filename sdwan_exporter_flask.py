
# sdwan_exporter_flask.py
from flask import Flask, Response
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco SD-WAN Sandbox credentials
HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

app = Flask(__name__)

# Create session and login once
session = requests.Session()
login_url = f"{HOST}/j_security_check"
payload = {"j_username": USERNAME, "j_password": PASSWORD}
resp = session.post(login_url, data=payload, verify=False)

if resp.status_code != 200 or "JSESSIONID" not in session.cookies:
    raise Exception("Login failed!")

print("JSESSIONID", session.cookies.get("JSESSIONID"))
print("Logged in successfully")

@app.route("/metrics")
def metrics():
    try:
        # Retrieve device list
        devices_url = f"{HOST}/dataservice/device"
        resp = session.get(devices_url, verify=False)
        if resp.status_code != 200:
            raise Exception(f"Failed to retrieve devices: {resp.status_code}, {resp.text}")
        devices = resp.json().get("data", [])
        
        # Count all devices
        up_count = len(devices)
        
        # Prometheus metric format
        output = f"# HELP sdwan_devices_up Number of SD-WAN devices\n"
        output += f"# TYPE sdwan_devices_up gauge\n"
        output += f"sdwan_devices_up {up_count}\n"
    except Exception as e:
        output = f"# Error: {str(e)}"
    return Response(output, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
