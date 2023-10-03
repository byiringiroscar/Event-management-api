from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

User = get_user_model()


# Create a custom admin class for User model
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'full_name', 'phone_number', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'full_name', 'phone_number')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'full_name', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'phone_number', 'password1', 'password2'),
        }),
    )


# Register your custom User admin class with the Django admin site
admin.site.register(User, UserAdmin)
