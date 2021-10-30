from django.db import models

# Create your models here.


class post(models.Model):
    # imag
    # author
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
