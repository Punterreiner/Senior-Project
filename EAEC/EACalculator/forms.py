from django import forms
from .models import Feedback 

levels = (
    ('poor','Poor'),
    ('ok', 'Ok'),
    ('good','Good'),
    ('excellent','Excellent')
)

yes_no = (('yes', 'Yes'), ('no','No'))

pol = (('U18', 'Under 18'),
        ('college','College'),
        ('working', 'Working'),
        ('retired', 'Retired'))

class Fields(forms.Form):
    spare_Money = forms.CharField(widget= forms.NumberInput(attrs={'placeholder': 'Enter a number'}), max_length=50)
    free_Time = forms.CharField(widget= forms.NumberInput(attrs={'placeholder': 'hours per week'}), max_length=50)
    age = forms.ChoiceField(choices=pol)
    fitness = forms.ChoiceField(choices=levels)
    near_Water = forms.ChoiceField(choices=yes_no)
    #contribution_Level = forms.ChoiceField(choices = levels)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []