"""为应用程序users定义URL模式"""

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]