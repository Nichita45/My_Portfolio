from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, blank=True, null=True)
    uploader = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title

