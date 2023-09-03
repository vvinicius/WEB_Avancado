from django.db import models


class Aluno(models.Model):
    nome = models.CharField('Nome',
    max_length=50)
    sobrenome = models.CharField('Sobrenome',
    max_length=100)
    periodo_ingresso = models.CharField('Período de Ingresso',max_length=50)
    nota = models.DecimalField('Nota - Web Avançado', decimal_places=2,
    max_digits=4)
    situacao = models.CharField('Situacao', max_length=50)
    email = models.EmailField('E-mail', max_length=100)




    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

