import ipaddress

ip_addresses = ["192.168.1.2", "192.168.1.5", "192.168.1.1", "192.168.1.3", "192.168.1.4"]
max_ip = ipaddress.IPv4Address('0.0.0.0')
min_ip = ipaddress.IPv4Address('255.255.255.255')

for ip in ip_addresses:
    ip_bin = ipaddress.IPv4Address(ip)
    max_ip = max(max_ip,ip_bin)
    min_ip = min(min_ip,ip_bin)


max_ip_binary = bin(int(max_ip))[2:].zfill(32)
min_ip_bin = bin(int(min_ip))[2:].zfill(32)

max_l = 0
print(max_ip_binary)
print(min_ip_bin)
print(max_ip_binary>min_ip_bin)
for i in range(32):
    if max_ip_binary[i]!=min_ip_bin[i]:
        max_l = i
        break
l = []
for i in range(max_l):
    l.append(min_ip_bin[i])

for i in range(max_l,32):
    l.append('0')
res = ''.join(l)
decimal_address = int(res, 2)  # Convert binary to decimal
ip_address = ipaddress.IPv4Address(decimal_address)  # Convert decimal to IP address
ip_address = str(ip_address)+"/"+str(max_l)
print(ip_address)
