# Generated by Django 4.2.2 on 2024-09-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price"],
                "permissions": [
                    ("can_edit_category", "Can edit category"),
                    ("can_edit_description", "Can edit description"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
