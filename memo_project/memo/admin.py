from django.contrib import admin
from .models import Memo, Like

# Register your models here.
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'memo', 'created_at')