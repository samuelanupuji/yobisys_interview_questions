
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Usermodelss(AbstractUser):
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=12)


class Category(models.Model):
    name= models.CharField(max_length=255)
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')




