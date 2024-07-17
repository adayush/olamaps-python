import pytest
from dotenv import load_dotenv
from olamaps import Client

from .fixtures import client

load_dotenv()


@pytest.mark.asyncio
async def test_autocomplete_missing_text(client: Client):
    with pytest.raises(AssertionError):
        await client.autocomplete("")


@pytest.mark.asyncio
async def test_autocomplete(client: Client):
    results = await client.autocomplete(
        text="kempe", location="13.19825,77.67311", radius=100
    )
    assert len(results)


@pytest.mark.asyncio
async def test_geocoding_missing_address(client: Client):
    with pytest.raises(AssertionError):
        await client.geocode("")


@pytest.mark.asyncio
async def test_geocoding(client: Client):
    results = await client.geocode("World Trade Park, Jaipur")
    assert len(results)


@pytest.mark.asyncio
async def test_reverse_geocoding(client: Client):
    results = await client.reverse_geocode("12.9519408", "77.6381845")
    assert len(results)
