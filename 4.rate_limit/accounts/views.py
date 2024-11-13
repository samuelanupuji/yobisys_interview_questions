from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from .models import *
from .serializers import *

# Create your views here.

class Userviews(generics.CreateAPIView):
    queryset= Usermodelss.objects.all()
    serializer_class= UserSerializer
    throttle_classes= [UserRateThrottle]

    def post(self, request):
        serializer= self.get_serializer(data= request.data)
        if serializer.is_valid():
            user=serializer.save()
            password= request.data.get('password')
            user.set_password(password)
            user.save()

            return Response({'message': 'sucessful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductsViews(generics.ListAPIView):
    queryset= Products.objects.all()
    serializer_class= ProductSerializer
    throttle_classes= [UserRateThrottle]

    def get_queryset(self):
        queryset=super().get_queryset()
        search_query= self.request.query_params.get('search', None)
        if search_query:
            queryset= queryset.filter(name__icontains= search_query)
        return queryset
    
    