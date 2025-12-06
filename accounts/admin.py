from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

# ====================================
# Custom User Admin
# ====================================
class CustomUserAdmin(UserAdmin):
    # Use our custom forms
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Fields to display in the admin list view
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('is_staff', 'is_active', 'is_verified')

    # Fields for creating a new user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('phone_number', 'date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'date_of_birth', 'profile_picture', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


# ====================================
# Profile Admin
# ====================================
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country')
    search_fields = ('user__username', 'user__email', 'city', 'country')


# ====================================
# Register models with admin
# ====================================
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)


