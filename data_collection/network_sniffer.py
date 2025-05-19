from scapy.all import sniff

def packet_callback(packet):
    print(f"[Packet] {packet.summary()}")

def sniff_packets(duration=10):
    sniff(prn=packet_callback, timeout=duration)
