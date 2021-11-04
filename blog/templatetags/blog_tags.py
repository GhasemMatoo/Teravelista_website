from django import template
from blog.models import post
register = template.Library()


@register.inclusion_tag("blog/includes/blog-Popular-Posts.html")
def popular_post (arg=3):
    posts=post.objects.filter(status=1).order_by("-published_date")[:arg]
    return {"posts":posts}
