from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.listar_tarefas, name='listar'),
    path('<int:pk>/', views.detalhes_tarefa, name='detalhes'),
    path('criar/', views.criar_tarefa, name='criar'),
    path('editar/<int:pk>/', views.editar_tarefa, name='editar'),
    path('excluir/<int:pk>/', views.excluir_tarefa, name='excluir'),
]
