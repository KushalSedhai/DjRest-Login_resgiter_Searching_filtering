from rest_framework.serializers import ModelSerializer
from .models import User, Student

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
        
class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'