from pydantic import BaseModel, Field


class AddProductRequest(BaseModel):
    user_id: str = Field(..., description="User ID")
    product_id: str = Field(..., description="Product ID")
    outlet_id: str = Field(..., description="Outlet ID")


class CartProductInfo(BaseModel):
    cart: dict
    product: dict
    selling_price: float | None = None
<<<<<<< Updated upstream:src/joi_delivery/controller/models.py
=======


class ProductHealthItem(BaseModel):
    product_id: str = Field(..., description="Product ID")
    product_name: str = Field(..., description="Product name")
    available_stock: int = Field(..., description="Available stock quantity")
    threshold: int = Field(..., description="Minimum stock threshold")
    is_low_stock: bool = Field(..., description="Whether product is below threshold")
    mrp: float = Field(..., description="Maximum retail price")
    weight: float = Field(..., description="Product weight in grams")


class InventoryHealthResponse(BaseModel):
    store_id: str = Field(..., description="Store ID")
    store_name: str | None = Field(None, description="Store name")
    total_products: int = Field(0, description="Total number of products")
    low_stock_count: int = Field(0, description="Number of products below threshold")
    products: list[ProductHealthItem] = Field(default_factory=list, description="List of products with health status")
    message: str | None = Field(None, description="Optional message (e.g., for errors)")
>>>>>>> Stashed changes:src/controller/models.py
