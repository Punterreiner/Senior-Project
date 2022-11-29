from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback, name='feedback'),
    path('results', views.results, name='results'),
    
]