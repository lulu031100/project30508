from django.db import models
from django import forms
# from .models import Image

# Create your models here.
class Image(models.Model):
    picture = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['picture', 'title']