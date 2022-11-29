from django import forms
from .models import Feedback 

levels = (
    ('poor','POOR'),
    ('ok', 'OK'),
    ('good','GOOD'),
    ('excellent','EXCELLENT')
)

yes_no = (('yes', 'YES'), ('no','NO'))

class Fields(forms.Form):
    age = forms.CharField(widget= forms.NumberInput(attrs={'placeholder': 'Enter a number'}), max_length=50)
    spare_Money = forms.CharField(widget= forms.NumberInput(attrs={'placeholder': 'Enter a number'}), max_length=50)
    free_Time = forms.CharField(widget= forms.NumberInput(attrs={'placeholder': 'hours per week'}), max_length=50)
    fitness = forms.ChoiceField(choices=levels)
    near_Water = forms.ChoiceField(choices=yes_no)
    #contribution_Level = forms.ChoiceField(choices = levels)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []