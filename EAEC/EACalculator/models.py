from django.db import models
from django.urls import reverse
from django.forms import ModelForm

# Create your models here.

class Feedback(models.Model):
    email = models.EmailField()
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

