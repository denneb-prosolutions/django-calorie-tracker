from django.shortcuts import render
from . import forms

# Create your views here.
def denneb_home(request):
    
    if request.method == "POST":
        form = forms.CreateFoods(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return render(request, 'home.html')
    else:
        form = forms.CreateFoods()
    return render(request, 'home.html' , {'foods_form' : form})