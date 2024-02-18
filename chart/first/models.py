from django.db import models

class main(models.Model):
    labels=models.CharField(max_length=300)
    data=models.IntegerField()