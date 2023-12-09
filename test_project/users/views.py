from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))