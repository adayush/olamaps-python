import pytest
from dotenv import load_dotenv
from olamaps import Client

from .fixtures import client

load_dotenv()


@pytest.mark.asyncio
async def test_routing(client: Client):
    res = await client.directions(
        origin="12.993103152916301,77.54332622119354",
        destination="12.972006793201695,77.5800850011884",
        alternatives=True,
        steps=True,
    )

    assert res["status_code"] == 200
