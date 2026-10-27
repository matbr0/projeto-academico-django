from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    carga_horaria = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="alunos")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} - {self.matricula}"


class Disciplina(models.Model):
    nome = models.CharField(max_length=120)
    codigo = models.CharField(max_length=20, unique=True)
    carga_horaria = models.PositiveIntegerField(default=0)
    ativa = models.BooleanField(default=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="disciplinas")

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
