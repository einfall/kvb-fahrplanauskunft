from aiohttp import web
from homeassistant.components.http import HomeAssistantView
import aiohttp
import logging
from urllib.parse import quote

_LOGGER = logging.getLogger(__name__)
API_BASE = "https://kvb.mobilesticket.de/openapi/v2/journey/700"


async def fetch_json(url):
    print(f"KVB API CALL: {url}", flush=True)
    _LOGGER.info("KVB API CALL: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(f"KVB API RESPONSE: status={resp.status} url={url}", flush=True)
            _LOGGER.info("KVB API RESPONSE: status=%s url=%s", resp.status, url)
            return await resp.json()


class KVBSearchView(HomeAssistantView):
    url = "/api/kvb_journey/search"
    name = "api:kvb_journey:search"
    requires_auth = False

    async def get(self, request):
        query = request.query.get("q", "")
        print(f"KVB SEARCH REQUEST: query={query}", flush=True)
        _LOGGER.info("KVB SEARCH REQUEST: query=%s", query)
        url = f"{API_BASE}/locations?q={quote(query)}&type=S"
        return web.json_response(await fetch_json(url))


class KVBJourneyView(HomeAssistantView):
    url = "/api/kvb_journey/journey"
    name = "api:kvb_journey:journey"
    requires_auth = False

    async def get(self, request):
        start_id = request.query.get("start")
        dest_id = request.query.get("dest")
        date = request.query.get("date")

        print(f"KVB JOURNEY REQUEST: start={start_id} dest={dest_id} date={date}", flush=True)
        _LOGGER.info("KVB JOURNEY REQUEST: start=%s dest=%s date=%s", start_id, dest_id, date)

        url = (
            f"{API_BASE}/journey/"
            f"{quote(start_id or '', safe='')}/"
            f"{quote(dest_id or '', safe='')}"
            f"?via=&date={quote(date or '', safe='T:-')}&ptrans=&flags=00000"
        )
        return web.json_response(await fetch_json(url))


class KVBNextView(HomeAssistantView):
    url = "/api/kvb_journey/next"
    name = "api:kvb_journey:next"
    requires_auth = False

    async def get(self, request):
        recall_id = request.query.get("recallId")
        print(f"KVB NEXT REQUEST: recallId={recall_id}", flush=True)
        _LOGGER.info("KVB NEXT REQUEST: recallId=%s", recall_id)
        url = f"{API_BASE}/journey/next/{quote(recall_id or '', safe=':')}"
        return web.json_response(await fetch_json(url))


class KVBPreviousView(HomeAssistantView):
    url = "/api/kvb_journey/previous"
    name = "api:kvb_journey:previous"
    requires_auth = False

    async def get(self, request):
        recall_id = request.query.get("recallId")
        print(f"KVB PREVIOUS REQUEST: recallId={recall_id}", flush=True)
        _LOGGER.info("KVB PREVIOUS REQUEST: recallId=%s", recall_id)
        url = f"{API_BASE}/journey/previous/{quote(recall_id or '', safe=':')}"
        return web.json_response(await fetch_json(url))
