<<<<<<< Updated upstream:src/joi_delivery/dependencies.py
from fastapi import Request

from joi_delivery.service.cart_service import CartService
from joi_delivery.service.product_service import ProductService
from joi_delivery.service.user_service import UserService
=======
from fastapi import Depends, Request
from src.service.cart_service import CartService
from src.service.user_service import UserService
from src.service.product_service import ProductService
from src.service.inventory_service import InventoryService
>>>>>>> Stashed changes:src/dependencies.py


def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


def get_product_service(request: Request) -> ProductService:
    return request.app.state.product_service


def get_cart_service(request: Request) -> CartService:
    return request.app.state.cart_service


def get_inventory_service(request: Request) -> InventoryService:
    return request.app.state.inventory_service
