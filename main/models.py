from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse

RATING_CHOISES = [
    (1, '1'), (2, '2'), (3, '3'), 
    (4, '4'), (5, '5'),
]

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homepage')

class Review(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='Movies')
    #tags = models.TextField(choices="""""")
    #images = models.FileField()
    publisher = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(max_length=6000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOISES, blank=True, default=0)
    #likes = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})