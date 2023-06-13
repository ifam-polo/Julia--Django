from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('quantidade em estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome =  models.CharField('sobrenome', max_length=100)
    email = models.EmailField('e-mail', max_length=100)
