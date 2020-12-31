from django.forms import TextInput

from django import forms



class NameForm(forms.Form):
    male = forms.CharField(label='Your male', max_length=100)
    female = forms.CharField(label='Your female', max_length=100)
    widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}

