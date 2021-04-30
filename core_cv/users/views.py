from django.shortcuts import render
from django.views.generic import View
from .models import Profile
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

User = settings.AUTH_USER_MODEL


class HomeUsers(View):
    def __init__(self):
        super().__init__()
        self.profile = None

    def get(self, *args, **kwarg):
        self.profile = Profile.objects.get(user_id=1)

        context = {
            "title": 'CV Page',
            "profile": self.profile,
        }

        return render(self.request, "home_users.html", context)

    def post(self, *args, **kwarg):
        pass


class Register(View):
    # user creation form (django build in)

    def __init__(self):
        super(Register, self).__init__()
        self.form = None

    def get(self, *args, **kwarg):
        form = UserCreationForm()

        context = {
            "title": 'Register',
            "form": self.form,
        }

        return render(self.request, "register_users.html", context)

    def post(self, *args, **kwarg):
        pass
