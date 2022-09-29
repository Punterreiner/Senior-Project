from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'EACalculator/index.html')

def results(request):
    return render(request, 'EACalculator/results.html')

def feedback(request):
    return render(request, 'EACalculator/feedback.html')