from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    possui_validade = models.BooleanField()
    data_validade = models.DateField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    data_venda = models.DateTimeField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.produto.nome} (Quantidade: {self.quantidade})"

    class Meta:
        verbose_name='Venda'


class Conta(models.Model):
    saldo = models.FloatField()
    data_atualizacao = models.DateTimeField()
    instituicao = models.CharField(max_length=50)
    agencia = models.CharField(max_length=10)
    numero_conta = models.CharField(max_length=10)

    def __str__(self):
        return f"Saldo R$: {self.saldo} {self.instituicao}"


class Movimentacao(models.Model):
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1)
    valor = models.FloatField()

    def __str__(self):
        return f'{self.tipo} : {self.valor}'

    class Meta:
        verbose_name='Movimentaçõe'
