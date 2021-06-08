from django.db import models

# Create your models here.


from django.contrib.auth.models import User, AbstractUser, Group


class User(AbstractUser):
    pass


class Register(models.Model):
    name = models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    phone= models.CharField(max_length=12)
    address=models.TextField()
    date= models.DateField()
    
    def __str__(self):
        return self.name
    
