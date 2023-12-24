from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
import logging
import json
from django.contrib.auth.forms import UserCreationForm

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'djangoapp/index.html')

def about_us(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

def contact_us(request):
    return render(request, 'djangoapp/contact_us.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name}!")
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'djangoapp/login.html')

def logout_request(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('djangoapp:index')

def signup_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name}! Your account has been created.")
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Error creating your account. Please check the provided information.")
    else:
        form = UserCreationForm()

    return render(request, 'djangoapp/registration.html', {'form': form})


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
