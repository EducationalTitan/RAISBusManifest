from django.shortcuts import render, redirect
from .forms import BusManifestForm, SignUpForm  # Import the necessary forms
from django.contrib import messages
from .models import BusManifest
from django.contrib.auth import login, authenticate
from django.urls import reverse


def manifest_form(request):
    if request.method == 'POST':
        form = BusManifestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manifest submitted successfully!')
            return redirect('manifest_list')  # Adjust as needed
    else:
        form = BusManifestForm()

    return render(request, 'manifest/manifest_form.html', {'form': form})

# Display a list of all bus manifests
def manifest_list(request):
    manifests = BusManifest.objects.all().order_by('-date')  # Get all manifests ordered by date
    return render(request, 'manifest/manifest_list.html', {'manifests': manifests})

# Handle user signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('home')  # Redirect to home page after successful signup
    else:
        form = SignUpForm()  # Show empty signup form for GET request

    return render(request, 'manifest/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # handle login logic
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manifest_form')

# Render the homepage view
def homepage_view(request):
    return render(request, 'manifest/home.html')

def home(request):
    return render(request, 'manifest/home.html')



