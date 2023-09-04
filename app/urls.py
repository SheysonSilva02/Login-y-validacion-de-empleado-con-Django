from django.urls import path
from. views import home,listar,modif,registro

urlpatterns = [
    path('', home, name= "home"),
    path('listar/', listar, name= "listar"),
    path('modif/<id>/', modif, name= "modif"),
    path('registro/<id>/', registro, name = "registro"),
]