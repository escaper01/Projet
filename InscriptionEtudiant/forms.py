from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

# class CreatNewUser(forms.ModelForm):
#     class Meta:
#         model = Etudiant
#         fields = {'nom' , 'prenom' ,'email' , 'phone','age','password', 'confirm_password' , 'pays'}
#         widgets = {
#             'nom' : forms.TextInput(attrs={'class': 'form-control'}),
#             'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
#             'email' : forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
#             'age' : forms.NumberInput(attrs={'class': 'form-control'}),
#             'password' : forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
#             'confirm_password' : forms.PasswordInput(attrs={'class': 'form-control'}),
#             'pays' : forms.TextInput(attrs={'class': 'form-control'}),
#         }


#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['email','mobile','age','status','matiere']



#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary','mobile','status']

#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()




#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'



#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))