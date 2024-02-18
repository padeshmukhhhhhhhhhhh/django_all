from django.shortcuts import render,redirect
from .forms import second
from .models import main
# Create your views here.
def chart(request):
    main1=main.objects.all()
    data={'second':second,
          'main1':main1}
    print(data)
    if request.method == "POST":
        data1=second(request.POST)
        data1.save()
        return redirect("chart")
        
    
    return render(request,"home.html",data)