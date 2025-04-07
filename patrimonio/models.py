from django.db import models

# Endereços
class Endereco(models.Model):
    end_logradouro = models.CharField(max_length=255)
    end_numero = models.IntegerField()
    end_complemento = models.CharField(max_length=255, blank=True, null=True)
    end_bairro = models.CharField(max_length=100)
    end_cidade = models.CharField(max_length=100)
    end_estado = models.CharField(max_length=100)
    end_pais = models.CharField(max_length=100)
    end_cep = models.CharField(max_length=10)
    end_uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.end_logradouro}, {self.end_numero} - {self.end_cidade}/{self.end_uf}"

# Pessoas
class Pessoa(models.Model):
    TIPO_CHOICES = [
        (1, 'Física'),
        (2, 'Jurídica'),
    ]
    pes_end = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    pes_tipo = models.IntegerField(choices=TIPO_CHOICES)
    pes_telefone = models.CharField(max_length=20)
    pes_email = models.EmailField()
    pes_data_cadastro = models.DateField()
    pes_pf = models.OneToOneField('PessoaFisica', on_delete=models.SET_NULL, null=True, blank=True)
    pes_pj = models.OneToOneField('PessoaJuridica', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.pes_email

# Pessoa Física
class PessoaFisica(models.Model):
    GENERO_CHOICES = [
        (1, 'Masculino'),
        (2, 'Feminino'),
        (3, 'Outro'),
    ]
    pf_nome = models.CharField(max_length=255)
    pf_nascimento = models.DateField()
    pf_cpf = models.CharField(max_length=14, unique=True)
    pf_genero = models.IntegerField(choices=GENERO_CHOICES)

    def __str__(self):
        return self.pf_nome

# Pessoa Jurídica
class PessoaJuridica(models.Model):
    pj_razao_social = models.CharField(max_length=255)
    pj_nome_fantasia = models.CharField(max_length=255)
    pj_cnpj = models.CharField(max_length=18, unique=True)
    pj_representante = models.CharField(max_length=255)
    pj_data_constituicao = models.DateField()

    def __str__(self):
        return self.pj_razao_social

# Patrimônio
class Patrimonio(models.Model):
    pat_codigo = models.CharField(max_length=20, unique=True)  # Código de tombamento
    pat_nome = models.CharField(max_length=100)
    pat_marca = models.CharField(max_length=100)
    pat_modelo = models.CharField(max_length=100)
    pat_nse = models.CharField(max_length=50, unique=True)
    pat_data_registrado = models.DateField()
    pat_data_aquisicao = models.DateField()
    pat_valor = models.FloatField()
    pat_descricao = models.TextField(blank=True, null=True)
    pat_categoria = models.CharField(max_length=100)
    pat_status = models.CharField(
        max_length=20,
        choices=[('ativo', 'Ativo'), ('manutencao', 'Em Manutenção'), ('baixado', 'Baixado')],
        default='ativo'
    )

    def __str__(self):
        return f"{self.pat_codigo} - {self.pat_nome}"

# Inventários
class Inventario(models.Model):
    inv_descricao = models.CharField(max_length=255)
    inv_data_criacao = models.DateField()

    def __str__(self):
        return self.inv_descricao

# Inventário-Patrimônio (Relacionamento N para N)
class InventarioPatrimonio(models.Model):
    STATUS_CHOICES = [
        (1, 'Em Estoque'),
        (2, 'Em Uso'),
        (3, 'Danificado'),
        (4, 'Descartado'),
    ]
    ip_pat = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)
    ip_inv = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    ip_status = models.IntegerField(choices=STATUS_CHOICES)
    ip_descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"Inventário {self.ip_inv} - Patrimônio {self.ip_pat}"

# Etiquetagem
class Etiquetagem(models.Model):
    eti_descricao = models.CharField(max_length=255)
    eti_data_criacao = models.DateField()

    def __str__(self):
        return self.eti_descricao

# Etiquetagem-Patrimônio
class EtiquetagemPatrimonio(models.Model):
    ep_eti = models.ForeignKey(Etiquetagem, on_delete=models.CASCADE)
    ep_pat = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Etiqueta {self.ep_eti} - Patrimônio {self.ep_pat}"

# Ambiente
class Ambiente(models.Model):
    amb_nome = models.CharField(max_length=100)
    amb_descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.amb_nome

# Ambiente-Patrimônio
class AmbientePatrimonio(models.Model):
    ap_amb = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    ap_pat = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)
    ap_data_entrada = models.DateField()
    ap_data_saida = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.ap_pat} no ambiente {self.ap_amb}"

# Pessoa-Ambiente (nova tabela associativa do DER)
class PessoaAmbiente(models.Model):
    pa_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pa_ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    pa_data_entrada = models.DateField()
    pa_data_saida = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.pa_pessoa} associado ao ambiente {self.pa_ambiente}"

# Empréstimo
class Emprestimo(models.Model):
    STATUS_CHOICES = [
        (1, 'Pendente'),
        (2, 'Efetivado'),
        (3, 'Devolvido'),
        (4, 'Cancelado'),
    ]
    emp_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    emp_criado = models.DateField()
    emp_efetivado = models.DateField()
    emp_prazo = models.IntegerField()
    emp_devolvido = models.DateField(blank=True, null=True)
    emp_status = models.IntegerField(choices=STATUS_CHOICES)
    emp_anotacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Empréstimo de {self.emp_pessoa} em {self.emp_criado}"

# Patrimônio-Emprestimo
class PatrimonioEmprestimo(models.Model):
    pe_emp = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    pe_pat = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pe_pat} emprestado em {self.pe_emp}"
