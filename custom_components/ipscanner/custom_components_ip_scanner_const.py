from homeassistant.const import Platform

DOMAIN = "ip_scanner"
PLATFORMS = [Platform.SENSOR]
CONF_IP_RANGE = "ip_range"
SCAN_INTERVAL = 900  # 15 minutes in seconds