"""Support for LHP."""
from __future__ import annotations

from lhp import CurrentWaterLevel

from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfLength, CONF_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up LHP entity based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LhpSensorEntity(entry=entry, coordinator=coordinator)])


class LhpSensorEntity(
    CoordinatorEntity[DataUpdateCoordinator[CurrentWaterLevel]], SensorEntity
):
    """Defines an LHP sensor entity."""

    _attr_has_entity_name = True
    _attr_native_unit_of_measurement = UnitOfLength.CENTIMETERS
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0
    _attr_icon = "mdi:wave"

    def __init__(
        self,
        *,
        entry: ConfigEntry,
        coordinator: DataUpdateCoordinator[CurrentWaterLevel],
    ) -> None:
        """Initialize LHP sensor entity."""
        super().__init__(coordinator=coordinator)
        self._attr_unique_id = entry.entry_id

        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer="Länderübergreifendes Hochwasserportal",
            name=entry.data[CONF_ID] + "_water_level",
        )

    @property
    def native_value(self) -> float | None:
        """Return the current water level."""
        if not self.coordinator.data.water_level:
            return None
        return self.coordinator.data.water_level
