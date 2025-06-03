from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.discovery import async_load_platform

DOMAIN = "ip_scanner"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.async_create_task(
        async_load_platform(hass, "device_tracker", DOMAIN, {}, entry.data)
    )
    return True
