from django.contrib import admin, messages
from uapp.models import *


class VendaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # atualiza o saldo da conta
        conta = Conta.objects.all().first()
        valor_venda = obj.produto.valor * obj.quantidade
        novo_saldo = conta.saldo + valor_venda
        conta.saldo = novo_saldo
        conta.save()
        # registra a movimentação
        movimentacao = Movimentacao(tipo='E',valor=valor_venda)
        movimentacao.save()
        super().save_model(request, obj, form, change)


class SaidaAdmin(admin.ModelAdmin):

    def save_model(self, request,obj,form,change):
        # atualiza o saldo da conta
        conta = Conta.objects.all().first()
        valor_saida = obj.valor
        # verificar saldo suficiente
        if valor_saida <= conta.saldo:
            # registra a operação normalmente
            novo_saldo = conta.saldo - valor_saida
            conta.saldo = novo_saldo
            conta.save()
            # registra a movimentação
            movimentacao = Movimentacao(tipo='S',valor=valor_saida)
            movimentacao.save()
            super().save_model(request, obj, form, change)
        else:
            # informa sobre o saldo insuficiente
            messages.add_message(request,
                                 messages.ERROR,'Saldo insuficiente')



# Registrando as classes no admin
admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Conta)
admin.site.register(Movimentacao)
admin.site.register(Saida, SaidaAdmin)