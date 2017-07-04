from django.contrib import admin
from .models import User
from .forms import UserAdminCreatForm, UserAdminForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreatForm
    add_fieldsets = (
        (None,{
            'fields': ('username', 'name', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets=(
        (None,{
            'fields':('username', 'email')
        }),
        ('Informações Básicas',{
            'fields':('name', 'last_login')
        }),
        ('Permissões',{
            'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined']

admin.site.register(User, UserAdmin)
