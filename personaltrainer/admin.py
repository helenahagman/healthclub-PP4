from django.contrib import admin
from .models import BookingSession, UserProfile, CustomUser
from django_summernote.admin import SummernoteModelAdmin
from .forms import BookingSessionForm, RegistrationForm


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


admin.site.register(BookingSession, BookingSessionAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
