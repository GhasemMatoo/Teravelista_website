from django.contrib import admin
from website.models import contact,NEWSLETTER
# Register your models here.


class contactadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('email', 'subject')
    search_fields = ('name','subject', 'massage')


admin.site.register(contact,contactadmin)
admin.site.register(NEWSLETTER)