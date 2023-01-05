from django.contrib.auth.models import User, Group
from django.utils.text import Truncator
from rest_framework import serializers
from base.models import Post, Tag

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', "last_name", "is_staff"]

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']

class PostSerializer(serializers.ModelSerializer):
    uploader = SimpleUserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'tag', 'uploader', 'content']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']