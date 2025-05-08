from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Техника', description='планеты')

        products = [
            {"name": "Планшет",
            "description": "Самсунг",
            "image": "",
            "category": category,
            "price": 105000,
            "created_at": "2025-05-08",
            "updated_at": "2025-05-08"},
            {"name": "Планшет",
             "description": "Самсунг",
             "image": "",
             "category": category,
             "price": 100000,
             "created_at": "2025-05-08",
             "updated_at": "2025-05-08"}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'successfully added product: {product.name}'))