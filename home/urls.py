
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.denneb_home, name="home_page")
]
