from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, EmployeeRegisterForm, AnnouncementForm, LeaveOfficerForm
from allusers.models import allUser

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['is_public'] = True
            form.cleaned_data['role'] = 'PUBLIC'
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'alluser/register.html', {'form': form})

def new_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['role']='EMPLOYEE'
            form.cleaned_data['is_staff'] = True
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Officer account has been created! You are now able to log in using your email and password')
            return redirect('login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'alluser/register.html', {'form': form})

def new_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'New Announcement Added, It will be visible in Side Panel')
            return redirect('home')
    else:
        form = AnnouncementForm()
    return render(request, 'alluser/addannouncement.html', {'form': form})


def new_leaveofficer(request):
    if request.method == 'POST':
        form = LeaveOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Officer on Leave added to Side Panel')
            return redirect('home')
    else:
        form = LeaveOfficerForm()
    return render(request, 'alluser/addleaveofficer.html', {'form': form})


