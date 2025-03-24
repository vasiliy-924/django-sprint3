from django.shortcuts import render
from django.http import Http404


def index(request):
    return render(request, 'blog/index.html', {'posts': list(reversed(posts))})


def post_detail(request, post_id):
    if post_id not in posts_by_id:
        raise Http404(f'Пост с ID {post_id} не найден.')
    return render(request, 'blog/detail.html', {'post': posts_by_id[post_id]})


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
