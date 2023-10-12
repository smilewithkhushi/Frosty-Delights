from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),   
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services')
    #if the url is triggered with the page with particular name, eg, contact, then it goes to contact page

]
