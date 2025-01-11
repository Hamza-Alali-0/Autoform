from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .form import Forminscription
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = Forminscription(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = Forminscription()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')


@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

    
def deconnexion(request):
    logout(request)
    return redirect('connexion')

def base(request):
    return render(request, 'base.html')

def formations(request):
    return render(request, 'formations.html')

def jeux(request):
    return render(request, 'jeux.html')


def formvideo(request):
    
    video_id = request.GET.get('video')
    
    return render(request, 'formvideo.html', {'video_id': video_id})


