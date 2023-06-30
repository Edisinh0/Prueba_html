#from django.conf.urls import url
from django.urls import path, include
from . import views 

urlpatterns = [
    path('index', views.index, name='Index'),
    path('contacto', views.contacto, name='Contacto'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('accounts/', include('django.contrib.auth.urls'))

]