from django.contrib import admin
from .models import Reservation,MenuItems,User


from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
admin.site.register(Reservation)
admin.site.register(MenuItems)
admin.site.register(User)