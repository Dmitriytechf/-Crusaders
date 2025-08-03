from django.urls import path
from homepage.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]