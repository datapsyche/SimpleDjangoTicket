from django.shortcuts import render, redirect
from ticket.models import Ticket, Department, FollowUp
from ticket.forms import TicketForm, DepartmentForm, FollowUpForm


def home(request):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'ticket/home.html', context)


def about(request):
    return render(request, 'ticket/about.html', {'title': 'About'})


def addticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'ticket/addticket.html', {'form': form})

def adddepartment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepartmentForm()
    return render(request, 'ticket/adddepartment.html', {'form': form})

def addfollowup(request):
    if request.method == 'POST':
        form = FollowUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FollowUpForm()
    return render(request, 'ticket/addfollowup.html', {'form': form})

def showticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'ticket/ticket.html', {'form': form})


