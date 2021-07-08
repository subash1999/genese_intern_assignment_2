from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank= True, null = True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank= True, null = True, on_delete=models.SET_NULL)
    slug = models.SlugField(null = True, blank= True)