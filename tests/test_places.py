import pytest
from dotenv import load_dotenv
from olamaps import Client, AsyncClient

from .fixtures import client, async_client

load_dotenv()


@pytest.mark.asyncio
async def test_autocomplete_missing_text(client: Client, async_client: AsyncClient):
    with pytest.raises(AssertionError):
        client.autocomplete("")

    with pytest.raises(AssertionError):
        await async_client.autocomplete("")


@pytest.mark.asyncio
async def test_autocomplete(client: Client, async_client: AsyncClient):
    results = client.autocomplete(
        text="kempe", location="13.19825,77.67311", radius=100
    )
    assert len(results)

    results = await async_client.autocomplete(
        text="kempe", location="13.19825,77.67311", radius=100
    )
    assert len(results)


@pytest.mark.asyncio
async def test_geocoding_missing_address(client: Client, async_client: AsyncClient):
    with pytest.raises(AssertionError):
        client.geocode("")

    with pytest.raises(AssertionError):
        await async_client.geocode("")


@pytest.mark.asyncio
async def test_geocoding(client: Client, async_client: AsyncClient):
    results = client.geocode("World Trade Park, Jaipur")
    assert len(results)

    results = await async_client.geocode("World Trade Park, Jaipur")
    assert len(results)


@pytest.mark.asyncio
async def test_reverse_geocoding(client: Client, async_client: AsyncClient):
    results = client.reverse_geocode("12.9519408", "77.6381845")
    assert len(results)

    results = await async_client.reverse_geocode("12.9519408", "77.6381845")
    assert len(results)
