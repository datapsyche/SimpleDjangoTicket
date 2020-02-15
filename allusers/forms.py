from django.forms import ModelForm
from django import forms
from allusers.models import allUser, Announcement, LeaveOfficer
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


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['text']


class LeaveOfficerForm(ModelForm):
    officer_on_leave = forms.ModelChoiceField(queryset=allUser.objects.filter(is_staff=True), label="Officer On Leave")

    class Meta:
        model = LeaveOfficer
        fields = ['officer_on_leave']

