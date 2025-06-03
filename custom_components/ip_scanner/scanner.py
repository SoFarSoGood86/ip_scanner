import subprocess
import re
import platform

def get_connected_devices():
    result = []

    try:
        system = platform.system()

        if system == "Linux":
            iw_output = subprocess.check_output("iw dev wlan0 station dump", shell=True).decode()
            arp_output = subprocess.check_output("arp -n", shell=True).decode()

            mac_rssi = dict(re.findall(r"Station ([0-9a-f:]+).*?signal: (-\d+) dBm", iw_output, re.DOTALL))
            for line in arp_output.splitlines():
                if "wlan0" in line:
                    parts = line.split()
                    ip = parts[0]
                    mac = parts[2]
                    signal = int(mac_rssi.get(mac.lower(), -100))
                    result.append({"ip": ip, "mac": mac, "signal": signal})
    except Exception as e:
        print(f"IP Scanner error: {e}")
    return result
