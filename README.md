# Python 3 Network Packet Sniffer
"This is a Python 3 Network Packet Sniffer that dissects incoming packets at a specified network interface controller and presents their details on the screen.

This program relies solely on the [NETProtocols](https://github.com/EONRaider/NETProtocols) library and is compatible with any Python 3.8+ interpreter."

## Running the Application
### I. Development Mode
```
# Clone the repository
git clone https://github.com/CelestialScripter/Python--Packet-sniffer.git

# Navigate to the project directory
cd Python--Packet-sniffer

# Install the required dependencies using pip or poetry
# Using pip:
pip install -r requirements.txt

# OR using poetry:
# poetry install

# Run the packet sniffer script with superuser privileges
sudo python3 sniffer.py
```
### II. (Optional) Build the binary
Use the `build.py` file to compile your own binary with the `PyInstaller` package. You just need to install all dependencies and build. 
Dependency management works with both [Poetry](https://python-poetry.org/) (recommended) and [Virtualenv](https://virtualenv.pypa.io/en/latest/). 
```
<-- Install dependencies as shown above in Step I -->
user@host:~/packet-sniffer$ python3 build.py
```
## Usage
```
sniffer.py [-h] [-i INTERFACE] [-d]

Network Packet Sniffer

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Interface from which packets will be captured (monitors
                        all available interfaces by default).
  -d, --data            Output packet data during capture.
```
## Legal Disclaimer
The code in this repository should only be used with proper consent and in compliance with all relevant local, state, and federal laws.
Users are responsible for adhering to legal regulations.
The developers do not assume any liability and are not accountable for any misuse or harm caused by this code if it is used by unauthorized individuals or threat actors, intentionally or unintentionally, to compromise the security, privacy, integrity, or availability of systems and associated resources. In this context, "compromise" refers to the exploitation of known or unknown vulnerabilities within these systems, which may include the manipulation of security measures, whether through human actions or electronic means.

The use of this code is explicitly supported by the developers in specific scenarios, such as educational environments or authorized penetration testing engagements. These engagements should have a clear objective of identifying and mitigating vulnerabilities in systems, thereby reducing their susceptibility to exploitation and attacks by malicious actors, as defined in their respective threat models.
