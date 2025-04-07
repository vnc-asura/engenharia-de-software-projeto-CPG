from django.contrib import admin
from patrimonio.models import (
    Endereco,
    Pessoa,
    PessoaFisica,
    PessoaJuridica,
    Patrimonio,
    Inventario,
    InventarioPatrimonio,
    Etiquetagem,
    EtiquetagemPatrimonio,
    Ambiente,
    AmbientePatrimonio,
    PessoaAmbiente,
    Emprestimo,
    PatrimonioEmprestimo,
)

# Registrando os modelos no Django Admin
admin.site.register(Endereco)
admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Patrimonio)
admin.site.register(Inventario)
admin.site.register(InventarioPatrimonio)
admin.site.register(Etiquetagem)
admin.site.register(EtiquetagemPatrimonio)
admin.site.register(Ambiente)
admin.site.register(AmbientePatrimonio)
admin.site.register(PessoaAmbiente)
admin.site.register(Emprestimo)
admin.site.register(PatrimonioEmprestimo)