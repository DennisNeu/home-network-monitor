from scapy.all import ARP, Ether, srp
from datahandler import DataHandler
import argparse

data_handler = DataHandler("data.json")

def network_scan():
    """Function scans network with arp and returns list of found clients"""
    TARGET_IP = "10.159.134.0/24"  # adjust to your subnet
    arp = ARP(pdst=TARGET_IP)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    return srp(packet, timeout=3, verbose=0)[0]

result = network_scan()

print(result)

# Populate list
devices = []

# Maybe change data structure to a dict with ip as key and list as value"
# Dont know why this works
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

for d in devices:
    print(d)
   # name = input("Add name: ")
   # d.update({'name': name}) # Its a dict

data_handler.save_data(devices)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--scan", action="store_true", help="Scan the network for devices")
    parser.add_argument("--list", action="store_true", help="List saved devices")
    parser.add_argument("--clear", action="store_true", help="Clear saved devices")
    parser.add_argument("--name", type=str, help="Add a name to a device by IP")
    args = parser.parse_args()

    if args.scan:
        scanned_devices = network_scan()
        devices = []
        for sent, received in scanned_devices:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        data_handler.save_data(devices)
        print("Scan complete. Devices saved to data.json.")

    if args.clear:
        data_handler.delete_data()
        print("Saved devices cleared.")