from django.contrib import admin
from .models import Aluno, Curso, Disciplina


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "carga_horaria", "ativo", "criado_em")
    search_fields = ("nome", "descricao")
    list_filter = ("ativo",)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula", "email", "curso", "ativo")
    search_fields = ("nome", "matricula", "email")
    list_filter = ("ativo", "curso")


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nome", "curso", "carga_horaria", "ativa")
    search_fields = ("nome", "codigo")
    list_filter = ("ativa", "curso")
