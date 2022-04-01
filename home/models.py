from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Foods(models.Model):
    food_name = models.CharField(max_length=60)
    food_calory = models.FloatField()
    picture = models.FileField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
      return self.food_name

    def snippet(self):
      return self.body[:50]+'...'