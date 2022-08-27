from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Seja bem vindo.")

def receitas(request):
    return HttpResponse("Aqui estão minhas receitas")