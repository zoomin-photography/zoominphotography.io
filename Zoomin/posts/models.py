from django.db import models
from django.urls import reverse
# Create your models here.
class Newpost(models.Model):

    name = models.CharField(max_length=200,unique=True)
    new_photo = models.ImageField(upload_to='posts/images', blank=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name
