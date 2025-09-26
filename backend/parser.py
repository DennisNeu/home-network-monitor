import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Network Scanner")
        self.parser.add_argument("--scan", action="store_true", help="Scan the network for devices")
        self.parser.add_argument("--list", action="store_true", help="List saved devices")
        self.parser.add_argument("--clear", action="store_true", help="Clear saved devices")
        self.parser.add_argument("--name", type=str, help="Add a name to a device by IP")

    def parse(self, args=None):
        return self.parser.parse_args(args)