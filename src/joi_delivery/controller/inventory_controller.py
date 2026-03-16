from http import HTTPStatus
<<<<<<< Updated upstream:src/joi_delivery/controller/inventory_controller.py

from fastapi import APIRouter, Query, Response
=======
from fastapi import APIRouter, Query, Response, Depends
from ..service.product_service import ProductService
from ..dependencies import get_product_service
>>>>>>> Stashed changes:src/controller/inventory_controller.py

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/health")
def fetch_store_inventory_health(store_id: str = Query(..., alias="store_id", description="Store ID")):
<<<<<<< Updated upstream:src/joi_delivery/controller/inventory_controller.py
    return Response(status_code=HTTPStatus.OK)
=======
    return Response(status_code=HTTPStatus.OK) 

@router.get("/product/search")
def fetch_grocery_product(
    product_name: str = Query(..., alias="product_name", description="product_name"),
    product_service: ProductService = Depends(get_product_service)
):
    products = product_service.search_product(product_name)
    return products
>>>>>>> Stashed changes:src/controller/inventory_controller.py
