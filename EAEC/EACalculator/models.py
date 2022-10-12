from django.db import models
from django.urls import reverse
from django.forms import ModelForm

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

    def __str__(self):
        return self.field_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class FieldsForm(ModelForm):
    class Meta:    
        model = Fields
        fields = ['age', 'spare_money', 'free_time', 'fitness']