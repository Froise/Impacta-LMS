from django.shortcuts import render, redirect
from contas.models import Usuario

def listaUsuarios(request):
    context = {
        'usuarios':Usuario.objects.all()
    }
    return render(request, 'listaUsuario.html', context)

def novoUsuario(request):
    context={}
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        if senha == senha2:
            Usuario.objects.create(
                email=email,
                senha=senha
            )
            return redirect('/contas/')
        else:
            context['erro'] = ' As senhas não conferem!'

    return render(request, 'formUsuario.html' ,context)
