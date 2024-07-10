import pytest
from dotenv import load_dotenv
from olamaps import Client

from .fixtures import client

load_dotenv()


@pytest.mark.asyncio
async def test_geocoding_missing_address(client: Client):
    with pytest.raises(AssertionError):
        await client.geocode("")


@pytest.mark.asyncio
async def test_geocoding(client: Client):
    res = await client.geocode("World Trade Park, Jaipur")
    print(res)
    assert res["status_code"] == 200


@pytest.mark.asyncio
async def test_reverse_geocoding(client: Client):
    res = await client.reverse_geocode("12.9519408", "77.6381845")
    assert res["status_code"] == 200
