from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    blog_preview = models.ImageField(
        upload_to="preview/",
        verbose_name="превью записи блога",
        **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    is_published = models.BooleanField(verbose_name='признак публикации',
                                       default=True)
    views_count = models.PositiveIntegerField(verbose_name='кол-во просмотров',
                                              default=0)

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["title"]
        permissions = [
            ("can_edit_title", "Can edit title"),
            ("can_edit_content", "Can edit content"),
            ("can_edit_is_published", "Can edit is_published"),
        ]
