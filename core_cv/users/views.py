from django.shortcuts import render
from django.views.generic import View
from .models import Profile
from django.conf import settings

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
