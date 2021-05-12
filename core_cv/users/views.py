from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from .models import Profile, InTouch
from .forms import UserRegisterForm, UserProfileForm, ContactForm
from django.contrib import messages
from .utils import check_name, mail_send

"""
front page  
"""


class HomeUsers(View):
    def __init__(self):
        super().__init__()
        self.profile = None
        self.form = ContactForm()
        self.uname = None
        self.q = None

    def get(self, *args, **kwarg):

        """
        check_name will check the strange attempts validation
        """
        self.uname = check_name(self.kwargs.get('uname'), self.request)
        self.q = check_name(self.request.GET.get('q'), self.request)

        """
         transfer uname and q thru hte session
        """
        self.request.session['uname'] = self.uname
        self.request.session['q'] = self.q

        """
        search switch
        """
        if self.uname:
            self.profile = Profile.objects.get(user__username=self.uname)
        elif self.q:
            self.profile = Profile.objects.get(user__username=self.q)

            """ 
            main page will be the main user page (admin) 
            oll others will be www.domain/username 
            """
        else:
            if self.request.user.is_authenticated:
                self.profile = Profile.objects.get(user__username=self.request.user.username)
            else:
                self.profile = Profile.objects.get(user__username='admin')

        context = {
            "title": 'CV Page',
            "profile": self.profile,
            'form': self.form,

        }

        return render(self.request, "home_users.html", context)

    """
    # handling message sending at main page 
    # get data from user
    # save to db
    # send email to user and for self 
    all logic will be in utils file
    """

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
                # handle mailing for user nad for the person that asking
                mail_send(email, text, request)
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


"""
any user can update his profile 
allow only for user to update his profile 
user must be logged in to see this page at all 
"""


class ProfileUserUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    fields = (
        'show_name',
        'phone',
        'image',
        'intro',
        'experience',
        'education',
        'skills',
        'personal_quality',
        'languages',

    )
    model = Profile
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'profile'
        return context
