from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class BookingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(default='example@example.com', blank=False)
    age = models.CharField(max_length=2, default='18', blank=False)
    phone_number = models.CharField(max_length=15, default='', blank=False)
    date = models.DateField(default=timezone.now, help_text='Select date')
    time = models.TimeField(default=None)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = (
                slugify(self.user.username)
                if self.user and hasattr(self.user, 'username')
                else 'no-username'
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            self.user.username
            if self.user and hasattr(self.user, 'username')
            else "No User"
        )


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return (
            self.user.username
            if self.user and hasattr(self.user, 'username')
            else "Profile without user"


class Booking(models.Model):
    user=models.ForeignKey(BookingSession, on_delete=models.CASCADE)
    service=models.ForeignKey(
        'personaltrainer.Service', on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=20, default='pending')

    def __str__(self):
        user_username=(
            self.user.user.username
            if self.user and hasattr(self.user, 'user')
            and hasattr(self.user.user, 'username')
            else 'No User'
        )
        return (
            f"{user_username} - {self.service.name} - "
            f"{self.date} {self.time}"
        )


class ServiceManager(models.Manager):
        pass


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
