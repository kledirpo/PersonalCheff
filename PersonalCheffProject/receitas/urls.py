from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/', views.receitas, name='receitas'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
    path('miojo', views.miojo, name='miojo'),
    path('bolodefuba', views.bolodefuba, name='bolodefuba'),
    path('salada', views.salada, name='salada'),
    path('contato', views.contato, name='contato')
]
