from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    mobile=models.IntegerField(null=True)
    dob=models.DateField(null=True)
    