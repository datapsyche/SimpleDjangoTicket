from django.forms import ModelForm
from ticket.models import Ticket, FollowUp, Department


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = ['ticket', 'date', 'title',
                  'text', 'user']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'subdepartment']
