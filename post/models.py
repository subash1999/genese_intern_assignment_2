from assignment2.utils import unique_slug_generator
from category.models import Category
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.urls.base import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )
    slug = models.SlugField(null=False, blank=False, unique=True)

    def get_absolute_url(self):
        return reverse("category:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # override the save method to generate slug
        # self.slug = unique_slug_generator(self, self.title)
        super(Post, self).save(*args, **kwargs)


# generate slug using the signal
@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance, instance.title)
