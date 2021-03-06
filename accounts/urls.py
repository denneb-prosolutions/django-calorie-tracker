from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup , name='signup'),
    path('login', views.login , name='login'),
    path('logout', views.logout , name='logout'),
    path('required' ,views.require_login, name="require_login"),
]