import argparse
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        protocol_name = "Unknown"
        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        elif protocol == 1:
            protocol_name = "ICMP"
            
        print(f"\n[+] IPv4 Packet: {ip_src} -> {ip_dst} (Protocol: {protocol_name})")
        
        # Check for TCP/UDP for port information
        if TCP in packet:
            print(f"    Ports: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"    Ports: {packet[UDP].sport} -> {packet[UDP].dport}")
            
        # Display Payload if present
        if Raw in packet:
            try:
                # Try to decode payload as utf-8, ignore errors to get a readable preview
                payload = packet[Raw].load.decode('utf-8', errors='ignore')
                # Replace newlines with spaces for a cleaner one-line preview
                payload_clean = payload.replace('\n', ' ').replace('\r', '')
                print(f"    Payload: {payload_clean[:100]}...") 
            except Exception:
                pass

def start_sniffer(interface=None):
    print("Starting network sniffer...")
    print("Press Ctrl+C to stop.")
    
    # scapy sniff function will capture packets and call packet_callback for each
    if interface:
        print(f"Sniffing on interface: {interface}")
        sniff(iface=interface, prn=packet_callback, store=0)
    else:
        print("Sniffing on default interface...")
        sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Network Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on (e.g., eth0, wlan0)", default=None)
    args = parser.parse_args()
    
    start_sniffer(args.interface)
