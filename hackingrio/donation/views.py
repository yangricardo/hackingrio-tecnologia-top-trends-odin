from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import DonationForm
from .models import Beneficiary, Donation, DonatedBeneficiary

def home(request):

    return render(request, 'home.html', )

def donation(request):
    user = User.objects.first() 
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donated_by = user
            donation.save()

            # return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = DonationForm()
    return render(request, 'donation.html',  {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
