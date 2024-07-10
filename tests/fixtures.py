import pytest_asyncio
from olamaps import Client

@pytest_asyncio.fixture
async def client():
    api_client = Client()
    yield api_client

    await api_client.close()
