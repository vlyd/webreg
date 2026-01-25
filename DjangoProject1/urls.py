from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from DjangoProject1.views import UsersViewSet
from django.contrib.auth import views as auth_views
from .views import registration

#router = routers.DefaultRouter()
#router.register('players', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Страница входа
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Страница выхода
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', registration, name='register'),
    #path('api/', include(router.urls)),

]