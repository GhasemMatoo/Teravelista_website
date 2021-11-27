from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def login_View(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'authenticate/login.html')
        if request.method =='POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        messages.add_message(request, messages.ERROR, 'warning that might need attention.')
        return render(request, 'authenticate/login.html',{'form': form})
    else:
        return redirect('/')

@login_required(login_url='/authenticate /login')
def logout_View(request):
    logout(request)
    return redirect('/')

def register_View(request):
    return render(request, 'authenticate/register.html')
