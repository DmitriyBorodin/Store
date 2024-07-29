from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='катерогия')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='продукт')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='catalog/preview', verbose_name='фото продукта', related_name='categories', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    price = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'price']
