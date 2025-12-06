from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserChangeForm,
    ProfileUpdateForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm
)
from .models import Profile

# =====================================
# User Registration View
# =====================================
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your account has been created successfully.")
            return redirect('dashboard')  # Redirect to your dashboard
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# =====================================
# User Login View
# =====================================
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')  # Redirect to your dashboard
        messages.error(request, "Invalid email or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# =====================================
# User Logout View
# =====================================
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


# =====================================
# User Profile View
# =====================================
@login_required
def profile_view(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = CustomUserChangeForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile.html', context)


# =====================================
# Password Change View
# =====================================
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been updated successfully.")
            return redirect('profile')  # Redirect after password change
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


# =====================================
# Password Reset Request View
# =====================================
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


# =====================================
# Password Reset Confirm View (Set New Password)
# =====================================
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')













