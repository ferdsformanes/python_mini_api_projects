# Lookup Any IP Address Using Requests and ipwhois.io

import requests

def lookup_ip(ip_address: str):
    url = f"https://ipwhois.app/json/{ip_address}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("success", True):
            print(f"IP: {data.get('ip')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Organization: {data.get('org')}")
            print(f"Country: {data.get('country')}")
            print(f"ASN: {data.get('asn')}")
        else:
            print(f"Lookup failed: {data.get('message', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    ip = input("Enter a public IP address: ").strip()
    lookup_ip(ip)
