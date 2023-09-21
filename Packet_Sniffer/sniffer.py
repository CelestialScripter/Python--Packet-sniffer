import argparse
import os
from core import PacketSniffer
from output import OutputToScreen

def parse_arguments():
    parser = argparse.ArgumentParser(description="Network packet sniffer")
    parser.add_argument(
        "-i", "--interface",
        type=str,
        default=None,
        help="Interface from which Ethernet frames will be captured (monitors "
             "all available interfaces by default)."
    )
    parser.add_argument(
        "-d", "--data",
        action="store_true",
        help="Output packet data during capture."
    )
    return parser.parse_args()

def check_permissions():
    if os.getuid() != 0:
        raise SystemExit("Error: Permission denied. This application requires "
                         "administrator privileges to run.")

def main():
    args = parse_arguments()
    check_permissions()

    sniffer = PacketSniffer()
    OutputToScreen(subject=sniffer, display_data=args.data)

    try:
        for _ in sniffer.listen(args.interface):
            # Iterate through the frames yielded by the listener
            pass
    except KeyboardInterrupt:
        raise SystemExit("[!] Aborting packet capture...")

if __name__ == "__main__":
    main()
