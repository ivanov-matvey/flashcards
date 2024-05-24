from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title[0:32]


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.front[0:32]
