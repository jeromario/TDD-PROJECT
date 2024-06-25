from uuid import UUID
from store.usecases.product import product_usecase
from tests.schemas.product import ProductOut


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


async def test_usecases_get_should_return_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


async def test_usecases_get_should_not_found():
    result = await product_usecase.get(UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a"))

    assert isinstance(result, ProductOut)
