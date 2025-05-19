import os
import re

def scan_files():
    print("[*] Simulating YARA scan...")
    suspicious_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".log"):
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    content = f.read()
                    if "unauthorized access" in content:
                        suspicious_files.append(f"{file}: unauthorized access pattern found")
    return suspicious_files
