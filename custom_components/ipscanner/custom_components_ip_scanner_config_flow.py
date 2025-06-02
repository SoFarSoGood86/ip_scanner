import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_IP_RANGE
from .const import DOMAIN

class IPScannerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for IP Scanner integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validate the IP range
            try:
                # Basic validation for IP range (e.g., 192.168.1.0/24 or 192.168.1.1-254)
                ip_range = user_input[CONF_IP_RANGE]
                if not ("/" in ip_range or "-" in ip_range):
                    errors["base"] = "invalid_ip_range"
                else:
                    # Store the configuration
                    return self.async_create_entry(
                        title="IP Scanner",
                        data={CONF_IP_RANGE: ip_range}
                    )
            except Exception:
                errors["base"] = "invalid_ip_range"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_RANGE, default="192.168.1.0/24"): str,
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OptionsFlowHandler(config_entry)

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for IP Scanner integration."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle the options step."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_IP_RANGE,
                    default=self.config_entry.data.get(CONF_IP_RANGE, "192.168.1.0/24")
                ): str,
            }),
        )