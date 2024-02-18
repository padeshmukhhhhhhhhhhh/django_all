from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)



class Message(models.Model):
    room = models.ForeignKey(room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
