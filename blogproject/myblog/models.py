from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.urls import reverse


class UserRegistration(AbstractUser):
    user_image = models.ImageField(upload_to="uploads/", blank=True, null=True)


class Posts(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    post = models.CharField(max_length=255)
    title = models.CharField(max_length=200, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    likes = models.ManyToManyField(UserRegistration, blank=True, null=True, related_name='post_likes')


class Staff(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)

    def __str__(self):
        return self.name
