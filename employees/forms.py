from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['image', 'mobile', 'designation', 'gender', 'course']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')