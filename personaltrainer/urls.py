from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('book/', views.book_service, name='book_service'),
    path('booking-success/', views.booking_success, name='booking_success'),
]
