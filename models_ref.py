from django.db import models
from allusers.models import allUser
from django.utils import timezone


# Create your models here.
STATUS_CHOICES = (
    ('IN QUEUE', 'IN QUEUE'),
    ('ASSIGNED', 'ASSIGNED'),
    ('PROCESSING', 'PROCESSING'),
    ('REJECTED', 'REJECTED'),
    ('APPROVED', 'APPROVED'),
    ('TRANSFERED', 'TRANSFERED'),
    ('ADDITIONAL INFO', 'ADDITIONAL INFO')
)

class Category(models.Model):
    name = models.CharField('category', max_length=255)
    subcategory = models.CharField('subcategory', max_length=255, null=True, blank=True)


class ServiceRequest(models.Model):
    owner = models.ForeignKey(allUser, related_name='owner', blank=True, null=True, verbose_name='Owner', on_delete=models.DO_NOTHING)
    description = models.TextField('description', blank=True, null=True)
    category = models.ForeignKey(Category, related_name="category", blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField('Status', choices=STATUS_CHOICES,
                              max_length=255, blank=True, null=True, default="IN QUEUE")
    waiting_for = models.ForeignKey(allUser, related_name='waiting_for', blank=True,
                                    null=True, verbose_name='Waiting For', on_delete=models.DO_NOTHING)
    closed_date = models.DateTimeField(blank=True, null=True)
    assigned_to = models.ForeignKey(allUser, related_name='assigned_to', blank=True,
                                    null=True, verbose_name='Assigned to', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    duedate = models.DateTimeField(null=True)
    extra = models.CharField('extra', max_length=1024, null=True, blank=True)
    

    def __unicode__(self):
        return str(self.id)


class Comment(models.Model):
    """
    A FollowUp is a comment to a ticket.
    """
    service_request = models.ForeignKey(
        ServiceRequest, verbose_name='ServiceRequest', on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Date', default=timezone.now)
    title = models.CharField('CommentTitle', max_length=200)
    text = models.TextField('CommentDetail', blank=True, null=True,)
    user = models.ForeignKey(allUser, blank=True, null=True,
                             verbose_name='User', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified', ]


class MarriageRegistration(models.Model):
    service_request = models.ForeignKey(ServiceRequest, verbose_name='ServiceRequest', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(allUser, blank=True, null=True, verbose_name='User', on_delete=models.DO_NOTHING)
    bride_name = models.CharField(
        'BrideName', max_length=200, blank=True, null=True,)
    bride_voter_id = models.CharField(
        'BrideVoterId', max_length=200, blank=True, null=True,)
    groom_name = models.CharField(
        'GroomName', max_length=200, blank=True, null=True,)
    groom_voter_id = models.CharField(
        'GroomVoterId', max_length=200, blank=True, null=True,)
    bride_address = models.CharField(
        'BrideAddress', max_length=200, blank=True, null=True,)
    groom_address = models.CharField(
        'GroomAddress', max_length=200, blank=True, null=True,)
    date = models.DateTimeField('Date', default=timezone.now)
    venue = models.CharField(
        'VenueAddress', max_length=200, blank=True, null=True,)
    marriage_reg_number = models.CharField('Marriage_reg_number', max_length=200)

    def _str_(self):
        return f"<MarriageRequest : {self.groom_name} and {self.bride_name} :: Request:{self.service_request}>"


GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

class BirthCertificate(models.Model):
    service_request = models.ForeignKey(ServiceRequest, verbose_name='ServiceRequest', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(allUser, blank=True, null=True, verbose_name='User', on_delete=models.DO_NOTHING)
    child_name = models.CharField(
        'ChildName', max_length=200, blank=True, null=True,)
    child_gender = models.CharField('Gender', choices=GENDER, max_length=255, blank=True, null=True)
    place_of_birth = models.CharField(
        'place_of_birth', max_length=200, blank=True, null=True,)
    date_of_birth = models.DateTimeField('Date', default=timezone.now)
    hospital_name = models.CharField(
        'place_of_birth', max_length=200, blank=True, null=True,)
    birth_reg_number = models.CharField(
        'birth_registration_number', max_length=200, blank=True, null=True,)

    def _str_(self):
        return f"<BirthCertificateRequest : {self.child_name} at {self.hospital_name} :: Request:{self.service_request}>"


    
            


