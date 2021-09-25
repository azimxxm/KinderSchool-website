from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Class', views.Class, name='Class'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Enroll_Now', views.Enroll_Now, name='Enroll_Now'),
]
