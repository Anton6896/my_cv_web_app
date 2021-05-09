# costume profile for ech user that was created
from django.db import models
from PIL import Image
import os
from uuid import uuid4
from django.conf import settings
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.urls import reverse

User = settings.AUTH_USER_MODEL


def customer_image_file_path(instance, filename):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'

    return os.path.join('upload/customer_pic/', filename)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_query_name='user_profile')
    image = models.ImageField(default='default.jpg',
                              upload_to=customer_image_file_path)

    # todo create data that will be taken from user for his portfolio

    # intro = models.TextField(null=True, blank=True)
    show_name = models.CharField(null=True, blank=True, max_length=50)
    phone = models.CharField(null=True, blank=True, max_length=50)

    intro = RichTextField(null=True, blank=True)
    experience = RichTextField(null=True, blank=True)
    education = RichTextField(null=True, blank=True)
    skills = RichTextField(null=True, blank=True)
    personal_quality = models.TextField(null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        try:
            img = Image.open(self.image.path)
            output_size = (300, 300)

            if img.height > 300 or img.width > 300:
                img.thumbnail(output_size)
                img.save(self.image.path)
        except IOError:
            print(f'where is the file for img working ?')

    def __str__(self):
        return f"profile of {self.user.username}"

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={"pk": self.pk})


# trigger create user profile on user creation
def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(user_created_receiver, sender=User)


class InTouch(models.Model):
    # email is optional but bootstrap will check it
    # its independent table
    email = models.CharField(null=True, blank=True, max_length=50)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)
