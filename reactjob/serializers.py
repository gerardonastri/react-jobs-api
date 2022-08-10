from rest_framework.serializers import ModelSerializer
from .models import Job
from .models import User


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
