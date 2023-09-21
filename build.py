import PyInstaller.__main__ as pyinstaller
import argparse

def build_packet_sniffer_binary():
    """Build the Network Packet Sniffer binary using PyInstaller."""
    parser = argparse.ArgumentParser(description="Build the Packet Sniffer binary.")
    parser.add_argument(
        "--onefile", action="store_true", help="Build a single executable file."
    )
    args = parser.parse_args()

    build_args = ["packet_sniffer/core.py"]
    if args.onefile:
        build_args.append("--onefile")

    pyinstaller.run(build_args)

if __name__ == "__main__":
    build_packet_sniffer_binary()
