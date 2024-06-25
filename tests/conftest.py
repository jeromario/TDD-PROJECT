import asyncio
from uuid import UUID
import pytest
from store.db.mongo import db_client
from tests.factories import product_data
from tests.schemas.product import ProductIn


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        if collection_name.startswith("system"):
            continue
        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("73e5b900d2aa676261b798dc1946f045548a")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)
