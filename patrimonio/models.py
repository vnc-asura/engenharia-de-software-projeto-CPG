from django.db import models

# Create your models here.

class Patrimonio(models.Model):

    codigo = models.CharField(max_length=20, unique=True)  # Código de tombamento
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)  
    localizacao = models.ForeignKey('Localizacao', on_delete=models.SET_NULL, null=True)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.SET_NULL, null=True, blank=True)
    data_aquisicao = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('ativo', 'Ativo'), ('manutencao', 'Em Manutenção'), ('baixado', 'Baixado')],
        default='ativo'
    )

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
class Localizacao(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Ex: Bloco A, Sala 101
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    setor = models.CharField(max_length=100)  # Ex: TI, Administração

    def __str__(self):
        return f"{self.nome} ({self.setor})"

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class HistoricoMovimentacao(models.Model):

    patrimonio = models.ForeignKey('Patrimonio', on_delete=models.CASCADE)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    localizacao_anterior = models.ForeignKey('Localizacao', on_delete=models.SET_NULL, null=True, related_name='origem')
    localizacao_nova = models.ForeignKey('Localizacao', on_delete=models.SET_NULL, null=True, related_name='destino')
    responsavel_anterior = models.ForeignKey('Responsavel', on_delete=models.SET_NULL, null=True, related_name='responsavel_anterior')
    responsavel_novo = models.ForeignKey('Responsavel', on_delete=models.SET_NULL, null=True, related_name='responsavel_novo')

    def __str__(self):
        return f"Movimentação {self.patrimonio} em {self.data_movimentacao}"
    
