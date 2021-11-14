from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.form import ContactForm,NewsletterForm
from django.contrib import messages
# Create your views here.
def index_views(request):
    return render(request,'website/index.html')
    
def about_views(request):
    return render(request,'website/about.html')
    
def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = form.cleaned_data['name']='UNKNOW'
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Yor ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Yor ticket dident submited.')
    form= ContactForm()
    return render(request,'website/contact.html',{'form': form})

def NEWSLETTER_views(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    form=NewsletterForm()
    return render(request,'website/index.html',{'form': form})