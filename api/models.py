from django.db import models

# Create your models here.


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