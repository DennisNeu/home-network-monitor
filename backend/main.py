from scapy.all import ARP, Ether, srp
from datahandler import DataHandler

data_handler = DataHandler("data.json")

TARGET_IP = "10.159.134.0/24"  # adjust to your subnet
arp = ARP(pdst=TARGET_IP)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

for d in devices:
    print(d)
    name = input("Add name: ")
    d.update({'name': name}) # Its a dict

data_handler.save_data(devices)
