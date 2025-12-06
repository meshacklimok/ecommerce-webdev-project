from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    AuthenticationForm, 
    PasswordChangeForm, 
    PasswordResetForm, 
    SetPasswordForm
)
from .models import CustomUser, Profile

# ======================================
# User Registration Form
# ======================================
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        help_text="Required. Enter a valid email address.",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    phone_number = forms.CharField(
        label="Phone Number",
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'})
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        help_text="Enter a strong password."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        help_text="Enter the same password as above for verification."
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'date_of_birth', 'profile_picture', 'password1', 'password2')


# ======================================
# User Update Form
# ======================================
class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label="Phone Number",
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'date_of_birth', 'profile_picture')


# ======================================
# Profile Update Form
# ======================================
class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        label="Bio",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell something about yourself...'})
    )
    address = forms.CharField(
        label="Address",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'})
    )
    city = forms.CharField(
        label="City",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
    )
    country = forms.CharField(
        label="Country",
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your country'})
    )

    class Meta:
        model = Profile
        fields = ('bio', 'address', 'city', 'country')


# ======================================
# Login Form (Email-based)
# ======================================
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )


# ======================================
# Password Change Form
# ======================================
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'})
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )


# ======================================
# Password Reset Form
# ======================================
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )


# ======================================
# Set New Password Form
# ======================================
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )


