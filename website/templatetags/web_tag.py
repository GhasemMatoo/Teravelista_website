from blog.models import post
from datetime import datetime, timedelta
from django import template

register = template.Library()

@register.inclusion_tag('website/includes/home_blog_area.html')
def web_posts(arg=6):
    time_now = datetime.now() + timedelta(days=1)
    formatedDate = time_now.strftime("%Y-%m-%d")
    Posts = post.objects.exclude(
        published_date__gt=formatedDate).filter(status=1)[:arg]
    return {"Posts": Posts}
