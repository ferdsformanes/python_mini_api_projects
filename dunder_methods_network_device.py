# Python Dunder Methods for Network Automation
# ------------------------------------------------------------------
# What are Dunder (Magic) Methods?
# ------------------------------------------------------------------
# Dunder methods are special methods in Python that start and end with
# double underscores, like __init__, __str__, __len__, etc.
#
# Why do we need them?
# - They let us customize how objects of our class behave with built-in
#   Python functions (like print(), len(), str(), repr()) or even make objects
#   act like functions (with __call__).
# - Without these, Python "falls back" to default behavior inherited
#   from the base 'object' class:
#     • __str__/__repr__ → shows <__main__.ClassName object at 0x...>
#     • __len__          → raises TypeError (no default available)
#     • __call__         → raises TypeError (not callable by default)
# ------------------------------------------------------------------

from netmiko import ConnectHandler

class NetworkDevice:
    def __init__(self, hostname, ip, username, password):
        self.hostname = hostname
        self.ip = ip
        self.username = username
        self.password = password

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

    # # Regular method for comparison
    # def run_command(self, command):
    #     device = {
    #         "device_type": "cisco_ios_telnet",  # Using Telnet
    #         "host": self.ip,
    #         "username": self.username,
    #         "password": self.password,
    #     }
    #     with ConnectHandler(**device) as net_connect:
    #         return net_connect.send_command(command)
        
    # # __str__ → defines how the object is printed (user-friendly)
    # def __str__(self):
    #     return f"{self.hostname} ({self.ip})"

    # # __repr__ → unambiguous representation, useful for debugging
    # def __repr__(self):
    #     return (f"NetworkDevice(hostname='{self.hostname}', ip='{self.ip}')")

    # # __len__ → lets us use len() on the object
    # def __len__(self):
    #     return len(self.hostname)

# Creating an object (instance of the class)
cisco = NetworkDevice("route-views.routeviews.org", "128.223.51.103", "rviews", "rviews")

# # -------------------- __call__ --------------------
# print("=== __call__ Example ===")
# print("With __call__:")
# print(cisco("show version"))      # Object acts like a function

# print("\nWithout __call__ (using normal method):")
# print(cisco.run_command("show version"))   # Must call method explicitly


# # -------------------- __str__ --------------------
# print("\n=== __str__ Example ===")
# print("With __str__:")
# print(cisco)                      # User-friendly string

# print("\nWithout __str__ (default fallback):")
# # If __str__ was not defined, print() falls back to object.__str__
# print(object.__str__(cisco))      # <__main__.NetworkDevice object at 0x...>


# # -------------------- __repr__ --------------------
# print("\n=== __repr__ Example ===")
# print("With __repr__:")
# print(repr(cisco))                # Debug-friendly string

# print("\nWithout __repr__ (default fallback):")
# # Falls back to object.__repr__
# print(object.__repr__(cisco))     # <__main__.NetworkDevice object at 0x...>


# # -------------------- __len__ --------------------
# print("\n=== __len__ Example ===")
# print("With __len__:")
# print(f"Hostname length = {len(cisco)}")  # Length of hostname

# print("\nWithout __len__ (would raise error):")
# try:
#     len(cisco)  # No __len__ in base object
# except Exception as e:
#     print(f"Error: {e}")
