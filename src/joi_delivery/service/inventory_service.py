from typing import List, Optional
from ..domain.grocery_store import GroceryStore
from ..domain.grocery_product import GroceryProduct


class InventoryService:
    def __init__(self, stores: List[GroceryStore], products: List[GroceryProduct]):
        self.stores = stores
        self.products = products
    
    def get_store_by_id(self, store_id: str) -> Optional[GroceryStore]:
        """Get store by ID"""
        for store in self.stores:
            if store.outlet_id == store_id:
                return store
        return None
    
    def get_products_for_store(self, store_id: str) -> List[GroceryProduct]:
        """Get all products for a specific store"""
        return [
            product for product in self.products 
            if product.store and product.store.outlet_id == store_id
        ]
    
    def get_store_inventory_health(self, store_id: str) -> dict:
        """
        Get inventory health for a store.
        Returns store info and products with their health status.
        Products are flagged as low_stock if available_stock <= threshold.
        """
        store = self.get_store_by_id(store_id)
        if not store:
            return {
                "store_id": store_id,
                "store_name": None,
                "message": "Store not found",
                "products": []
            }
        
        products = self.get_products_for_store(store_id)
        
        product_health_items = []
        for product in products:
            is_low_stock = product.available_stock <= product.threshold
            product_health_items.append({
                "product_id": product.product_id,
                "product_name": product.product_name,
                "available_stock": product.available_stock,
                "threshold": product.threshold,
                "is_low_stock": is_low_stock,
                "mrp": product.mrp,
                "weight": product.weight
            })
        
        return {
            "store_id": store.outlet_id,
            "store_name": store.name,
            "total_products": len(products),
            "low_stock_count": sum(1 for item in product_health_items if item["is_low_stock"]),
            "products": product_health_items
        }
