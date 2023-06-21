from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Doctor
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def doctor(request):
    dict_doctor = {
        'doc' : Doctor.objects.all()
    }
    return render(request,'doctor.html',dict_doctor)

def department(request):
    dict_department = {
        'dept' : Department.objects.all()
    }
    return render(request,'department.html', dict_department)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'forms' : form
    }
    return render(request, 'booking.html', dict_form)
