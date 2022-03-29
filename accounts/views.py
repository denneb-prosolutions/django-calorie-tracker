from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from home import views

# Create your views here.
def signup(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        auth_login(request, user)
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

def logout(request):
    if request.method == 'POST':
      auth_logout(request)
      return redirect(views.denneb_home)

@login_required(login_url='/accounts/login')
def require_login(request):
    return render(request, 'accounts/required.html')