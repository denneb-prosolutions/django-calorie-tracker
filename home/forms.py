from django import forms
from . import models

class CreateFoods(forms.ModelForm):

    class Meta:
        model = models.Foods
        fields = ("food_name", "food_calory" , "picture",)

