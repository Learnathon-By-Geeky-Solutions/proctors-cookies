from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log out any previously logged-in sessions for this user
            Session.objects.filter(user=user).delete()
            
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("profile") # Redirect to the profile page after successful login
        else:
            messages.error(request, "Invalid username or password.")
    
    context = {'title': 'Login'}
    return render(request, 'registration/login.html', context)




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')


def demo_view(request):
    return render(request, 'demo.html')



@login_required
def profile_view(request):
    """
    View to display the profile of the currently logged-in user.
    """
    user = get_object_or_404(User, username=request.user.username)  # Filter by the logged-in user's username
    return render(request, 'user_profile.html', {'user_profile': user})