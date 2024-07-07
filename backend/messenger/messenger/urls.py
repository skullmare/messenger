"""
URL configuration for messenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chat.views import ChatListCreateView, ChatDetailView, MessageListCreateView, MessageDetailView
from user.views import PasswordResetConfirmView, ActivationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('api/v1/chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('api/v1/chats/<int:chat_id>/messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('api/v1/messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('password_reset/<uid>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('activate/<uid>/<token>/', ActivationView.as_view(), name='activate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
