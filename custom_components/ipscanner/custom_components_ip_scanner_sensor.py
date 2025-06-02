import logging
import nmap
import subprocess
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from homeassistant.const import CONF_IP_RANGE
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    ip_range = config_entry.data[CONF_IP_RANGE]
    
    coordinator = IPScannerCoordinator(hass, ip_range)
    await coordinator.async_config_entry_first_refresh()
    
    # Create sensors for each discovered device
    devices = coordinator.data or {}
    entities = [
        IPScannerSensor(coordinator, device, key)
        for device, info in devices.items()
        for key in ["ip", "mac", "rssi"]
        if key in info
    ]
    
    async_add_entities(entities)

class IPScannerCoordinator(DataUpdateCoordinator):
    """Coordinator to manage network scanning."""

    def __init__(self, hass: HomeAssistant, ip_range: str):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=SCAN_INTERVAL),
        )
        self.ip_range = ip_range

    async def _async_update_data(self):
        """Fetch data from the network."""
        try:
            nm = nmap.PortScanner()
            # Perform a quick ping scan
            scan_result = await self.hass.async_add_executor_job(
                nm.scan, self.ip_range, arguments="-sn"
            )
            devices = {}
            
            for host in nm.all_hosts():
                if "mac" in nm[host]["addresses"]:
                    mac = nm[host]["addresses"]["mac"]
                    rssi = await self._get_wifi_signal(host)
                    devices[host] = {
                        "ip": host,
                        "mac": mac,
                        "rssi": rssi if rssi is not None else "N/A"
                    }
            
            return devices
        except Exception as err:
            _LOGGER.error("Error scanning network: %s", err)
            return {}

    async def _get_wifi_signal(self, ip: str) -> str | None:
        """Attempt to get Wi-Fi signal strength (RSSI) for a device."""
        try:
            # This is a placeholder for RSSI retrieval
            # Actual implementation depends on the system and available tools
            result = await self.hass.async_add_executor_job(
                subprocess.run,
                ["iw", "dev", "wlan0", "station", "get", ip],
                capture_output=True,
                text=True
            )
            output = result.stdout
            # Parse RSSI from output (example parsing, adjust based on actual output)
            for line in output.split("\n"):
                if "signal:" in line:
                    return line.split(":")[1].strip()
            return None
        except Exception:
            return None

class IPScannerSensor(CoordinatorEntity, SensorEntity):
    """Representation of a network device sensor."""

    def __init__(self, coordinator: DataUpdateCoordinator, device: str, key: str):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._device = device
        self._key = key
        self._attr_unique_id = f"{DOMAIN}_{device}_{key}"
        self._attr_name = f"IP Scanner {device} {key.upper()}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._device, {}).get(self._key, "unknown")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return {
            "ip": "mdi:ip",
            "mac": "mdi:network",
            "rssi": "mdi:wifi"
        }.get(self._key, "mdi:help")