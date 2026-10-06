# Basic Network Sniffer

This is a simple Python-based network sniffer built using the `scapy` library. It captures network traffic and provides basic analysis by displaying source and destination IP addresses, protocols (TCP, UDP, ICMP), port numbers, and a preview of the packet payload.

## Features

- Captures IPv4 network packets.
- Identifies protocols (TCP, UDP, ICMP).
- Displays source and destination IPs and ports.
- Provides a string preview of the payload (if present).

## Prerequisites

- **Python 3.x**
- **Scapy library**: You need to install `scapy` to run this program.

```bash
pip install scapy
```

- **Npcap (Windows)**: If you are running this on Windows, you will need to install Npcap (https://npcap.com/) for Scapy to be able to capture packets. Linux users may need to run the script with `sudo` privileges.

## Usage

You can run the script without any arguments to sniff on the default network interface:

```bash
python sniffer.py
```

**(Note: You usually need Administrator/root privileges to capture network traffic.)**

### Specify an Interface

If you want to specify a particular network interface (e.g., `eth0` or `Wi-Fi`), you can use the `-i` or `--interface` flag:

```bash
python sniffer.py -i eth0
```

## Example Output

```
Starting network sniffer...
Press Ctrl+C to stop.
Sniffing on default interface...

[+] IPv4 Packet: 192.168.1.15 -> 142.250.190.46 (Protocol: TCP)
    Ports: 54321 -> 443

[+] IPv4 Packet: 142.250.190.46 -> 192.168.1.15 (Protocol: TCP)
    Ports: 443 -> 54321
    Payload: Application Data...
```

## Disclaimer

This tool is created for educational purposes only. Do not use this tool on any network where you do not have explicit permission to monitor the traffic.