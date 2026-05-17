# Gym Management System

Sistema de gestão de academia desenvolvido com **Django** para o trabalho da disciplina GAC116 - Programação Web. Permite gerenciar alunos, planos, instrutores, modalidades, treinos e pagamentos, com um painel administrativo moderno e intuitivo.

---

## Funcionalidades

- **Modelagem completa** com 6 tabelas e relacionamentos (ForeignKey)
- **Painel administrativo customizado** com tema **Jazzmin** (interface moderna e responsiva)
- **Inlines no admin**: pagamentos e treinos aparecem diretamente na ficha do aluno
- **Automação de pagamento**: o valor do pagamento é preenchido automaticamente a partir do plano do aluno (campo opcional)
- **Filtros e buscas** em todas as listagens do admin
- **Estrutura pronta** para expansão (views, templates com Bootstrap, autenticação de usuários)

---

## Modelos

| Modelo       | Descrição                                                                 |
|--------------|---------------------------------------------------------------------------|
| **Aluno**    | Nome, e-mail, telefone, idade, status ativo/inativo, plano vinculado, treino vinculado, data de cadastro |
| **Plano**    | Nome, preço, duração em meses, descrição                                 |
| **Instrutor**| Nome, e-mail, telefone, especialidade                                    |
| **Modalidade**| Nome, descrição (ex: Musculação, Yoga)                                   |
| **Treino**   | Nome, descrição, instrutor (FK), modalidade (FK)                          |
| **Pagamento**| Aluno (FK), valor (preenchido automático), data, status (Pago/Pendente/Atrasado) |

### Relacionamentos principais
- Um `Aluno` pertence a um `Plano` (FK, pode ser nulo)
- Um `Aluno` pode ter um `Treino` associado (FK)
- Um `Treino` tem um `Instrutor` e uma `Modalidade`
- Um `Aluno` pode ter múltiplos `Pagamento` (um-para-muitos)

---

## Como executar o projeto

### Pré‑requisitos
- Python 3.10 ou superior
- Git
- (Opcional) Ambiente virtual

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/eijuliamorais/gym-management-system.git
   cd gym-management-system

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows

3. **Instale as dependências**
   ```bash
   pip install django django-jazzmin

4. **Aplique as migrações do banco de dados**
   ```bash
   python manage.py createsuperuser

6. **Colete os arquivos estáticos (para o tema Jazzmin)**
   ```bash
   python manage.py collectstatic

7. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver

8. **Acesse o sistema**
   ```bash
   Admin: http://127.0.0.1:8000/admin (use o superusuário criado)
   Página inicial padrão (será customizada futuramente)
