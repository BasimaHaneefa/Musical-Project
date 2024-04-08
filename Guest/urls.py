from django.contrib import admin
from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [

   path('MusicalBandRegistration/',views.MusicalBandRegistration,name="MusicalBandRegistration"),
   path('FreelancerRegistration/',views.FreelancerRegistration,name="FreelancerRegistration"),

   path('NewUser/',views.userRegistration,name="userRegistration"),
   path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

    path('Login/',views.Login,name="Login"),

    path('',views.Index,name="Index"),
]