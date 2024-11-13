from django.db import models

class post(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title