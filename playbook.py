from threat_hunting.yara_scanner import scan_files
from data_collection.log_collector import collect_logs
from data_collection.network_sniffer import sniff_packets
from alerting.email_alert import send_alert

def run_playbook():
    print("[*] Starting Automated Incident Response Playbook...")

    print("[*] Collecting logs...")
    collect_logs()

    print("[*] Starting network traffic capture...")
    sniff_packets(duration=10)

    print("[*] Performing threat hunting using YARA...")
    matches = scan_files()
    if matches:
        print("[!] Threats detected!")
        send_alert("Threats detected", "\n".join(matches))
    else:
        print("[+] No threats found.")

if __name__ == "__main__":
    run_playbook()
