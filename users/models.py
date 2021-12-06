from django.db import models
from cloudinary.models import CloudinaryField, CloudinaryImage
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('media')
    default_image = CloudinaryImage('default.png')
    def __str__(self):
        return f'{self.user.username} Profile'