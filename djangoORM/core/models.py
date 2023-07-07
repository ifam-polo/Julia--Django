from django.db import models
from django.contrib.auth import get_user_model

"""Relacionamento um para um: Um carro so se relaciona com um chassi
e um chassi so se relaciona com um"""

"""Relacionamento um para muitos: usa-se a fk no atributo(um). Ex um carro pode
ter apenas uma montadora, mas uma montadora pode montar varios carros"""


"""Relacionamento muitos para muitos """

"""Na classe carro(entidade fraca) percebe-se nos atributos das classes montadora e chassi(entidade forte)
CASCADE que significa que se o chassi for apagado o carro tambem será, porque
carro depende de chassi para existir"""
class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16)

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero
        

class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome
    

class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=30)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    motorista = models.ManyToManyField(get_user_model())
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}' 
 
        
"""O OneToOneField funciona como uma fk, ou seja, vc consegue
acessar as informações de ambos através de ambas as classes independente
delas terem o atributo ou não"""