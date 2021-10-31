from django.contrib import admin
from blog.models import post
# Register your models here.


class postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_dispyley = '-empty-'
    list_display = ('title','author', 'counted_views', 'status','published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ('title', 'content')


admin.site.register(post,postadmin)
