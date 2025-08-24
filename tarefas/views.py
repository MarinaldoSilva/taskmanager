from rest_framework import viewsets
from .serializers import TarefaSerializer 
from .models import Tarefa
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

class TarefaViewSet(viewsets.ModelViewSet):
    "sempre que for necessário serializar os dados, use esse padrão de serialização"
    "para traduzir para json"
    serializer_class = TarefaSerializer

    """verifica de acorodo com as regras de autenticação se o usuário tem um tokem.
    salva a resposta para que o IsAuthenticated possa fazer a proxima validação
    authentication_classes = [TokenAuthentication]
    Define que a autenticação para este ViewSet será via Token
    """
    
    """verifica qual a resposta de authentication_classes para saber se o usuário realmente está logado ou não"""
    permission_classes = [IsAuthenticated]
    """se estiver logado pode verificar as proprias postagens ou criar, somente se estiver autenticado
    define a regra de que apenas usuários autenticados podem acessar este endpoint"""

    """quando reescrevemos o metodo get_queryset ao inves de mostrar todos as tarefas
    mostra somente as que o dono tem o tokem que está vinculados na tarefa"""
    def get_queryset(self):
        """dono=self.request.user - quando o usuário passa pela autenticação e validação
        esse parametro do metodo filter pega o usuário que chamou, e verifica se o token criado é do usuário
        e com base nisso é comparada a tarefa com o usuário, para saber se esta vinculado a um user a tarefa especifica
        se não tiver não vai mostrar nada"""
        return Tarefa.objects.filter(dono=self.request.user)


    """ao reescrever o perform_create, estamos falando para o nosso cód, quando foi salvar uma nova tarefa
    vai ser adicionado um dono nessa tarefa, vinculando a identidade do usuário a tarefa, e devido ao tokem
    o sistema já sabe quem é o dono da tarefa"""
    def perform_create(self,serializer):

        """vai receber o dono da tarefa"""
        serializer.save(dono=self.request.user)


