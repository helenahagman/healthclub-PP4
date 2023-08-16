from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'previous'), (1, 'Booked'))


class BookingSession(models.Model):
    name = models.CharField(max_length=80, default='Name', blank=False)
    email = models.EmailField(default='example@example.com', blank=False)
    age = models.CharField(max_length=2, default='18', blank=False)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)


# class RegistrationForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password']
#        widgets = {
#            'password': forms.PasswordInput(),
#        }
