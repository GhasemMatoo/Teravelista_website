from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import post
from datetime import datetime, timedelta
# Create your views here.


def blog_views(requset):
    time_now=datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(published_date__gt=formatedDate).filter(status=1)
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
