from django.forms import ModelForm
from blog.models import comment

class commentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'email', 'messages', 'subject']