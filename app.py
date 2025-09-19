import socket
x = "Hello, World!"

print(x)

hostname = socket.gethostname()
print(f"Hostname: {hostname}")

IPadd= socket.gethostbyname(hostname)
print(f"IP Address: {IPadd}")