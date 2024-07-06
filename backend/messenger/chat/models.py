from django.db import models
from user.models import CustomUser

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(CustomUser)

class Message(models.Model):
    text = models.CharField(max_length=500)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Image(models.Model):
    path = models.ImageField(upload_to='images/', null=True, blank=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
