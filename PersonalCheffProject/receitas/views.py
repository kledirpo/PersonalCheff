from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def receitas(request):
    return render(request, 'index.html')

def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')

def miojo(request):
    return render(request, 'miojo.html')

