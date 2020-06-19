import json
from urllib.parse import urljoin

import requests


class Tradier:
    """ (currently readonly) api for grabbing tradier data """

    def __init__(
        self, access_token: str, base_url: str = "https://sandbox.tradier.com",
    ):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {access_token}", "Accept": "application/json",}
        )

    def request(self, path: str, params: dict) -> dict:
        """ makes a GET request to a particular endpoint """
        url = urljoin(self.base_url, path)
        response = self.session.get(url, params=params)
        assert response.status_code == 200
        return response.json()

    def get_quotes(self, symbols: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-quotes """
        return self.request("/v1/markets/quotes", {"symbols": symbols, **kwargs})

    def get_options_chains(self, symbol: str, expiration: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-options-chains """
        return self.request(
            "/v1/markets/options/chains",
            {"symbol": symbol, "expiration": expiration, **kwargs},
        )

    def get_options_strikes(self, symbol: str, expiration: str) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-options-strikes """
        return self.request(
            "/v1/markets/options/strikes", {"symbol": symbol, "expiration": expiration},
        )

    def get_options_expirations(self, symbol: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-options-expirations """
        return self.request(
            "/v1/markets/options/expirations", {"symbol": symbol, **kwargs},
        )

    def get_lookup_options_symbols(self, underlying: str) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-lookup-options-symbols """
        return self.request("/v1/markets/options/lookup", {"underlying": underlying})

    def get_history(self, symbol: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-history """
        return self.request("/v1/markets/history", {"symbol": symbol, **kwargs})

    def get_timesales(self, symbol: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-timesales """
        return self.request("/v1/markets/timesales", {"symbol": symbol, **kwargs})

    def get_etb(self) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-etb """
        return self.request("/v1/markets/etb", {})

    def get_clock(self) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-clock """
        return self.request("/v1/markets/clock", {})

    def get_calendar(self, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-calendar """
        return self.request("/v1/markets/calendar", {**kwargs})

    def get_search(self, q: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-search """
        return self.request("/v1/markets/search", {"q": q, **kwargs})

    def get_lookup(self, q: str, **kwargs: dict) -> dict:
        """ https://documentation.tradier.com/brokerage-api/markets/get-lookup """
        return self.request("/v1/markets/lookup", {"q": q, **kwargs})
