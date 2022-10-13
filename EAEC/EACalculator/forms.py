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
    spare_money = forms.CharField(max_length=50)
    free_time = forms.CharField(max_length=50)
    fitness = forms.ChoiceField(choices=levels)
    near_water = forms.ChoiceField(choices=yes_no)
