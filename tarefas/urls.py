from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet

"""livro de registros em branco"""
router = DefaultRouter()

"""add new line in the book(gastando meu inglês hahahaha)"""
router.register(r'tarefas', TarefaViewSet, basename='tarefas')

"""minha lista de urls agora tem o endereço com as rotas adicionadas"""
urlpatterns = router.urls