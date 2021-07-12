from assignment2.utils import unique_slug_generator
from django.db import models
from django.urls.base import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null = False, blank= False, unique=True)

    def get_absolute_url(self):
        return reverse('category:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # override the save method to generate slug
        # self.slug = unique_slug_generator(self, self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


# generate slug using the signal
@receiver(pre_save, sender=Category)
def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance,instance.name)