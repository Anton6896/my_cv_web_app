from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}')
            return redirect("users:home")
    else:
        form = UserRegisterForm()

    return render(request, 'register_users.html', {
        "title": "register2",
        'form': form
    })


# todo edit profile data for cv
# https://www.youtube.com/watch?v=mF5jzSXb1dc
# you need the beautifully implementation on the page view
def profile():
    pass
