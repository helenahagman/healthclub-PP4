from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django_summernote.admin import SummernoteModelAdmin
from .forms import BookingSessionForm, RegistrationForm
from personaltrainer.models import CustomUser, BookingSession


User = get_user_model()


@admin.register(BookingSession)
class BookingSessionAdmin(SummernoteModelAdmin):
    form = BookingSessionForm

    list_display = ('name', 'email', 'phone_number', 'date', 'time')
    search_fields = ['name', 'email', 'phone_number', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('date', 'time')
    summernote_fields = ('content',)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone_number')
    search_fields = ['name', 'username', 'email', 'phone_number']


@admin.register(CustomUser)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email', 'user__phone_number',)
    form = RegistrationForm

    def get_username(self, obj):
        return obj.user.username if obj.user else ""

    def get_email(self, obj):
        return obj.user.email if obj.user else ""

    def get_phone_number(self, obj):
        return obj.user.phone_number if obj.user else ""

    get_email.short_description = 'Email'
    get_username.short_description = 'Username'
    get_phone_number.short_description = 'Phone Number'
