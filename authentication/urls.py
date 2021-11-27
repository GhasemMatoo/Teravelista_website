from django.urls import  path
from . import views

app_name ="authenticate"

urlpatterns =[
    path('login',views.login_View, name='login'),
    path('logout',views.logout_View, name='logout'),
    path('register',views.register_View, name='register'),
]