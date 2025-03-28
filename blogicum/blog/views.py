from django.shortcuts import get_object_or_404, render

from .constants import POSTS_LIMIT
from .models import Category, Post
from .querysets import published_posts_filter


def index(request):
    post_list = published_posts_filter(Post.objects.all())[:POSTS_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        published_posts_filter(Post.objects.all()),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    post_list = published_posts_filter(category.posts.all())
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
