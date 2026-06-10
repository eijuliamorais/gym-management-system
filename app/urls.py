from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),                          
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  

    # Alunos 
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),

    # Planos
    path('planos/', views.listar_planos, name='listar_planos'),
    path('planos/novo/', views.criar_plano, name='criar_plano'),
    path('planos/editar/<int:id>/', views.editar_plano, name='editar_plano'),
    path('planos/excluir/<int:id>/', views.excluir_plano, name='excluir_plano'),

    # Pagamentos
    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('pagamentos/novo/', views.criar_pagamento, name='criar_pagamento'),
    path('pagamentos/editar/<int:id>/', views.editar_pagamento, name='editar_pagamento'),
    path('pagamentos/excluir/<int:id>/', views.excluir_pagamento, name='excluir_pagamento'),

    # Treinos
    path('treinos/', views.listar_treinos, name='listar_treinos'),
    path('treinos/novo/', views.criar_treino, name='criar_treino'),
    path('treinos/editar/<int:id>/', views.editar_treino, name='editar_treino'),
    path('treinos/excluir/<int:id>/', views.excluir_treino, name='excluir_treino'),
]