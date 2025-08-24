from django.db import models
from django.conf import settings

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    conclusao = models.BooleanField(default=False)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tarefas')
    
    def __str__(self):
        return self.titulo