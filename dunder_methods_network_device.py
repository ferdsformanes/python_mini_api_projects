# Python Dunder Methods for Network Automation
from netmiko import ConnectHandler

class NetworkDevice:
    def __init__(self, hostname, ip, username, password):
        self.hostname = hostname
        self.ip = ip
        self.username = username
        self.password = password

    # __str__ → defines how the object is printed (user-friendly)
    def __str__(self):
        return f"{self.hostname} ({self.ip})"

    # __repr__ → unambiguous representation, useful for debugging
    def __repr__(self):
        return (f"NetworkDevice(hostname='{self.hostname}', ip='{self.ip}')")

    # __len__ → lets us use len() on the object
    def __len__(self):
        return len(self.hostname)

    # __call__ → makes the object callable like a function (runs a command)
    def __call__(self, command):
        device = {
            "device_type": "cisco_ios_telnet",  # Using Telnet
            "host": self.ip,
            "username": self.username,
            "password": self.password,
        }
        try:
            with ConnectHandler(**device) as net_connect:
                return net_connect.send_command(command)
        except Exception as e:
            return f"Failed to run command: {e}"

    # Regular method for comparison
    def run_command(self, command):
        device = {
            "device_type": "cisco_ios_telnet",  # Using Telnet
            "host": self.ip,
            "username": self.username,
            "password": self.password,
        }
        with ConnectHandler(**device) as net_connect:
            return net_connect.send_command(command)


# --- Example Usage ---
cisco = NetworkDevice("route-views.routeviews.org", "128.223.51.103", "rviews", "rviews")

print("Calling object directly with __call__:")
print(cisco("show version"))      # Looks like calling a function (thanks to __call__)

# Uncomment to compare with normal method call
# print("\nCalling explicit method without __call__:")
# print(cisco.run_command("show version"))   # Using regular method instead

print("\nUsing __str__ method:")
print(cisco)                      # Prints user-friendly string (hostname + IP)

print("\nUsing __repr__ method:")
print(repr(cisco))                # Prints debug-friendly string (class + attributes)

print("\nUsing __len__ method:")
print(f"Hostname length = {len(cisco)}")  # len() now works → length of hostname
