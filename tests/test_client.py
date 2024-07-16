import os
import pytest
import asyncio
from dotenv import load_dotenv

from olamaps import Client, AuthError, ClientError

load_dotenv()


@pytest.mark.asyncio
async def test_missing_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.delenv("OLAMAPS_CLIENT_ID", raising=False)
        mp.delenv("OLAMAPS_CLIENT_SECRET", raising=False)

        with pytest.raises(ClientError):
            client = Client()
            await client.close()


@pytest.mark.asyncio
async def test_partial_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.delenv("OLAMAPS_CLIENT_ID", raising=False)
        mp.delenv("OLAMAPS_CLIENT_SECRET", raising=False)

        with pytest.raises(ClientError):
            client = Client(client_id="1234")
            await client.close()


@pytest.mark.asyncio
async def test_invalid_client_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.setenv("OLAMAPS_CLIENT_ID", "1234")
        mp.setenv("OLAMAPS_CLIENT_SECRET", "1234")

        with pytest.raises(AuthError):
            client = Client()
            await client.close()


@pytest.mark.asyncio
async def test_valid_client_params():
    client = Client()
    await client.close()


@pytest.mark.asyncio
async def test_invalid_api_key():
    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("OLAMAPS_API_KEY", "1234")

        with pytest.raises(AuthError):
            client = Client()
            await client.geocode("World Trade Park, Jaipur")
            await client.close()
