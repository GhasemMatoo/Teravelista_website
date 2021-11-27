from django.forms import ModelForm
from blog.models import comment
from captcha.fields import CaptchaField

class commentForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = comment
        fields = ['name', 'email', 'messages', 'subject']