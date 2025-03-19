from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.phone_number = phone_number
                user.save()
                login(request, user)
                return redirect('dashboard')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Passwords don't match")
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
