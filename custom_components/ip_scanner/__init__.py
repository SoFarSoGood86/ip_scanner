"""IP Scanner integration for Home Assistant."""

from homeassistant.core import HomeAssistant

DOMAIN = "ip_scanner"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the IP Scanner component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up IP Scanner from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True
