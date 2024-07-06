from django.contrib import admin
from .models import Chat, Message, Image
# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Image)