from django.shortcuts import render
from core.models import Evento

# Create your views here.

# def index(request):
#         return redirect('/agenda/')

def lista_eventos(request):
        #evento = Evento.objects.get(id=1) - Retorna evento de um usuário específico
        evento = Evento.objects.all() # Retorna eventos de todos os usuários
        #usuario = request.user # Retorna eventos do usuário logado na sessão
        #evento = Evento.objects.filter(usuario=usuario)
        dados = {'eventos':evento}
        return render(request, 'agenda.html', dados)


