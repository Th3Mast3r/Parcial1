from django.contrib.auth.models import User #archivo creado
def project_context(request):  #se importa de django-contribuciones-autenticacion-modelos y de alli que importe los usuarios

    context = {
        'me': User.objects.first(), #muestra el primer objeto dentro del usuario
    }

    return context #retorna