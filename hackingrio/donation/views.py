from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.



def signup(request):
    return render(request, 'donation/signup.html', )