from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("login", obtain_auth_token),
    path("signup", views.api_signup),
]