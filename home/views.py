from django.shortcuts import render

# Create your views here.
def denneb_home(request):
    return render(request, 'home.html')