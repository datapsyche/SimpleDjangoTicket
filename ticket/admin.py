from django.contrib import admin
from .models import Category, ServiceRequest, Comment
from django.contrib.auth.models import Group

# # Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory')
    ordering = ('name',)
    search_fields = ('name',)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'status','assigned_to','extra')
    ordering = ('created','updated')
    search_fields = ('extra',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'service_request', 'user')
    ordering = ('created',)
    search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(Comment, CommentAdmin)

