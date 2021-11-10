from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

SCORE_CHOISES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),   
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]
RATING_CHOISES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class Review(models.Model):
    title = models.CharField(max_length=50)
    #group = models.TextField(choices="""""")
    #tags = models.TextField(choices="""""")
    #images = models.FileField()
    publisher = models.CharField(max_length=50)
    #publisher = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(max_length=6000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField(choices=SCORE_CHOISES)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOISES, blank=True, default=1)
    #likes = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return self.title
