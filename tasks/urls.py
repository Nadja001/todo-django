from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.listar_tarefas, name='listar'),
    path('<int:pk>/', views.detalhes_tarefa, name='detalhes'),
]
