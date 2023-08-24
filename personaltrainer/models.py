from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

User = get_user_model()


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username


class BookingSession(models.Model):
    name = models.CharField(max_length=80, default='Name', blank=False)
    email = models.EmailField(default='example@example.com', blank=False)
    age = models.CharField(max_length=2, default='18', blank=False)
    phone_number = models.CharField(max_length=15, default='', blank=False)
    date = models.DateField(default=timezone.now, help_text='Select date')
    time = models.TimeField(default=None)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True,
        blank=True
    )

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "Profile without user"
