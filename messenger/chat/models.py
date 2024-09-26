from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Уникальное имя комнаты
    is_group = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='chat_members', blank=True)