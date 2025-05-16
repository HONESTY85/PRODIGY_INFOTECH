from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_callback(packet):
    time_stamp = datetime.now().strftime("%H:%M:%S")

    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = "Other"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        print(f"[{time_stamp}] {src_ip} --> {dst_ip} | Protocol: {protocol}")

        if Raw in packet:
            payload = packet[Raw].load[:30]  # Display first 30 bytes
            try:
                print(f"    Payload: {payload.decode('utf-8', errors='ignore')}")
            except:
                print(f"    Payload: {payload}")
        print("-" * 60)

def main():
    print("=== Packet Sniffer Started (Press Ctrl+C to stop) ===")
    # Requires root or admin privileges
    sniff(filter="ip", prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
