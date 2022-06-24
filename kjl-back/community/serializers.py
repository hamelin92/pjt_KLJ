from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article,Comment

class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer) :
        class Meta:
            model = get_user_model()
            fields = ('username',)
    
    user = UserSerializer(read_only=True)
    image = serializers.ImageField(use_url=True, required=False, default='community/None.jpg')
    
    class Meta :
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    
    user = UserSerializer(read_only=True)

    class Meta :
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = get_user_model()
            fields = ('username',)
    user = UserSerializer(read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta :
            model = Article
            fields = ('pk',)
            
    article = ArticleSerializer(read_only=True)
    
    class Meta :
        model = Comment
        fields = '__all__'