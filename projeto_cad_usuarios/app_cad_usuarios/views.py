from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


from django.http.response import HttpResponse


def home(request):
    return render(request,'usuarios/home.html')

def about(request):
    return render(request, 'Tela_about/about.html')





def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já existe')
            return redirect('cadastro')
        else:
            user = User(username=username, email=email, senha=senha)
            user.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('cadastro')
    else:
        return render(request, 'cadastro.html')


        
 
def entrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        if User.objects.filter(username=username).exists() and User.objects.filter(senha=senha).exists():
            return redirect('home')
        else:
            
            messages.error(request, 'Usuário ou senha incorretas')
            return redirect('entrar')
    else:
        return render(request, 'entrar.html')
















    


