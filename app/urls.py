from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]