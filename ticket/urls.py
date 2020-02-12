from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addticket', views.addticket, name="addticket"),
    path('adddepartment', views.adddepartment, name="adddepartment"),
    path('addfollowup', views.addfollowup, name="addfollowup")
]
