from django.urls import path

from .views import (
    renderHomeView,
    renderRegisterView,
    renderLoginView,
    renderLogoutView,
)


urlpatterns = [
    path('', renderHomeView, name='home'),
    path('register/', renderRegisterView, name='register'),
    path('login/', renderLoginView, name='login'),
    path('logout/', renderLogoutView, name='logout'),
]