from django.contrib import admin
from .models import Aluno, Plano, Modalidade, Treino, Pagamento, Instrutor

admin.site.register(Aluno)
admin.site.register(Plano)
admin.site.register(Modalidade)
admin.site.register(Treino)
admin.site.register(Pagamento)
admin.site.register(Instrutor)