from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.phone
        





    
