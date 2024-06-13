from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.vypis_tem, name='temy'),
    path('', views.tema_list, name='temy'),
    path('temy/<tema>', views.vypis_temy, name='tema'),
    path('ucitelia/<ucitel>', views.vypis_ucitela, name='ucitel'),
    path('studenti/<student>', views.vypis_studenta, name='student'),
    path('statistics', views.statistics, name='statistics'),
    path('tema/create', views.pridat_temu, name='pridat_temu'),
]