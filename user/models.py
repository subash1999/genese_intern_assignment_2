from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    dob = models.DateField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='users', default='../static/default_user.png')
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
