from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, permissions
from .models import Chat, Message, File
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.serializers import ValidationError
from django.utils import timezone

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        chat = serializer.save()
        chat.members.add(self.request.user)
        chat.save()
    
    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user.id)

class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user.id)

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    
    def perform_create(self, serializer):
        files_data = self.request.FILES.getlist('files')
        user = self.request.user
        chat_id = self.kwargs.get('chat_id')
        date = timezone.now().date()
        time = timezone.now().time()

        chat = Chat.objects.filter(id=chat_id).first()
        if not chat:
            raise ValidationError({"chat": "Chat with this ID does not exist."})

        if not chat.members.filter(id=user.id).exists():
            raise ValidationError({"chat": "You are not a member of this chat."})

        message = serializer.save(user=user, chat=chat, date=date, time=time)

        for file_data in files_data:
            file = File.objects.create(path=file_data)
            message.files.add(file)

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id, chat__members=self.request.user).order_by('date', 'time')

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user.id)