from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, InTouch


class UserRegisterForm(UserCreationForm):
    # extend an user creation form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.Form):
    class Meta:
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


class ContactForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))

    class Meta:
        model = InTouch
        fields = ('email', 'text')


