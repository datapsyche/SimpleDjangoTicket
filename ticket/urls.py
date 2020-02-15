from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = 'CTSS Administration'
admin.site.index_title = 'Advanced Features and Options'
admin.site.site_title = 'Centralized Transparent Service System Administration'



urlpatterns = [
    path('', views.home, name='home'),
    path('addmarriagecertificate', views.addmarriagecertificate, name="addmarriagecertificate"),
    path('addbirthcertificate', views.addbirthcertificate, name="addbirthcertificate"),
    path('ticket/<int:num>/', views.ticketinfo, name="showticketinfo"),
    path('search/', views.search, name='search'),
    path('ticket/<int:pk>/escalate/', views.escalate, name="escalate"),
]
