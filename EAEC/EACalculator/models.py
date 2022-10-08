from django.db import models

# Create your models here.

levels = (
    ('poor','POOR'),
    ('ok', 'OK'),
    ('good','GOOD'),
    ('excellent','EXCELLENT')
)

class Fields(models.Model):
    age = models.CharField(max_length=50)
    spare_money = models.CharField(max_length=50)
    free_time = models.CharField(max_length=50)
    fitness = models.CharField(max_length=50, choices=levels, default='poor')