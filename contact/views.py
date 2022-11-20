from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ContactSerializer
from .models import Contact
# Create your views here.


@api_view(['POST'])
def message(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getData(request):
    data = Contact.objects.all()
    serializer = ContactSerializer(data, many=True)
    return Response(serializer.data)
