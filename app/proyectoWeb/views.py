from django.shortcuts import render

# Create your views here.
def index(request):
    hola="hola mundo"
    return render(request,hola)