from pydantic import Field
from tests.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Quantity Product")
    price: float = Field(..., description="Price product")
    status: bool = Field(..., description="Status product")


class ProductOut(ProductIn):
    ...
