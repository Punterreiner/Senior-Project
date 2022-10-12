from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import Fields
# Create your views here.

def index(request):
    if request.method == "POST":
        form = Fields(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            spare_money = form.cleaned_data['spare_money']
            free_time = form.cleaned_data['free_time']
            fitness = form.cleaned_data['fitness']
            dict = {'age':age, 'spare_money': spare_money,'free_time':free_time,'fitness': fitness}
            return render(request, 'EACalculator/results.html', dict)
            
    else:
        form = Fields()

    return render(request, 'EACalculator/index.html', {'form':form})

def results(request):
    return render(request, 'EACalculator/results.html')

def feedback(request):
    return render(request, 'EACalculator/feedback.html')