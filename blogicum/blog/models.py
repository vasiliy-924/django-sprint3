from django.db import models
from django.contrib.auth import get_user_model

from .constants import (
    DEFAULT_STR_LENGTH,
    PUBLISHED_HELP_TEXT,
    POST_TITLE_MAX_LENGTH,
    CATEGORY_TITLE_MAX_LENGTH,
    CATEGORY_SLUG_MAX_LENGTH,
    LOCATION_NAME_MAX_LENGTH
)

User = get_user_model()


class PublishedCreatedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text=PUBLISHED_HELP_TEXT
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Post(PublishedCreatedModel):
    title = models.CharField(
        max_length=POST_TITLE_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем — '
                   'можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='posts'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='posts'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:DEFAULT_STR_LENGTH]


class Category(PublishedCreatedModel):
    title = models.CharField(
        max_length=CATEGORY_TITLE_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        max_length=CATEGORY_SLUG_MAX_LENGTH,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:DEFAULT_STR_LENGTH]


class Location(PublishedCreatedModel):
    name = models.CharField(
        max_length=LOCATION_NAME_MAX_LENGTH,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:DEFAULT_STR_LENGTH]
