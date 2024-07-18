import pytest
import pytest_asyncio
from olamaps import Client, AsyncClient

@pytest_asyncio.fixture
async def async_client():
    api_client = AsyncClient()
    yield api_client

    await api_client.close()

@pytest.fixture
def client():
    api_client = Client()
    yield api_client

    api_client.close()
