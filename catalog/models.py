from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="катерогия")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="продукт")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(
        upload_to="preview/",
        verbose_name="фото продукта",
        **NULLABLE
    )
    category = models.ForeignKey(Category, on_delete=models.SET(0))
    price = models.IntegerField(verbose_name="цена")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    is_published = models.BooleanField(verbose_name="Признак публикации", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_is_published", "Can edit is_published"),
        ]

    owner = models.ForeignKey(User, verbose_name="Владелец",
                              blank=True, null=True, on_delete=models.SET_NULL)


class Version(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='версия',
        on_delete=models.SET_NULL,
        verbose_name='версия товара',
        **NULLABLE)

    version_number = models.PositiveIntegerField(
        verbose_name='Номер версии')

    version_name = models.CharField(
        max_length=150, verbose_name='Название версии')

    is_current = models.BooleanField(
        verbose_name='Признак текущей версии', default=True)

    owner = models.ForeignKey(User, verbose_name="Владелец",
                              blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
