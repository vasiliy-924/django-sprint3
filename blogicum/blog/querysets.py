from django.utils.timezone import now


def filter_published(queryset):
    """Фильтрует QuerySet по критериям публикации."""
    return queryset.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now()
    ).select_related('category', 'location', 'author')
