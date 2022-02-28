"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from netlabv2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.netlav2,name="index"),
    path('guadardatosini/',views.guadardatosini),
    path('dtablePacientesNetLab/',views.dtablePacientesNetLab),
    path('buscarvacunado/',views.buscar_vacunado),
    path('guardarnegativo/',views.guardar_negativos),
    path('listarnegativos/',views.listar_negativos),
    path('actualizarnegativos/',views.actualizar_negativos),
    path('listaeess/',views.lista_eess),
    path('resumennegativos/',views.resumen__negativos),
    path('api/', include('apiRest.urls'))
    #path('selenium/',views.selenium)
]
