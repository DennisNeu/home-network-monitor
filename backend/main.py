from scapy.all import ARP, Ether, srp
from datahandler import DataHandler
import argparse

data_handler = DataHandler("data.json")
TARGET_IP = "192.168.178.0/24"  # adjust to your subnet

def network_scan():
    """Function scans network with arp and returns list of found clients"""
    arp = ARP(pdst=TARGET_IP)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    return srp(packet, timeout=3, verbose=0)[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--scan", action="store_true", help="Scan the network for devices")
    parser.add_argument("--list", action="store_true", help="List saved devices")
    parser.add_argument("--clear", action="store_true", help="Clear saved devices")
    parser.add_argument("--name", type=str, help="Add a name to a device by IP")
    args = parser.parse_args()

    if args.scan:
        scanned_devices = network_scan()
        network = []
        devices = []
        for sent, received in scanned_devices:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        entry = {"ip": TARGET_IP, "devices": devices}
        network.append(entry)
        data_handler.save_data(network)
        print("Scan complete. Devices saved to data.json.")

    if args.clear:
        data_handler.delete_data()
        print("Saved devices cleared.")

    if args.list:
        saved_devices = data_handler.load_data()
        if not saved_devices:
            print("No devices found.")
        else:
            for device in saved_devices:
                print(device)
            print("total devices found:", len(saved_devices))        