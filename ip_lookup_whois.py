import requests

def lookup_ip(ip_address: str):
    """Query ipwhois.io for details about an IP address."""
    url = f"https://ipwhois.app/json/{ip_address}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print(data.keys())

    if data.get("success", True):  # ipwhois.io returns success=False if invalid
        print("IP:", data.get("ip"))
        print("Country:", data.get("country"))
        print("ISP:", data.get("isp"))
        print("ASN:", data.get("asn"))
        print("Organization:", data.get("org"))
    else:
        print(f"Lookup failed: {data.get('message', 'Unknown error')}")

    
if __name__ == "__main__":
    ip = input("Enter a public IP address: ").strip()
    lookup_ip(ip)

# invalid ip: 999.999.999.999