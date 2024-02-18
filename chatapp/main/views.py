from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as ln ,logout as lo
from django.contrib.auth.decorators import login_required
from .models import room,Message

def signup(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')







def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
       

        # Authenticate against the default User model
        user_default = authenticate(request, username=username, password=password)

       
        if user_default is not None:
            # Authenticate using the default User model and log in
            ln(request, user_default)
            return redirect('rooms')  # Redirect to your home page or any other desired page
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def rooms(request):
    rooms = room.objects.all()
    data={'rooms': rooms}
    return render(request,"rooms.html",data)


def chat(request, id):
    room1 = room.objects.get(id=id)
    messages = Message.objects.filter(room=room1)[0:25]
    context={'room1': room1,
               'messages': messages}
   

    return render(request, 'chat.html',context)