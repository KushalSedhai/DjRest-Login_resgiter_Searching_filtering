from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from .serializer import UserSerializer, StudentSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from .models import Student
from rest_framework.permissions import AllowAny, DjangoModelPermissions

# Create your views here.

@api_view(['POST',])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("user is created")
    else:
        return Response(serializer.erros)

@api_view(['POST',])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username = email, password= password)
    
    if user ==  None:
        return Response("Credentials wrong")
    else:
        token,_= Token.objects.get_or_create(user=user)
        return Response(token.key)

class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['name']
    search_fields = ['name']