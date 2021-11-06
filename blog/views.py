from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import post
from datetime import datetime, timedelta
# Create your views here.


def blog_views(request, cat_name=None, author_username=None):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(
        published_date__gt=formatedDate).filter(status=1)
    if cat_name:
        Posts = Posts.filter(category__name=cat_name)
    if author_username:
        Posts = Posts.filter(author__username=author_username)
    Posts = Paginator(Posts, 3)
    page_number = request.GET.get('page')
    Posts=Posts.get_page(page_number)
    context = {'Posts': Posts}
    return render(request, 'blog/blog-home.html', context)


def single_views(request, pid):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(
        published_date__gt=formatedDate).filter(status=1)
    Post = get_object_or_404(Posts, id=pid)
    Post.counted_views = Post.counted_views + 1
    Post.save()
    context = {'Post': Post, 'Posts': Posts}
    return render(request, 'blog/blog-single.html', context)


def search_views(request):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(
        published_date__gt=formatedDate).filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get("s"):
            Posts = Posts.filter(content__contains=s)
    context = {'Posts': Posts}
    return render(request, 'blog/blog-home.html', context)
