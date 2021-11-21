from django.db import models
from django.contrib.auth.models import User # importando models do django
from datetime import datetime

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # utilizando a propria tabela de usuários do django
    local = models.CharField(blank=True, null=True, max_length=60)

    class Meta: # Padrão utilizado para forçar a criação da tabela com o nome que vc deseja, evita criar "core_evento"
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self): # convertendo o formato de hora para string para ser exibido na edição do evento
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False