# IP Scanner Integration for Home Assistant

This Home Assistant integration provides a network scanner that identifies devices on your local network, including their IP addresses, MAC addresses, and Wi-Fi signal strength (RSSI) where available.

## Installation

### Prerequisites
- A running Home Assistant instance.
- A GitHub account for HACS authentication.
- The `nmap` tool installed on the Home Assistant host (`sudo apt-get install nmap` for non-Hass.io setups).
- The `iw` tool for Wi-Fi signal strength (optional, for RSSI support).

### Installation via HACS
1. Ensure HACS is installed in your Home Assistant instance.
2. Go to **HACS > Integrations**.
3. Click the three dots in the top-right corner and select **Custom repositories**.
4. Add `https://github.com/SoFarSoGood86/ip_scanner` as a custom repository with the category **Integration**.
5. Search for **IP Scanner** in HACS and click **Install**.
6. Restart Home Assistant.
7. Go to **Settings > Devices & Services**, click **+ Add Integration**, and select **IP Scanner**.
8. Enter the IP range to scan (e.g., `192.168.1.0/24` or `192.168.1.1-254`).
9. Follow the prompts to complete the setup.

### Manual Installation
1. Download the latest release from the [GitHub repository](https://github.com/SoFarSoGood86/ip_scanner).
2. Extract the `ip_scanner` folder to `config/custom_components/` in your Home Assistant installation.
3. Restart Home Assistant.
4. Go to **Settings > Devices & Services**, click **+ Add Integration**, and select **IP Scanner**.
5. Configure the IP range as prompted.

## Configuration
The integration requires an IP range to scan. This can be specified in CIDR notation (e.g., `192.168.1.0/24`) or as a range (e.g., `192.168.1.1-254`). The scan runs every 15 minutes by default.

### Example Entities
For each detected device, three sensors are created:
- `sensor.ip_scanner_192_168_1_100_ip`: The IP address of the device.
- `sensor.ip_scanner_192_168_1_100_mac`: The MAC address of the device.
- `sensor.ip_scanner_192_168_1_100_rssi`: The Wi-Fi signal strength (if available).

## Troubleshooting
- Ensure `nmap` is installed on the host system.
- Check Home Assistant logs for errors related to the network scan.
- Verify the IP range is correctly formatted.
- RSSI data may not be available for all devices or systems.

## Contributing
Contributions are welcome! Please submit issues or pull requests to the [GitHub repository](https://github.com/SoFarSoGood86/ip_scanner).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.