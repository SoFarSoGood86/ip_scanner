import asyncio
from datetime import timedelta
from homeassistant.components.device_tracker.config_entry import ScannerEntity
from homeassistant.helpers.event import async_track_time_interval
from .scanner import get_connected_devices
from .const import DOMAIN, SCAN_INTERVAL

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    scanner = IPScanner(hass, async_add_entities)
    await scanner.async_initialize()

class IPScanner:
    def __init__(self, hass, async_add_entities):
        self.hass = hass
        self.async_add_entities = async_add_entities
        self.entities = {}

    async def async_initialize(self):
        await self._async_scan()
        async_track_time_interval(self.hass, self._async_scan, timedelta(seconds=SCAN_INTERVAL))

    async def _async_scan(self, now=None):
        devices = await self.hass.async_add_executor_job(get_connected_devices)
        new_entities = []
        for dev in devices:
            mac = dev["mac"]
            if mac not in self.entities:
                entity = IPScannerDevice(mac, dev["ip"], dev["signal"])
                self.entities[mac] = entity
                new_entities.append(entity)
            else:
                self.entities[mac].update(dev["ip"], dev["signal"])
        if new_entities:
            self.async_add_entities(new_entities)

class IPScannerDevice(ScannerEntity):
    def __init__(self, mac, ip, signal):
        self._mac = mac
        self._ip = ip
        self._signal = signal
        self._name = f"IP Scanner {mac[-5:].replace(':', '')}"

    @property
    def is_connected(self):
        return True

    @property
    def ip_address(self):
        return self._ip

    @property
    def mac_address(self):
        return self._mac

    @property
    def extra_state_attributes(self):
        return {"signal_strength": self._signal}

    @property
    def name(self):
        return self._name

    def update(self, ip, signal):
        self._ip = ip
        self._signal = signal
        self.async_write_ha_state()
