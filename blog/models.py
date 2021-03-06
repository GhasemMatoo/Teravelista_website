from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=False)

    def excerpt(self):
        return ' '.join(self.content.split()[:10])+'...'
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid' : self.id})
    
    def __str__(self):
        return self.title

class Meta:
    ordreing = ['-created_date']



class comment(models.Model):
    Poost = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    messages = models.TextField()
    approved = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
         
class Meta:
    ordreing = ['-created_date'] 

 
