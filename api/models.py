from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    info = models.TextField()
    
    def __str__(self):
        ret = self.user.username
        return ret


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        ret = self.name + ', ' + self.description
        return ret
    
    class Meta:
        ordering = ["created"]