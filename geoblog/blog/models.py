from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join('images', 'avatars', str(instance.pk), filename)

class post(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title