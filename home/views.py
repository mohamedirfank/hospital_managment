from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Docter

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def docters(request):
    docs = {
        'doct': Docter.objects.all()
    }
    return render(request, 'docters.html',docs)

def booking(request):
    return render(request, 'booking.html')

def department(request):
    dep = {
        'dept' : Department.objects.all()
    }
    return render(request, 'department.html', dep)