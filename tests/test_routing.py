import pytest
from dotenv import load_dotenv
from olamaps import Client, AsyncClient

from .fixtures import client, async_client

load_dotenv()


@pytest.mark.asyncio
async def test_directions(client: Client, async_client: AsyncClient):
    routes = client.directions(
        origin="12.993103152916301,77.54332622119354",
        destination="12.972006793201695,77.5800850011884",
        alternatives=True,
        steps=True,
    )
    assert len(routes)

    routes = await async_client.directions(
        origin="12.993103152916301,77.54332622119354",
        destination="12.972006793201695,77.5800850011884",
        alternatives=True,
        steps=True,
    )
    assert len(routes)
