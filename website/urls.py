from django.contrib.sitemaps.views import sitemap
from django.urls import path

from website.views import *

app_name = 'website'

urlpatterns = [
    path("", index_views, name='index'),
    path("about", about_views, name='about'),
    path("contact", contact_views, name='contact'),
    path("NEWSLETTER", NEWSLETTER_views, name='NEWSLETTER'),

]
