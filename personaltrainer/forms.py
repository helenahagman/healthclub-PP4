from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# pylint: disable=no-member
from .models import BookingSession, UserProfile, Booking, Service


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, required=True, help_text='Enter a valid email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control',
                                           'type': 'date'}),
            'time': forms.DateInput(attrs={'class': 'form-control',
                                           'type': 'time'}),
        }


service = forms.ModelChoiceField(queryset=Service.objects.all())
