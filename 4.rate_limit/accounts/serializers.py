
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usermodelss
        fields= ['username','password','email','phone']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields= '__all__'


    
    