from django.shortcuts import get_object_or_404

from catalog.models import Category, Product


class ProductService:
    """Сервис для создания списка продуктов по категории."""

    def __init__(self, category_id: int):
        self.category_id = category_id
        self.category = get_object_or_404(Category, id=self.category_id)

    def get_products(self):
        """Получает список продуктов в указанной категории."""
        return Product.objects.filter(category=self.category).order_by("-views_counter")