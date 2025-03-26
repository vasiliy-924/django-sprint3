from django.utils.timezone import now

from .models import Post


def get_published_posts():
    """Возвращает QuerySet опубликованных постов с оптимизацией запросов."""
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now()
    ).select_related('category', 'location', 'author')
