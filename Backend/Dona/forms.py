from django import forms
from .models import *
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from . models import Image,Profile



    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
