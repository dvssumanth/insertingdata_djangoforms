from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *

def insert_student(request):
    sfo=StudentForm()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            sname=sfd.cleaned_data['sname']
            sid=sfd.cleaned_data['sid']
            semail=sfd.cleaned_data['semail']
            so=Student.objects.get_or_create(sname=sname,sid=sid,semail=semail)[0]
            so.save()
            qsd=Student.objects.all()
            d1={'qsd':qsd}
            return render(request,'disp.html',d1)
    return render(request,'insert_student.html',d)