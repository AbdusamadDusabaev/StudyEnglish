from django.views import View
from django.views.generic import CreateView

from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpRequest, HttpResponse
from django.forms import Form
from django.core.exceptions import ValidationError

from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render

from .models import Profile
from .forms import ProfileForm


class RegistrationView(CreateView):
    template_name = "authentication/registration.html"
    form_class = UserCreationForm

    def form_valid(self, form: Form) -> HttpResponse:
        user_cleaned_data = form.cleaned_data
        username = user_cleaned_data["username"]
        password = user_cleaned_data["password1"]
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)
        return redirect(reverse("authentication:profile-update"))


class ProfileUpdateView(LoginRequiredMixin, View):
    @staticmethod
    def get(request: HttpRequest, error_message_dict: ValidationError = None) -> HttpResponse:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(instance=profile)
        context = {
            "profile_form": profile_form,
            "error_message_dict": error_message_dict,
        }
        return render(request=request, template_name="authentication/profile-update.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        profile = self.get_profile_form_data(request=request)
        try:
            profile.clean_fields()
            profile.save()
            # return redirect(reverse("personal-area:main-page"))
            return redirect(reverse("authentication:profile-update"))
        except ValidationError as error:
            return self.get(request=request, error_message_dict=error.message_dict)

    @staticmethod
    def get_profile_form_data(request: HttpRequest) -> Profile:
        profile = Profile.objects.get(user=request.user)
        profile.email = request.POST["email"]
        profile.first_name = request.POST["first_name"]
        profile.second_name = request.POST["second_name"]
        if request.FILES.get("avatar", "") != "":
            profile.avatar = request.FILES["avatar"]
        return profile


class MyLoginView(LoginView):
    template_name = "authentication/login.html"


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("authentication:login")
