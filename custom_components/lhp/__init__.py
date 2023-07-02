"""Custom integration to integrate integration_blueprint with Home Assistant.

For more details about this integration, please refer to
https://github.com/ludeeus/integration_blueprint
"""
from __future__ import annotations

from lhp import (
    LHPClient,
    CurrentWaterLevel,
    LHPError,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform, CONF_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed


from .const import DOMAIN, LOGGER, SCAN_INTERVAL

PLATFORMS = [Platform.SENSOR]


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Create LHP config entry."""
    session = async_get_clientsession(hass)
    lhp_client = LHPClient(session=session)

    async def async_update_currentwaterlevel() -> CurrentWaterLevel:
        try:
            return await lhp_client.currentwaterlevel(
                pgnr=entry.data[CONF_ID],
            )
        except LHPError as err:
            raise UpdateFailed("LHP API communication error") from err

    coordinator: DataUpdateCoordinator[CurrentWaterLevel] = DataUpdateCoordinator(
        hass,
        LOGGER,
        name=f"{DOMAIN}_{entry.data[CONF_ID]}",
        update_interval=SCAN_INTERVAL,
        update_method=async_update_currentwaterlevel,
    )
    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload LHP config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        del hass.data[DOMAIN][entry.entry_id]
    return unload_ok
