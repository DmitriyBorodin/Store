# Generated by Django 4.2.2 on 2024-09-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Признак публикации"),
        ),
    ]
