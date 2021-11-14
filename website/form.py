from django import forms
from website.models import contact,NEWSLETTER

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NEWSLETTER
        fields = '__all__'