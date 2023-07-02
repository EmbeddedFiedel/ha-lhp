"""Config flow to configure the LHP integration."""
from __future__ import annotations

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_ID
from homeassistant.helpers import selector
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class LhpFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for LHP."""

    VERSION = 1

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_ID])
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=user_input[CONF_ID],
                data={CONF_ID: user_input[CONF_ID]},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_ID,
                        default=(user_input or {}).get(CONF_ID),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT
                        ),
                    ),
                }
            ),
            errors=_errors,
        )
