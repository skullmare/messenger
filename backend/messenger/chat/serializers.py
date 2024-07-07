from rest_framework import serializers
from .models import Chat, Message, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'path']  # Включаем поле id для обратной связи

class MessageSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, required=False)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Message
        fields = ['id', 'text', 'chat', 'user', 'files', 'date', 'time']

    def create(self, validated_data):
        files_data = validated_data.pop('files', [])  # Извлекаем данные файлов
        message = Message.objects.create(**validated_data)  # Создаем сообщение

        for file_data in files_data:
            file = File.objects.create(path=file_data['path'])  # Создаем каждый файл
            message.files.add(file)  # Добавляем файл к сообщению

        return message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members']