"""Config flow for IP Scanner integration."""
from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "ip_scanner"

@config_entries.HANDLERS.register(DOMAIN)
class IPScannerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for IP Scanner."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="IP Scanner", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
