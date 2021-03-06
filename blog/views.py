from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import post, comment
from datetime import datetime, timedelta
from blog.Form import commentForm
from django.contrib import messages
# Create your views here.


def blog_views(request, **kwargs):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(published_date__gt=formatedDate).filter(
        status=1).order_by('-created_date')
    if kwargs.get('cat_name') != None:
        Posts = Posts.filter(category__name=kwargs.get('cat_name'))
    if kwargs.get('author_username') != None:
        Posts = Posts.filter(author__username=kwargs.get('author_username'))
    if kwargs.get('tag_name') != None:
        Posts = Posts.filter(tags__name__in=[kwargs.get('tag_name')])
    Posts = Paginator(Posts, 3)
    page_number = request.GET.get('page')
    Posts = Posts.get_page(page_number)
    context = {'Posts': Posts}
    return render(request, 'blog/blog-home.html', context)


def single_views(request, pid):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(
        published_date__gt=formatedDate).filter(status=1)
    Post = get_object_or_404(Posts, id=pid)
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.Poost_id = pid
            comments.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Yor Commets submited successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Yor Commets dident submited.')
    form = commentForm()
    Post.counted_views = Post.counted_views + 1
    Post.save()
    comments = comment.objects.filter(Poost=Post.id, approved=True)
    context = {'Post': Post, 'Posts': Posts,
               'comments': comments, 'form': form}
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
