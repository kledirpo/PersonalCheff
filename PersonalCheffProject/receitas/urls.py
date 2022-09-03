from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/', views.receitas, name='receitas'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja')
    path('miojo', views.miojo, name='miojo')

]