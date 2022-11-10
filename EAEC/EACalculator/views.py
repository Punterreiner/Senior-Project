from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .selector import Selector, dataPicker
import pandas as pd

from .forms import Fields
# Create your views here.

def index(request):
    if request.method == "POST":
        form = Fields(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            spare_money = form.cleaned_data['spare_Money']
            free_time = form.cleaned_data['free_Time']
            fitness = form.cleaned_data['fitness']
            near_water = form.cleaned_data['near_Water']
            #contribution_level = form.cleaned_data['contribution_Level']
            selector = Selector(age, spare_money, free_time, fitness, near_water)
            profile = selector.profileSelector(age, spare_money, free_time, fitness)
            datepicker = dataPicker(profile, near_water)
            table = datepicker.getTable(profile, near_water)
            dict = {'age':age, 'spare_money': spare_money,'free_time':free_time,'fitness': fitness,'near_water':near_water, 'profile': profile, 'table': table}
            return render(request, 'EACalculator/results.html', dict)
            
    else:
        form = Fields()

    return render(request, 'EACalculator/index.html', {'form':form})

def results(request):
    return render(request, 'EACalculator/results.html')

def feedback(request):
    return render(request, 'EACalculator/feedback.html')

def table(request):
    return render(request, 'EACalculator/table.html')