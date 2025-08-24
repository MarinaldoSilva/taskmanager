from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields =[
            'titulo',
            'descricao',
            'data_criacao',
            'conclusao',
            'dono'
        ]
        read_only_fields = ['dono', 'data_criacao']