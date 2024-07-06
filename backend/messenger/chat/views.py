from .models import Chat, Message, Image
from rest_framework.decorators import api_view
from .serializers import ChatSerializer, MessageSerializer, ImageSerializer
from rest_framework import generics
from rest_framework import permissions

class IsMemberOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.member == request.user

class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(members=self.request.user)
    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user.id)
    
class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberOrReadOnly]
    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user.id)