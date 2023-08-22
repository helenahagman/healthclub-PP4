from django.contrib import admin
from .models import BookingSession, UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BookingSession)
class BookingSessionAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'phone_number', 'date', 'time')
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ('date', 'time')
    summernote_fields = ('content',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user',)
    search_fields = ('user__username', 'user__email', 'user__phone_number',)
