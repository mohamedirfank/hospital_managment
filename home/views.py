from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Department,Docter
from .forms import BookingForm

# Create your views here.
@login_required()
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
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'confermation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def department(request):
    dep = {
        'dept' : Department.objects.all()
    }
    return render(request, 'department.html', dep)