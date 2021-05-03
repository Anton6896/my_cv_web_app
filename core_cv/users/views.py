from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from .models import Profile, InTouch
from .forms import UserRegisterForm, UserProfileForm, ContactForm
from django.contrib import messages


class HomeUsers(View):
    def __init__(self):
        super().__init__()
        self.profile = None
        self.form = ContactForm()

    def get(self, *args, **kwarg):
        self.profile = Profile.objects.get(user_id=1)

        context = {
            "title": 'CV Page',
            "profile": self.profile,
            'form': self.form,

        }

        return render(self.request, "home_users.html", context)

    def post(self, request, *args, **kwarg):
        self.form = ContactForm(request.POST)
        if self.form.is_valid():
            email = self.form.cleaned_data.get('email')
            text = self.form.cleaned_data.get('text')
            _, created = InTouch.objects.get_or_create(
                email=email,
                text=text
            )
            if created:
                messages.success(request, f'tanks {email}, will be in touch with you as soon as possible !')
                # todo send email that i received the data
            return redirect("users:home")


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
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            pass


class ProfileUserUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Profile
    fields = (
        'image',
        'intro',
        'experience',
        'education',
        'skills',
        'personal_quality',
        'languages',
    )
    template_name = 'profile_users.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request, f'Profile Updated for {self.request.user.username}')
        return super().form_valid(form)

    def test_func(self):
        # check if the user is author of this post
        pr = self.get_object()
        return self.request.user == pr.user
