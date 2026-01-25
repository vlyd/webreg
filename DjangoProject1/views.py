from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import CustomUser
from .serializers import UsersSerializer

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # передаём данные из формы
        if form.is_valid():                   # Django сам всё проверяет
            form.save()                       # создаёт пользователя
            return redirect('login')          # перенаправляем на страницу входа
    else:
        form = UserCreationForm()             # создаём пустую форму для отображения на странице

    return render(request, 'register.html', {'form': form})

class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer