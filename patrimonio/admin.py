from django.contrib import admin

# Register your models here.

from patrimonio.models import (Patrimonio, Localizacao, Responsavel, Categoria, HistoricoMovimentacao)

class PatrimonioAdmin(admin.ModelAdmin):
    patrimonio = [
        'codigo','nome','descricao','categoria','localizacao','responsavel','data_aquisicao','status'
    ]

    list_display = patrimonio

    search_fields = patrimonio

admin.site.register(Patrimonio, PatrimonioAdmin)