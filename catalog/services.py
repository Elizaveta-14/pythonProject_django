from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHES_ENABLED


class ProductService:
    @staticmethod
    def get_products_from_category(category_id):
        return Product.objects.filter(category_id=category_id).select_related(
            "category"
        )

    @staticmethod
    def get_products_from_cache():
        if not CACHES_ENABLED:
            return Product.objects.all()
        products = cache.get("product_list")
        if not products:
            products = Product.objects.all()
            cache.set("product_list", products)
            return products
        return products