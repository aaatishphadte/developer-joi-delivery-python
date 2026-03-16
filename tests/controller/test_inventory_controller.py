import pytest
from fastapi.testclient import TestClient
from joi_delivery.main import app


class TestInventoryController:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_should_return_the_health_of_the_store(self, client):
        get_url = "/inventory/health?store_id=store101"

        response = client.get(get_url)
<<<<<<< Updated upstream

        # Then: Assert the response
=======
        
        # Assert the response
>>>>>>> Stashed changes
        assert response.status_code == 200
        
        data = response.json()
        
        # Verify response structure
        assert "store_id" in data
        assert "store_name" in data
        assert "total_products" in data
        assert "low_stock_count" in data
        assert "products" in data
        
        # Verify store details
        assert data["store_id"] == "store101"
        assert data["store_name"] == "Fresh Picks"
        
        # Verify products list
        assert isinstance(data["products"], list)
        assert data["total_products"] == len(data["products"])
        
        # Verify product structure if products exist
        if data["products"]:
            product = data["products"][0]
            assert "product_id" in product
            assert "product_name" in product
            assert "available_stock" in product
            assert "threshold" in product
            assert "is_low_stock" in product
            assert "mrp" in product
            assert "weight" in product
    
    def test_should_return_error_for_nonexistent_store(self, client):
        get_url = "/inventory/health?store_id=nonexistent_store"
        
        response = client.get(get_url)
        
        # Should still return 200 but with message about store not found
        assert response.status_code == 200
        
        data = response.json()
        assert data["store_id"] == "nonexistent_store"
        assert data["store_name"] is None
        assert data["total_products"] == 0
        assert len(data["products"]) == 0
