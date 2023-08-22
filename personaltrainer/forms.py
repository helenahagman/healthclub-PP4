from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BookingSession


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class BookingSessionForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("Past dates are not permitted.")
        return date
