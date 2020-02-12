from django.db import models
from allusers.models import allUser
from django.utils import timezone


# Create your models here.
STATUS_CHOICES = (
    ('TODO', 'TODO'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('WAITING', 'WAITING'),
    ('DONE', 'DONE'),
)

class Department(models.Model):
    name = models.CharField('department', max_length=255)
    subdepartment = models.CharField('subdepartment', max_length=255)


class Ticket(models.Model):
    title = models.CharField('title', max_length=255)
    owner = models.ForeignKey(allUser, related_name='owner', blank=True, null=True, verbose_name='Owner', on_delete=models.DO_NOTHING)
    description = models.TextField('description', blank=True, null=True)
    department = models.ForeignKey(Department, related_name="department", blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=255, blank=True, null=True)
    waiting_for = models.ForeignKey(allUser, related_name='waiting_for', blank=True,
                                    null=True, verbose_name='Waiting For', on_delete=models.DO_NOTHING)
    closed_date = models.DateTimeField(blank=True, null=True)
    assigned_to = models.ForeignKey(allUser, related_name='assigned_to', blank=True,
                                    null=True, verbose_name='Assigned to', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return str(self.id)


class FollowUp(models.Model):
    """
    A FollowUp is a comment to a ticket.
    """
    ticket = models.ForeignKey(
        Ticket, verbose_name='Ticket', on_delete=models.DO_NOTHING)
    date = models.DateTimeField('Date', default=timezone.now)
    title = models.CharField('Title', max_length=200,)
    text = models.TextField('Text', blank=True, null=True,)
    user = models.ForeignKey(allUser, blank=True, null=True,
                             verbose_name='User', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified', ]
