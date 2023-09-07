from django.contrib import admin
from django.contrib.auth import get_user_model
from django_summernote.admin import SummernoteModelAdmin
from .models import BookingSession, UserProfile, Booking, Service
from .forms import BookingForm


User = get_user_model()


@admin.register(BookingSession)
class BookingSessionAdmin(SummernoteModelAdmin):
    form = BookingForm

    list_display = ('user_name', 'email', 'user_phone_number', 'date', 'time')
    search_fields = ['user__username', 'email',
                     'user__profile__phone_number', 'slug']
    prepopulated_fields = {'slug': ('email',)}
    list_filter = ('date', 'time')
    summernote_fields = ('content',)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = obj.user.username
        super().save_model(request, obj, form, change)

    def user_name(self, obj):
        return obj.user.profile.name if obj.user and obj.user.profile else ""
    user_name.short_description = 'Name'

    def user_phone_number(self, obj):
        return (obj.user.profile.phone_number if obj.user and obj.user.profile
                else "")
    user_phone_number.short_description = 'Phone Number'

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not change:
            obj.user = request.user
        return obj


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'phone_number')
    search_fields = ['name', 'username', 'email', 'phone_number']


admin.site.register(Service)
