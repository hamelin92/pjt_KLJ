from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ('id','username','nickname',)


class UserRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=10)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

    class Meta :
        model = get_user_model()
        fields = ('username','password1','password2','nickname')

