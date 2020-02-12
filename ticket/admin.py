from django.contrib import admin
from .models import Department,FollowUp,Ticket

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdepartment')
    ordering = ('name',)
    search_fields = ('name',)

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'title', 'user', 'text')
    ordering = ('created','modified')
    search_fields = ('title',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'department', 'status', 'waiting_for')
    ordering = ('created',)
    search_fields = ('title',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(FollowUp, FollowUpAdmin)
admin.site.register(Ticket, TicketAdmin)

