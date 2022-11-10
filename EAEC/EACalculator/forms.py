from django import forms

levels = (
    ('poor','POOR'),
    ('ok', 'OK'),
    ('good','GOOD'),
    ('excellent','EXCELLENT')
)

yes_no = (('yes', 'YES'), ('no','NO'))

class Fields(forms.Form):
    age = forms.CharField(max_length=50)
    spare_Money = forms.CharField(max_length=50)
    free_Time = forms.CharField(max_length=50)
    fitness = forms.ChoiceField(choices=levels)
    near_Water = forms.ChoiceField(choices=yes_no)
    contribution_Level = forms.ChoiceField(choices = levels)
