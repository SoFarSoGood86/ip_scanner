from scapy.all import ARP, Ether, srp
import subprocess

def get_devices():
    devices = []
    try:
        ip_range = "192.168.1.1/24"
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=0)[0]
        for sent, received in result:
            mac = received.hwsrc
            ip = received.psrc
            rssi = get_rssi(ip)
            devices.append({
                "ip": ip,
                "mac": mac,
                "rssi": rssi
            })
    except Exception as e:
        print(f"Erreur de scan : {e}")
    return devices

def get_rssi(ip):
    try:
        cmd = f"iw dev wlan0 station dump | grep -A 10 {ip} | grep signal"
        result = subprocess.check_output(cmd, shell=True).decode()
        return int(result.strip().split()[-2])
    except:
        return None
