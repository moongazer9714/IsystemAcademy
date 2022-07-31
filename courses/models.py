
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=150)
    month = models.IntegerField(default=3)
    day = models.IntegerField(default=3)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bog`lanish'
        verbose_name_plural = 'Bog`lanishlar'


@receiver(pre_save, sender=Course)
def article_pre_save(sender, instance, *args, **kwargs):

    instance.slug = slugify(instance.title)
