from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.


@login_required
def profile(request):
    profile = get_object_or_404(Profile, User=request.user)
    return render(request, 'base/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, User=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'base/edit_profile.html', {'form': form})


def index(request):
    return render(request, "base/index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in and redirect to index
            login(request, user)
            return redirect("index")

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'base/change_password.html', {'form': form})
