from django.db import models

# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Meta:
    ordreing = ['-created_date']

    def __str__(self):
        return self.name
