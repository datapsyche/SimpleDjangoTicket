from django.shortcuts import render, redirect, get_object_or_404
from ticket.models import ServiceRequest
from allusers.models import Announcement, LeaveOfficer
from ticket.forms import MarriageCertificateForm, BirthCertificateForm, ServiceRequestForm, ServiceReassignForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView
import json

def home(request):
    if request.user.is_authenticated:
        print("Requester Role :", request.user.role)
        if request.user.role == 'ADMIN':
            service_requests = ServiceRequest.objects.all()
        elif request.user.role == 'PUBLIC':
            service_requests = ServiceRequest.objects.filter(owner=request.user)
        else:
            service_requests = ServiceRequest.objects.filter(assigned_to=request.user)
        
        for service_request in service_requests:
            setattr(service_request, 'data', json.loads(service_request.extra))      

        context = {
            'service_requests': service_requests,
            'announcements' : Announcement.objects.all(),
            'leave_officers': LeaveOfficer.objects.all()
        }
    else:
        messages.warning(
            request, f'You donot have the permission to view the content, Please login to the system')
        context={
            'announcements': Announcement.objects.all(),
            'leave_officers': LeaveOfficer.objects.all()
        }
    return render(request, 'ticket/home.html', context)


def ticketinfo(request, num):
    if request.user.is_authenticated:
        service_request_object = get_object_or_404(ServiceRequest, pk=num)
        setattr(service_request_object, 'data',json.loads(service_request_object.extra))
        context = {
            'service_request': service_request_object,
            'announcements': Announcement.objects.all(),
            'leave_officers': LeaveOfficer.objects.all()
        }
        if request.user.role == 'PUBLIC':
            return render(request, 'ticket/item.html', context=context)
        elif request.user.role == 'EMPLOYEE':
            form = ServiceRequestForm(request.POST or None, instance=service_request_object)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                messages.success(request, f'Service Request has been edited')
            context['form'] = form            
            return render(request, 'ticket/edit.html', context=context)
        else:
            form = ServiceReassignForm(request.POST or None, instance=service_request_object)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                messages.success(request, f'Service Request has been edited')                
            context['form'] = form
            return render(request, 'ticket/edit.html', context=context)

    else:
        messages.warning(request, f'You donot have the permission to view the request')
        return render(request, 'ticket/edit.html', context=context)

def addmarriagecertificate(request):
    if request.method == 'POST':
        form = MarriageCertificateForm(request.POST)
        if form.is_valid():
            form.cleaned_data['marriage_date'] = str(form.cleaned_data['marriage_date'])
            service_request_json = json.dumps(form.cleaned_data)
            service_request_object = ServiceRequest(
                owner=request.user, description="Marriage Certificate", extra=service_request_json)
            service_request_object.save()
            setattr(service_request_object, 'data', json.loads(service_request_object.extra))
            messages.success(request, f'Marriage Certficate Request is generated with id : { service_request_object.id} ')
            context = {
                        'service_request': service_request_object,
                        'announcements': Announcement.objects.all(),
                        'leave_officers': LeaveOfficer.objects.all()
                       }
            return render(request, 'ticket/item.html', context)
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
            setattr(service_request_object, 'data',
                    json.loads(service_request_object.extra))
            messages.success(request, f'Birth Certficate Request is generated with id : { service_request_object.id} ')
            context = {
                'service_request': service_request_object,
                'announcements': Announcement.objects.all(),
                'leave_officers': LeaveOfficer.objects.all()
            }
            return render(request, 'ticket/item.html', context)
    else:
        form = BirthCertificateForm()
    return render(request, 'ticket/addbirthcertificate.html', {'form': form})



def search(request):
    query = request.GET.get('q')
    service_request = get_object_or_404(ServiceRequest, pk=query)
    setattr(service_request, 'data', json.loads(service_request.extra))
    context={
        'service_request': service_request
    }
    return render(request, 'ticket/item.html', context)

def escalate(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    setattr(service_request, 'data', json.loads(service_request.extra))
    service_request.status = "ESCALATE"
    service_request.save()
    context = {
        'service_request': service_request
    }
    return render(request, 'ticket/item.html', context)


