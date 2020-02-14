from django.shortcuts import render, redirect
from ticket.models import ServiceRequest
from ticket.forms import  MarriageCertificateForm, BirthCertificateForm
import json


def home(request):
    print("Requester Role :", request.user.role)
    if request.user.role == 'ADMIN':
        service_requests = ServiceRequest.objects.all()
    elif request.user.role == 'PUBLIC':
         service_requests = ServiceRequest.objects.filter(owner=request.user)
    else:
        service_requests = ServiceRequest.objects.filter(assigned_to=request.user)
    context = {
        'service_requests': service_requests
    }
    return render(request, 'ticket/home.html', context)

def addmarriagecertificate(request):
    if request.method == 'POST':
        form = MarriageCertificateForm(request.POST)
        if form.is_valid():
            form.cleaned_data['marriage_date'] = str(form.cleaned_data['marriage_date'])
            service_request_json = json.dumps(form.cleaned_data)
            service_request_object = ServiceRequest(
                owner=request.user, description="Marriage Certificate", extra=service_request_json)
            service_request_object.save()
            return render(request, 'ticket/success.html', {'id':service_request_object.id})
    else:
        form = MarriageCertificateForm()
    return render(request, 'ticket/addmarriagecertificate.html', {'form': form})


def addbirthcertificate(request):
    if request.method == 'POST':
        form = BirthCertificateForm(request.POST)
        if form.is_valid():
            form.cleaned_data['date_of_birth'] = str(
                form.cleaned_data['date_of_birth'])
            service_request_json = json.dumps(form.cleaned_data)
            service_request_object = ServiceRequest(
                owner=request.user, description="Birth Certificate", extra=service_request_json)
            service_request_object.save()
            return render(request, 'ticket/success.html', {'id': service_request_object.id})
    else:
        form = BirthCertificateForm()
    return render(request, 'ticket/addbirthcertificate.html', {'form': form})




# def about(request):
#     return render(request, 'ticket/about.html', {'title': 'About'})


# def addticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = TicketForm()
#     return render(request, 'ticket/addticket.html', {'form': form})

# def adddepartment(request):
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DepartmentForm()
#     return render(request, 'ticket/adddepartment.html', {'form': form})

# def addfollowup(request):
#     if request.method == 'POST':
#         form = MarriageCertificateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = MarriageCertificateForm()
#     return render(request, 'ticket/addmarriagecertificate.html', {'form': form})

# def showticket(request, pk):
#     ticket = Ticket.objects.get(pk=pk)
#     return render(request, 'ticket/ticket.html', {'form': form})  
