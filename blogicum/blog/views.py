from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .constants import POSTS_LIMIT
from .models import Category
from .querysets import get_published_posts


def index(request):
    post_list = get_published_posts()[:POSTS_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=now()
    ).select_related('category', 'location', 'author')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
