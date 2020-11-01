from django.db import models


class AudioBK(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class AudioVk(models.Model):
    audioname = models.CharField(max_length=100)
    age = models.IntegerField()