from django.contrib import admin
from .models import allUser, Announcement, LeaveOfficer
from django.contrib.auth.models import Group


# Register your models here.
class allUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    ordering = ('username',)
    search_fields = ('username','email')


admin.site.unregister(Group)
admin.site.register(allUser, allUserAdmin)
admin.site.register(Announcement)
admin.site.register(LeaveOfficer)

