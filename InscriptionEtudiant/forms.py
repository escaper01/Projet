from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentExtra




#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']


#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=StudentExtra
        fields=['user','mobile','age','matiere','image']

