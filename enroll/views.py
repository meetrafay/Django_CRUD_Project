from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from enroll.forms import StudentRigistration
from enroll.models import User
from .models import User

# Create your views here.
def show(request):
    if request.method == 'POST':
        fm=StudentRigistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            am=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            reg=User(name=nm,email=am,password=pas)
            reg.save()
            fm=StudentRigistration()
    else:
        fm=StudentRigistration()
    stud= User.objects.all()
        
    return render(request,'enroll/updatestd.html',{'form':fm,'stu':stud})

def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentRigistration(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
            fm=StudentRigistration()
    else:
         pi = User.objects.get(pk=id)
         fm=StudentRigistration(instance=pi)
    return render(request,'enroll/addandshow.html',{'form':fm})

def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')