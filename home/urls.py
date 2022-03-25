
from django.urls import path
from . import views

urlpatterns = [
    path('', views.denneb_home, name="home")
]
