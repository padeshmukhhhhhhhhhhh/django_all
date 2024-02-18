from django.shortcuts import render,redirect
from .models import customer
from django.http import HttpResponse
# Create your views here.
def customerdata(request):
      
    data=customer.objects.all()
    dict={"data":data}
    return render(request, "index1.html",dict)


def adddata(request):
    data=customer.objects.all()
    dict={"data":data}
    if request.method == "POST":
        print("post")
        name=request.POST['name']
        address=request.POST['address']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        
        newuser=customer(name=name,Address=address,City=city,phone=phone,Email=email)
        newuser.save()
        return redirect("customerdata")   
    
def delete(request,id):
    if request.method=="POST":
        data=customer.objects.get(id=id)
        data.delete()
        return redirect("customerdata")   
    
def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        data=customer(id=id,name=name,Address=address,City=city,phone=phone,Email=email)
        data.save()
        return redirect("customerdata")       