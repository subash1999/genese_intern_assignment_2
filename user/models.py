from django.db import models
from django.contrib.auth.models import User
import copy
import uuid


# Create your models here.
class UserProfile(models.Model):
    dob =  models.DateField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='users/', default='../static/default_user.png', blank=True, null=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    
    __original_image = None

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.__original_image = copy.deepcopy(self.image)

    def delete(self,  *args, **kwargs):
        self.__original_image.delete(save=False)
        super(UserProfile,self).delete(*args, **kwargs)

    def save(self,  *args, **kwargs):
        if not (self.image == self.__original_image):
            self.__original_image.delete(save=False)
            self.image.name = str(uuid.uuid4())+self.image.name
        super(UserProfile,self).save(*args, **kwargs)