from django.contrib import admin
from django.urls import path,include
from Home import views

admin.site.site_header = "Flipzon Admin"
admin.site.site_title = "Flipzon Admin Portal"
admin.site.index_title = "Welcome to Flipzon Insider Portal"

urlpatterns = [
   path("", views.index, name='Home'),
   path("home", views.index, name='Home'),
   path("contact", views.contact, name='contact'),
   path("dotd", views.dotd, name='dotd'),
   path("refur", views.refur, name='refur')
]