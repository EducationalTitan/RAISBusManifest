from django import forms
from .models import BusManifest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BusManifestForm(forms.ModelForm):
    class Meta:
        model = BusManifest
        fields = '__all__'
        widgets = {
            'departure_time': forms.TimeInput(attrs={'type': 'time'}),
            'arrival_time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
