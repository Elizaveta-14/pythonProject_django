from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Очистить таблицы Category и Product и добавить новые продукты'

    def handle(self, *args, **options):
        # Удаляем старые записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING('Старые продукты и категории удалены.'))

        # Создаём новую категорию
        category = Category.objects.create(name='Техника', description='планеты')

        # Новый список продуктов
        products = [
            {
                "name": "Планшет",
                "description": "Самсунг",
                "image": "",
                "category": category,
                "price": 105000,
                "created_at": "2025-05-08",
                "updated_at": "2025-05-08"
            },
            {
                "name": "Планшет",
                "description": "Самсунг",
                "image": "",
                "category": category,
                "price": 100000,
                "created_at": "2025-05-08",
                "updated_at": "2025-05-08"
            }
        ]

        # Добавляем продукты
        for product_data in products:
            product = Product.objects.create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Добавлен продукт: {product.name}'))