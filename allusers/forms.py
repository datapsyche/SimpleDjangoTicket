from django import forms
from allusers.models import allUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = allUser
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField()
    manager = forms.ModelChoiceField(queryset=allUser.objects.filter(is_staff=True))

    class Meta:
        model = allUser
        fields = ['username', 'email', 'password1', 'password2']

