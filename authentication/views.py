from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.Forms import RegisterForm,LoginForm

# Create your views here.

def login_View(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'authenticate/login.html')
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if '@' in username:
                kwargs = {'email': username.lower()}
            else:
                kwargs = {'username': username}
            try:
                username = User.objects.get(**kwargs).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'warning that invalid Username/Eimail and pssword')
                return render(request, 'authenticate/login.html')

    messages.add_message(request, messages.ERROR, 'warning that might need attention.')
    return render(request, 'authenticate/login.html',{'form': form})

@login_required(login_url='/authenticate/login')
def logout_View(request):
    logout(request)
    return redirect('/')

def register_View(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                form.save()
                return redirect('/authenticate/login')
        form = RegisterForm()
        return render(request, 'authenticate/register.html',{'form': form})
    else:
        return redirect('/')
