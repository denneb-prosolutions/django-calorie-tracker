from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from home import views

# Create your views here.
def signup(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect(views.denneb_home)
    else:    
      form = UserCreationForm()
    return render(request, 'accounts/signup.html' , {'form' : form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(views.denneb_home)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html' , {'form' : form})
      