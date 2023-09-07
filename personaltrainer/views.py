from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import generic, View
from .forms import SignUpForm, BookingForm
from .models import Service


User = get_user_model()

# authenicate and log in the user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')


class PersonalTrainerView(generic.TemplateView):
    template_name = 'personaltrainer.html'


@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    services = Service.objects.all()
    return render(request, 'book.html', {'form': form, 'services': services})


def booking_success(request):
    return render(request, 'booking_success.html')
