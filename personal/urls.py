from django.urls import path

from .views import (
    renderHomeView,
    renderRegisterView,
    renderLoginView,
    renderLogoutView,
    renderProfileView,
)


urlpatterns = [
    path('', renderHomeView, name='home'),
    path('register/', renderRegisterView, name='register'),
    path('login/', renderLoginView, name='login'),
    path('logout/', renderLogoutView, name='logout'),
    path('profile/', renderProfileView, name='profile'),
]