from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from personaltrainer.models import BookingSession, CustomUser


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
        model = CustomUser
        fields = ('username', 'name', 'email',
                  'phone_number', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
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
