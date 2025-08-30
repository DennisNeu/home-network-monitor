from scapy.all import ARP, Ether, srp
from datahandler import Datahandler

data_handler = Datahandler("data.json")

target_ip = "10.159.134.0/24"  # adjust to your subnet
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

for d in devices:
    print(d)
    name = input("Add name: ")
    d.update({'name': name})

data_handler.save_data(devices)
