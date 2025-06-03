from homeassistant.helpers.entity import Entity
from .scanner import get_devices
from .const import DOMAIN, SCAN_INTERVAL
import asyncio

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    entities = []
    devices = await hass.async_add_executor_job(get_devices)
    for device in devices:
        entities.append(IPScannerSensor(device["ip"], device["mac"], device["rssi"]))
    async_add_entities(entities, update_before_add=True)

class IPScannerSensor(Entity):
    def __init__(self, ip, mac, rssi):
        self._ip = ip
        self._mac = mac
        self._rssi = rssi
        self._name = f"IP Scanner {ip}"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._ip

    @property
    def extra_state_attributes(self):
        return {
            "mac_address": self._mac,
            "signal_strength": self._rssi
        }

    @property
    def icon(self):
        return "mdi:lan-connect"

    async def async_update(self):
        # Optionnel : réimplémenter une mise à jour périodique
        pass
