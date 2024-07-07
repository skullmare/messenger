from django.db import models
from user.models import CustomUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Chat(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(CustomUser)

class File(models.Model):
    path = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.path.url

class Message(models.Model):
    text = models.CharField(max_length=500)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    files = models.ManyToManyField(File, blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    
    def __str__(self):
        return self.text
    
@receiver(pre_delete, sender=File)
def image_model_delete(sender, instance, **kwargs):
    if instance.path.name:
        instance.path.delete(False)