from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_cloth(request):
        clothmodel_obj = clothmodel.objects.all()
        serializer = clothmodelserializer(clothmodel_obj, many=True)
        return Response(serializer.data)
@api_view(['POST'])
def post_cloth(request):
        clothmodel_obj = clothmodel.objects.all()
        serializer = clothmodelserializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
@api_view(['POST'])
def update_cloth(request,id):
        clothmodel_obj = clothmodel.objects.get(id=id )
        serializer = clothmodelserializer(instance=clothmodel_obj,data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
@api_view(['DELETE'])
def delete_cloth(request,id):
        clothmodel_obj = clothmodel.objects.get(id=id )
        clothmodel_obj.delete()
        return Response("The requriment is fullfilled")

    
    

        