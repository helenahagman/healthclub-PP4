from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponse
from .forms import SignUpForm


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
