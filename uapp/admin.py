from django.contrib import admin
from uapp.models import Produto, Venda, Conta, Movimentacao


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



# Register your models here.
admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Conta)
admin.site.register(Movimentacao)