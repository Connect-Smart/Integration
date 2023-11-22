import logging
from homeassistant.components.binary_sensor import BinarySensorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Solar Switch binary sensor."""
    async_add_entities([CSSolarSwitchSensor()])


class CSSolarSwitchSensor(BinarySensorEntity):
    """Representation of a CS solar switch binary sensor."""

    def __init__(self):
        """Initialize the binary sensor."""
        self._state = False

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return "CS Solar Switch"

    @property
    def is_on(self):
        """Return true if the binary sensor is on (positive power value)."""
        return self._state

    async def async_update(self):
        """Update the state of the binary sensor."""
        # Simulate changing state based on some condition (e.g., random Solar switch)
        import random
        self._state = bool(random.getrandbits(1))
