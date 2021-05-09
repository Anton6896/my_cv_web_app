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
    personal_quality = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'quality_1 , quality_2 , etc.',
        'label': "this is the label"
    }))

    class Meta:
        model = Profile
        exclude = ('user', )


class ContactForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '3',
    }))

    class Meta:
        model = InTouch
        fields = ('email', 'text')
