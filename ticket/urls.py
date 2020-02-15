from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('addticket', views.addticket, name="addticket"),
    # path('adddepartment', views.adddepartment, name="adddepartment"),
    # path('addfollowup', views.addfollowup, name="addfollowup"),
    path('addmarriagecertificate', views.addmarriagecertificate, name="addmarriagecertificate"),
    path('addbirthcertificate', views.addbirthcertificate, name="addbirthcertificate"),
    path('ticket/<int:num>/', views.ticketinfo, name="showticketinfo"),
    path('search/', views.search, name='search'),
    path('ticket/<int:pk>/escalate/', views.escalate, name="escalate"),
]
