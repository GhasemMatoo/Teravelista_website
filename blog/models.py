from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    # imag
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=False)


class Meta:
    ordreing = ['-created_date']

    def __str__(self):
        return self.title
