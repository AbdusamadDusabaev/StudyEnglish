from django.urls import path
from .views import RegistrationView, ProfileUpdateView, MyLoginView, MyLogoutView


app_name = "authentication"

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("profile-update/", ProfileUpdateView.as_view(), name="profile-update"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]