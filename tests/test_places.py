import pytest
from dotenv import load_dotenv
from olamaps import Client

from .fixtures import client

load_dotenv()


@pytest.mark.asyncio
async def test_geocoding_missing_address(client):
    with pytest.raises(AssertionError):
        await client.geocode("")


@pytest.mark.asyncio
async def test_geocoding(client):
    res = await client.geocode("World Trade Park, Jaipur")
    assert res["status"] == "ok"


@pytest.mark.asyncio
async def test_reverse_geocoding_invalid_lat_lng(client):
    with pytest.raises(AssertionError):
        res = await client.reverse_geocode(91, 181)


@pytest.mark.asyncio
async def test_reverse_geocoding_valid_lat_lng(client):
    res = await client.reverse_geocode(12.9519408, 77.6381845)
    assert res["status"] == "ok"
