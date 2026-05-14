from .const import DOMAIN
from .views import KVBSearchView
from .views import KVBJourneyView
from .views import KVBNextView
from .views import KVBPreviousView

PLATFORMS = []


async def async_setup_entry(hass, entry):
    hass.http.register_view(KVBSearchView)
    hass.http.register_view(KVBJourneyView)
    hass.http.register_view(KVBNextView)
    hass.http.register_view(KVBPreviousView)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    return True


async def async_unload_entry(hass, entry):
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
