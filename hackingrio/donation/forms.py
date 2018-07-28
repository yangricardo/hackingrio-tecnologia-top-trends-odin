from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import DonatedBeneficiary, Donation


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ['valor_doado']



class SignUpForm(UserCreationForm):
    nome = forms.CharField(max_length=30, required=False, help_text='Nome')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )