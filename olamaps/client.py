import os
import httpx
from typing import Optional

from .exceptions import AuthError, ClientError, InvalidRequestError, MapsServiceError

_DEFAULT_BASE_URL = "https://api.olamaps.io"


class Client:
    from .places import autocomplete, geocode, reverse_geocode
    from .routing import directions

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
    ):
        """
        :param client_id: Ola Maps API client ID. Required unless environment variable OLAMAPS_CLIENT_ID is set
        :param client_secret: Ola Maps API client secret. Required unless environment variable OLAMAPS_CLIENT_SECRET is set
        :param api_key: Ola Maps API key. Required unless environment variable OLAMAPS_API_KEY is set

        :param base_url: Base URL for the Ola Maps API. Default is https://api.olamaps.io
        """

        self.client_id = client_id or os.environ.get("OLAMAPS_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("OLAMAPS_CLIENT_SECRET")
        self.api_key = api_key or os.environ.get("OLAMAPS_API_KEY")
        self.base_url = base_url or _DEFAULT_BASE_URL

        self.session = httpx.Client(base_url=base_url, timeout=30)

        if self.api_key:
            self.session.params = self.session.params.set("api_key", self.api_key)
        elif self.client_id and self.client_secret:
            token = self._get_token()
            self.session.headers["Authorization"] = f"Bearer {token}"
        else:
            raise ClientError(
                "Either Ola Maps API key or both client ID and client secret are required."
            )

    def _get_token(self) -> str:
        response = httpx.post(
            url="https://account.olamaps.io/realms/olamaps/protocol/openid-connect/token",
            data={
                "grant_type": "client_credentials",
                "scope": "openid",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        ).json()

        if response.get("error"):
            raise AuthError(
                response.get(
                    "error_description",
                    "Invalid client id or secret provided.",
                )
            )

        return response.get("access_token")

    def _request(self, method, url, params) -> dict:
        response = self.session.request(
            method=method,
            url=url,
            params=params,
        )

        if response.status_code == 401:
            raise AuthError

        response = {"status_code": response.status_code, **response.json()}

        if response["status_code"] >= 500:
            raise MapsServiceError(
                response.get("reason", "Maps service faced some issue.")
            )
        elif response["status_code"] >= 400:
            raise InvalidRequestError(
                response.get("reason", "Invalid request parameters were sent.")
            )

        return response

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


class AsyncClient:
    from .places import (
        async_autocomplete as autocomplete,
        async_geocode as geocode,
        async_reverse_geocode as reverse_geocode,
    )
    from .routing import async_directions as directions

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: str = _DEFAULT_BASE_URL,
    ):
        """
        :param client_id: Ola Maps API client ID. Required unless environment variable OLAMAPS_CLIENT_ID is set
        :param client_secret: Ola Maps API client secret. Required unless environment variable OLAMAPS_CLIENT_SECRET is set
        :param api_key: Ola Maps API key. Required unless environment variable OLAMAPS_API_KEY is set

        :param base_url: Base URL for the Ola Maps API. Default is https://api.olamaps.io
        """

        self.client_id = client_id or os.environ.get("OLAMAPS_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("OLAMAPS_CLIENT_SECRET")
        self.api_key = api_key or os.environ.get("OLAMAPS_API_KEY")
        self.base_url = base_url or _DEFAULT_BASE_URL

        self.session = httpx.AsyncClient(base_url=base_url, timeout=30)

        if self.api_key:
            self.session.params = self.session.params.set("api_key", self.api_key)
        elif self.client_id and self.client_secret:
            token = self._get_token()
            self.session.headers["Authorization"] = f"Bearer {token}"
        else:
            raise ClientError(
                "Either Ola Maps API key or both client ID and client secret are required."
            )

    def _get_token(self) -> str:
        response = httpx.post(
            url="https://account.olamaps.io/realms/olamaps/protocol/openid-connect/token",
            data={
                "grant_type": "client_credentials",
                "scope": "openid",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        ).json()

        if response.get("error"):
            raise AuthError(
                response.get(
                    "error_description",
                    "Invalid client id or secret provided.",
                )
            )

        return response.get("access_token")

    async def _request(self, method, url, params) -> dict:
        response = await self.session.request(
            method=method,
            url=url,
            params=params,
        )

        if response.status_code == 401:
            raise AuthError

        response = {"status_code": response.status_code, **response.json()}

        if response["status_code"] >= 500:
            raise MapsServiceError(
                response.get("reason", "Maps service faced some issue.")
            )
        elif response["status_code"] >= 400:
            raise InvalidRequestError(
                response.get("reason", "Invalid request parameters were sent.")
            )

        return response

    async def close(self):
        await self.session.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *a):
        await self.close()
