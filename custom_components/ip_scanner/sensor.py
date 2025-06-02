"""IP Scanner sensor platform."""

import logging
from datetime import timedelta
from typing import Dict

import asyncio
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers.event import async_track_time_interval

from scapy.all import ARP, Ether, srp

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=5)

async def async_setup_entry(
    hass: HomeAssistantType,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up sensors based on a config entry."""

    scanner = IPScanner(hass)
    await scanner.async_scan()

    sensors = []
    for mac, device in scanner.devices.items():
        sensors.append(IPScannerSensor(device, mac))

    async_add_entities(sensors, True)

    async def async_update_data(now):
        await scanner.async_scan()
        for sensor in sensors:
            device = scanner.devices.get(sensor.unique_id)
            if device:
                sensor.update_device(device)
                sensor.async_write_ha_state()

    async_track_time_interval(hass, async_update_data, SCAN_INTERVAL)


class IPScanner:
    """Class to scan the network."""

    def __init__(self, hass):
        self.devices: Dict[str, dict] = {}
        self.hass = hass

    async def async_scan(self):
        """Scan the network for devices."""
        _LOGGER.debug("Starting network scan")

        loop = asyncio.get_event_loop()

        def scan_network():
            arp = ARP(pdst="192.168.1.0/24")
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            result = srp(packet, timeout=3, verbose=0)[0]

            devices = {}
            for sent, received in result:
                ip = received.psrc
                mac = received.hwsrc
                signal = None
                devices[mac] = {
                    "ip": ip,
                    "mac": mac,
                    "signal": signal,
                    "name": None,
                }
            return devices

        self.devices = await loop.run_in_executor(None, scan_network)


class IPScannerSensor(SensorEntity):
    """Representation of a scanned device as a sensor."""

    def __init__(self, device: dict, mac: str):
        self._device = device
        self._mac = mac
        self._attr_unique_id = mac
        self._attr_name = f"IP Scanner {mac}"
        self._attr_native_value = device.get("ip")
        self._attr_extra_state_attributes = {
            "ip": device.get("ip"),
            "mac": mac,
            "signal": device.get("signal"),
        }

    @property
    def unique_id(self):
        return self._mac

    @property
    def name(self):
        return self._attr_name

    @property
    def native_value(self):
        return self._attr_native_value

    @property
    def extra_state_attributes(self):
        return self._attr_extra_state_attributes

    def update_device(self, device):
        self._device = device
        self._attr_native_value = device.get("ip")
        self._attr_extra_state_attributes = {
            "ip": device.get("ip"),
            "mac": device.get("mac"),
            "signal": device.get("signal"),
        }
