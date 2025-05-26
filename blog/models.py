from django.db import models


class Blog(models.Model):
    heading = models.CharField(
        max_length=50, verbose_name="Заголовок", help_text="Введите название заголовка"
    )

    content = models.TextField(max_length=400, verbose_name="Содержимое")

    preview = models.ImageField(
        upload_to="blogs/image", blank=True, null=True, verbose_name="Фото"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата последнего изменения"
    )

    publication_attribute = models.BooleanField(default=True)

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["heading", "created_at"]

    def __str__(self):
        return self.heading
