from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import  UserData , LoanRequest


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

class UserDataRegisterForm(forms.ModelForm):
	class Meta:
		model= UserData
		fields = ['firstName','lastName','city', 'state', 'pincode','address', 'email', 'residence_owned_by', 'employment_Details','occupation']

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ('category', 'reason', 'amount', 'year', 'accounting_provider')
