from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('newannouncement/', views.new_announcement, name="new_announcement"),
    path('employeeregistration/', views.new_employee, name='new_employee'),
    path('newleaveofficer/', views.new_leaveofficer, name='new_leaveofficer')
]
