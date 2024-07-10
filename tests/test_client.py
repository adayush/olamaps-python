import os
import pytest
import asyncio
from dotenv import load_dotenv

from olamaps import Client

load_dotenv()


@pytest.mark.asyncio
async def test_missing_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.delenv("OLAMAPS_CLIENT_ID", raising=False)
        mp.delenv("OLAMAPS_CLIENT_SECRET", raising=False)

        with pytest.raises(AttributeError):
            client = Client()
            await client.close()


@pytest.mark.asyncio
async def test_partial_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.delenv("OLAMAPS_CLIENT_ID", raising=False)
        mp.delenv("OLAMAPS_CLIENT_SECRET", raising=False)

        with pytest.raises(AttributeError):
            client = Client(client_id="1234")
            await client.close()


@pytest.mark.asyncio
async def test_invalid_client_params():
    with pytest.MonkeyPatch.context() as mp:
        mp.delenv("OLAMAPS_API_KEY", raising=False)
        mp.setenv("OLAMAPS_CLIENT_ID", "1234")
        mp.setenv("OLAMAPS_CLIENT_SECRET", "1234")

        with pytest.raises(AssertionError):
            client = Client()
            await client.close()


@pytest.mark.asyncio
async def test_valid_client_params():
    client = Client()
    await client.close()
