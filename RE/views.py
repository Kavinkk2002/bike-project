from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.template import loader

from .models import kk1
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegisterationForm

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created. You can login now!')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    context = {'form':form} 
    return render(request,"register.html",context)

def fun(request):
    return HttpResponse("hello Welcome to my webpage")

def fun1(request):
    return HttpResponse("Royal Enfield")

def index(request):
    mydata=kk1.objects.all()
    if mydata!="":
        return render(request,"index.html",{"datas":mydata})
    else:
        return render(request,"index.html")

def bike(request):
    template=loader.get_template('bike.html')
    return HttpResponse(template.render())

def gt(request):
    template=loader.get_template('gt.html')
    return HttpResponse(template.render())

def inter(request):
    template=loader.get_template('inter.html')
    return HttpResponse(template.render())

def hunter(request):
    template=loader.get_template('hunter.html')
    return HttpResponse(template.render())

def bullet(request):
    template=loader.get_template('bullet.html')
    return HttpResponse(template.render())

def addData(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        department=request.POST["dep"]
        address=request.POST["add"]

        obj=kk1()
        obj.Name=name
        obj.Age=age
        obj.Department=department
        obj.Address=address
        obj.save()
        mydata=kk1.objects.all()
        return redirect("index")
    return render(request,"index.html")

def updateData(request,id):
    mydata=kk1.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        department=request.POST["department"]
        address=request.POST["address"]

        mydata.Name=name
        mydata.Age=age
        mydata.Department=department
        mydata.Address=address
        mydata.save()
        return redirect("index")
    return render(request,"update.html",{"data":mydata})

def deleteData(request,id):
    mydata=kk1.objects.get(id=id)
    mydata.delete()
    return redirect("index")

# Create your views here.
