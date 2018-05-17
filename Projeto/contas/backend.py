from django.core.exceptions import ObjectDoesNotExist
from contas.models import Usuario
def autenticar(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    try:
        usuario = Usuario.objects.get(email=email)
        if usuario.senha == senha:
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False

