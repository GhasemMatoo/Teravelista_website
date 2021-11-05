from django.shortcuts import render,get_object_or_404
from blog.models import post
from datetime import datetime, timedelta
# Create your views here.


def blog_views(requset,cat_name=None,author_username=None):
    time_now=datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(published_date__gt=formatedDate).filter(status=1)
    if cat_name:
        Posts=Posts.filter(category__name=cat_name)
    if author_username:
        Posts=Posts.filter(author__username=author_username)
    context = {'Posts': Posts}
    return render(requset, 'blog/blog-home.html', context)


def single_views(requset,pid):
    time_now=datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(published_date__gt=formatedDate).filter(status=1)
    Post =get_object_or_404(Posts,id=pid)
    Post.counted_views= Post.counted_views +1
    Post.save() 
    context = {'Post': Post,'Posts': Posts}
    return render(requset, 'blog/blog-single.html',context)
