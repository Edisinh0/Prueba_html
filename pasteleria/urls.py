#from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('index', views.index, name='Index'),
    path('contacto', views.contacto, name='Contacto'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
]