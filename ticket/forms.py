from django.forms import ModelForm, Form, CharField, ChoiceField, DateField, FileField, ImageField, IntegerField, ModelChoiceField
from ticket.models import Category, ServiceRequest, Comment
from django.conf import settings


class MarriageCertificateForm(Form):
    bride_name = CharField(label="Name of Bride", required=True)
    groom_name = CharField(label="Name of Groom", required=True)
    bride_aadhar_no = IntegerField(label="Aadhar Card of Bride", required=True)
    groom_aadhar_no = IntegerField(label="Aadhar Card of Groom", required=True)
    bride_address = CharField(label="Full Address of Bride", required=True)
    groom_address = CharField(label="Full Address of Groom", required=True)
    marriage_date = DateField(label="Date of Marriage", required=True, input_formats=getattr(settings, 'DATE_INPUT_FORMATS'))
    venue = CharField(label="Venue of Marriage", required=True)

class BirthCertificateForm(Form):
    child_name = CharField(label="Name of Child", required=True)
    child_gender = ChoiceField(label="Gender", choices=(('MALE','MALE'),('FEMALE','FEMALE')))
    place_of_birth = CharField(label="Place of Birth", required=True)
    date_of_birth = DateField(label="Date of Birth", required=True, input_formats=getattr(settings, 'DATE_INPUT_FORMATS'))
    hospital_name = CharField(label="Hospital Name", required=True)
    birth_reg_number = IntegerField(label="Hospital Birth Registration Number", required=True)


class ServiceRequestForm(ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['description', 'status', 'category',
                'closed_date',]

class ServiceReassignForm(ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['description', 'status', 'category',
                  'closed_date', 'assigned_to']

