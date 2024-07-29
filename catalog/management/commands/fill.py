from django.core.management import BaseCommand
import json
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def read_data_from_json():
        with open('catalog_dump.json', encoding='utf-16') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        data = self.read_data_from_json()

        products_for_creation = []
        categories_for_creation = []

        for obj in data:
            if obj['model'] == 'catalog.category':
                categories_for_creation.append(
                    Category(
                        pk=obj['pk'],
                        name=obj['fields']['name'],
                        description=obj['fields']['description']
                    )
                )
            elif obj['model'] == 'catalog.product':
                products_for_creation.append(
                    Product(
                        pk=obj["pk"],
                        name=obj["fields"]["name"],
                        description=obj["fields"]["description"],
                        preview=obj["fields"]["preview"],
                        category=Category(pk=obj["pk"]),
                        price=obj["fields"]["price"],
                        created_at=obj["fields"]["created_at"],
                        updated_at=obj["fields"]["updated_at"],
                    )
                )

        Category.objects.bulk_create(categories_for_creation)
        Product.objects.bulk_create(products_for_creation)