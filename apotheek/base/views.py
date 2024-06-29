from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Profile, Collection, Medicine, User
from .forms import ProfileForm, CollectionForm, MedicineForm

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


@staff_member_required
def unapproved_takeaways(request):
    return render(request, "base/unapproved_takeaways.html")


@login_required
def afhaalacties(request):
    collections = Collection.objects.filter(User=request.user)
    return render(request, 'base/afhaalacties.html', {'collections': collections})


@login_required
def update_afhaalacties(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('collection_'):
                collection_id = key.split('_')[1]
                collection = Collection.objects.get(
                    id=collection_id, user=request.user)
                if value == 'true':
                    collection.collected = True
                    collection.save()
        return redirect('afhaalacties')
    else:
        collections = Collection.objects.filter(User=request.user)
        return render(request, 'base/afhaalacties.html', {'collections': collections})


@staff_member_required
def manage_collections(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_collections')
    else:
        form = CollectionForm()
    collections = Collection.objects.all()
    users = User.objects.all()
    medicines = Medicine.objects.all()
    return render(request, 'base/manage_collections.html', {
        'form': form,
        'collections': collections,
        'users': users,
        'medicines': medicines,
    })


@staff_member_required
def confirm_afhaalacties(request):
    if request.method == 'POST':
        # Iterate through all collection instances for approval
        for key, value in request.POST.items():
            if key.startswith('approve_'):
                collection_id = key.split('_')[1]
                collection = Collection.objects.get(id=collection_id)
                if value == 'true':
                    collection.collected_approved = True
                    collection.save()
        return redirect('confirm_afhaalacties')
    else:
        collections = Collection.objects.filter(
            Collected=True, CollectedApproved=False)
        return render(request, 'base/confirm_afhaalacties.html', {'collections': collections})


@login_required
def medicine(request):
    medicines = Medicine.objects.all()
    context = {"medicines": medicines}
    return render(request, 'base/medicine.html', context)


@staff_member_required
def new_medicine(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.save()
            messages.success(request, "Medicijn succesvol toegevoegd")
            return redirect("new_medicine")
        else:
            messages.error(
                request, "Er is een fout opgetreden. Probeer het opnieuw.")
    else:
        form = MedicineForm()

    context = {"form": form}
    return render(request, "base/new_medicine.html", context)
