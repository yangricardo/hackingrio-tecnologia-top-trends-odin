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

def historic(request):
    doacoes = DonatedBeneficiary.objects.filter(doacao__doado_por=request.user)
    return render(request, 'historic.html', {'doacoes':doacoes})


def beneficiaries(request):
    doacoes = DonatedBeneficiary.objects.filter(doacao__doado_por=request.user)
    
    beneficiarios = list( set( d.beneficiario for d in doacoes ) )

    return render(request, 'beneficiary.html', {'beneficiarios':beneficiarios})



def donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.doado_por = request.user
            donation.save()

        beneficiarios = Beneficiary.objects.all()

        doacao_distribuida = donation.valor_doado / len(beneficiarios)
        
        for beneficiario in beneficiarios:
            DonatedBeneficiary.objects.create(doacao = donation,valor_doado_ao_beneficiario = doacao_distribuida,beneficiario = beneficiario,)





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
