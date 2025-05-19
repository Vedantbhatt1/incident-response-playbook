import os
import shutil
import logging

def collect_logs():
    logging.info("Collecting logs...")
    os.makedirs("collected_logs", exist_ok=True)
    sample_logs = ["/var/log/syslog", "/var/log/auth.log"] if os.name != 'nt' else ["C:\\Windows\\System32\\LogFiles\\Firewall\\pfirewall.log"]
    for log in sample_logs:
        if os.path.exists(log):
            shutil.copy(log, "collected_logs/")
