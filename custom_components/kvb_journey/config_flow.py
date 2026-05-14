from homeassistant import config_entries
from .const import DOMAIN


class KVBJourneyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        await self.async_set_unique_id("kvb_journey_default")
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title="KVB Fahrplanauskunft",
            data={}
        )
