from enum import unique
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Video(models.Model):
    video = models.FileField(upload_to='videos_uploaded',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    thumbnail = models.FileField(upload_to='thumbnails-uploads', null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='videos')

    def __str__(self):
        return self.title
    
