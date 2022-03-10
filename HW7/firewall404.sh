#!/bin/sh

# 1. Removing all previous rules or chains
sudo iptables -t filter -F
sudo iptables -t filter -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t raw -F
sudo iptables -t raw -X

# 2. Changing source IP address of all outgoing packets to my own IP
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# 3. Blocking a list of IP addresses coming from yahoo.com
sudo iptables -A INPUT -s 98.137.11.163 -j DROP
sudo iptables -A INPUT -s 98.137.11.164 -j DROP
sudo iptables -A INPUT -s 74.6.231.20 -j DROP
sudo iptables -A INPUT -s 74.6.231.21 -j DROP
sudo iptables -A INPUT -s 74.6.143.25 -j DROP
sudo iptables -A INPUT -s 74.6.143.26 -j DROP

# 4. Blocking my computer from being pinged by other hosts
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

# 5. Setting up  Port forwarding from port 4040 to port 22 (for tcp or udp)
# to test, enable connections to port 4040
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 4040 -j REDIRECT --to-port 22
sudo iptables -t nat -A PREROUTING -i eth0 -p udp --dport 4040 -j REDIRECT --to-port 22

# 6. Allowing SSH access only from machines in the engineering.purdue.edu domain
# block all connections first, then allowing those from engineering.purdue.edu domain
sudo iptables -A INPUT -p tcp --dport ssh -j DROP
sudo iptables -A INPUT -p tcp --dport ssh -s 128.46.104.5 -j ACCEPT

# 7. Rule for only allowing a single IP address on the internet to access machine
sudo iptables -A INPUT -p tcp --dport http -j DROP
sudo iptables -A INPUT -p tcp --dport http -s 128.46.104.5 -j ACCEPT

# 8. Permit Auth/Ident (port 113) that's used by services like SMTP and IRC
sudo iptables -A INPUT -p tcp --dport 113 -j ACCEPT