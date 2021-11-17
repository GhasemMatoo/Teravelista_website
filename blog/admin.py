from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post,category,comment
# Register your models here.


class postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_dispyley = '-empty-'
    list_display = ('title','author', 'counted_views', 'status','published_date', 'created_date')
    list_filter = ('status','author')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

class commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_dispyley = '-empty-'
    list_display = ('name','email', 'approved', 'created_date')
    list_filter = ('messages','subject')
    search_fields = ('name', 'messages')



admin.site.register(comment,commentadmin)
admin.site.register(post,postadmin)
admin.site.register(category)

