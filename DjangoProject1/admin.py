from django.contrib import admin
from .models import CustomUser  # Импортируем нашу модель пользователей

@admin.register(CustomUser)  # Регистрируем модель в админке
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'score', 'level', 'is_active')  # Какие поля показывать в списке
    search_fields = ('username',)  # Добавляем поиск по имени пользователя
    list_filter = ('is_active', 'level')  # Фильтры по активности и уровню