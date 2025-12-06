from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Custom User model
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Optional: add more fields as needed
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = ['username']  # Required when creating superuser

    def __str__(self):
        return self.email


# Optional: User profile for additional details
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"



