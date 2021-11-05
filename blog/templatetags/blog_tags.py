from django import template
from blog.models import post, category
register = template.Library()


@register.inclusion_tag("blog/includes/blog-Popular-Posts.html")
def popular_post(arg=3):
    posts = post.objects.filter(status=1).order_by("-published_date")[:arg]
    return {"posts": posts}


@register.inclusion_tag("blog/includes/blog-Post-Catgories.html")
def category_cunter():
    posts = post.objects.filter(status=1)
    categoryes = category.objects.all()
    cat_dite = {}
    for name in categoryes:
        cat_dite[name]=posts.filter(category=name).count()
    return {'category':cat_dite}
