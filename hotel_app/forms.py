from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Booking, User, Feedback


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'}))
    check_out = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Booking
        fields = ('check_in', 'check_out')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'email')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('content',)


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')
