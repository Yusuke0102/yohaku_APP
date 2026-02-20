from django.contrib import admin
from .models import AuthUser
# Register your models here.r

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'birth_date')  