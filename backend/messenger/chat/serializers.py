from rest_framework import serializers
from .models import Message, Chat, Image
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['path']
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members']
class MessageSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    class Meta:
        model = Message, Image
        fields = ['id', 'text', 'image']