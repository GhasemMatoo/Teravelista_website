from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    path("", blog_views, name='home'),
    path("<int:pid>", single_views, name='single'),
    path("category/<str:cat_name>", blog_views, name='category'),
    path("Tag/<str:tag_name>", blog_views, name='Tag'),
    path("author/<str:author_username>", blog_views, name='author'),
    path("search/", search_views, name='search'),

]
