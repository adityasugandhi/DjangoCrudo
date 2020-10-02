from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Curd
from .serializers import Curds
# Create your views here.

@api_view(['GET'])
def Customerview(request):
   Curd_urls = { 
    'Customerlist': '/customer_list/' ,
    'CustomerDetail': '/customer-detail/',
    'CustomerCreate': '/customer-create',
    'CustomerUpdate': '/customer-update/',
    'CustomerDelete': '/customer-delete/',
   }

@api_view(['GET'])
def Customerlist(request):
    Customer = Curd.objects.all()
    serializer = Curds(Customer, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def CustomerDetail(request, pk):
    Customer = Curd.objects.get(id=pk)
    serializer = Curds(Customer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CustomerCreate(request):
    serializer =  Curds(data = request.data)
    if serializer.is_valid():
         serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def CustomerUpdate(request, pk):
    Customer = Curd.objects.get(id=pk)
    serializer = Curds(instance= Customer, data = request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def CustomerDelete(request, pk):
    customer = Curd.objects.get(id=pk)
    customer.delete()

    return Response('Deleted Succesfully')

    