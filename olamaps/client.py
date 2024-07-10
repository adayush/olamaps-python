import os
import aiohttp
import requests
from urllib.parse import quote_plus
from typing import Optional

_DEFAULT_BASE_URL = "https://api.olamaps.io"


class Client:
    from .places import geocode, reverse_geocode

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = _DEFAULT_BASE_URL,
    ):
        """
        :param client_id: Ola Maps API client ID. Required unless environment variable OLAMAPS_CLIENT_ID is set
        :param client_secret: Ola Maps API client secret. Required unless environment variable OLAMAPS_CLIENT_SECRET is set

        :param base_url: Base URL for the Ola Maps API. Default is https://api.olamaps.io
        """

        self.client_id = client_id or os.environ.get("OLAMAPS_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("OLAMAPS_CLIENT_SECRET")
        self.api_key = api_key or os.environ.get("OLAMAPS_API_KEY")
        self.base_url = base_url or _DEFAULT_BASE_URL

        if self.api_key:
            self.session = aiohttp.ClientSession(
                base_url=base_url,
            )
        elif self.client_id and self.client_secret:
            token = self._get_token()
            self.session = aiohttp.ClientSession(
                base_url=base_url,
                headers={"Authorization": f"Bearer {token}"},
            )
        else:
            raise AttributeError(
                "Either Ola Maps API key or both client ID and client secret are required"
            )

    def _get_token(self):
        response = requests.post(
            url="https://account.olamaps.io/realms/olamaps/protocol/openid-connect/token",
            data={
                "grant_type": "client_credentials",
                "scope": "openid",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        ).json()
        assert response.get(
            "access_token"
        ), "Invalid client or Invalid client credentials"
        return response.get("access_token")

    async def _request(self, method, url, params):
        if not self.session.headers.get("Authorization"):
            params["api_key"] = self.api_key

        response = await self.session.request(method=method, url=url, params=params)
        return await response.json()

    async def close(self):
        await self.session.close()
