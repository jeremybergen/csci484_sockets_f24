from scapy.all import *

packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.5.1/24")

ans, unans = srp(packet, iface="VMware Network Adapter VMnet1", timeout=2)

print(f"ans: {ans.show()}")
# ip = IP(dst="192.168.0.1")
# tcp = TCP(sport=RandShort(), dport=[22, 80], seq=12345, ack=1000, window=1000, flags="S")
# raw = Raw(b"X" * 1024)

# p = ip/tcp/raw

# print(f"{p}")