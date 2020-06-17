# 1/bin/python3

# building a script to scan systems and need to import socket and sys
import socket
import sys
from datetime import datetime

# define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translating an hostname to ipv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 pscanner.py <ip>")
# you'll get an argument error if you don't put an argument in <ip> when you run python3 pscanner.py

# adds a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try: # PyCharm showed tabs in used throughout entire try block, replaced tabs with spaces and it ran prompting script error
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex(target, port) # too many parenthesis
        # print("Checking port {}.".format(port)) # Py2 syntax
        print(f'Checking port {port}') # Py3 syntax

        if result == 0:
            # print("Port {} is open".format(port)) # Py2 syntax
            print(f'Port {port} is open') # Py3 syntax

        s.close() #there was an extra space in front of this close

except KeyboardInterrupt
    print("\nExiting program.")
except socket.gaierror:
    print("Hostname could not be resolved")
except socket.error:
    print("Couldn't connect to Server")
    sys.exit()
