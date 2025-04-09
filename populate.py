import os
import django
from faker import Faker
import random

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')
django.setup()

from patrimonio.models import Endereco, Pessoa, PessoaFisica, PessoaJuridica, Patrimonio, Inventario, Etiquetagem, Ambiente, Emprestimo, InventarioPatrimonio

fake = Faker()

def populate(n=10):
    for _ in range(n):
        # Criar Endereço
        endereco = Endereco.objects.create(
            end_logradouro=fake.street_name(),
            end_numero=fake.random_int(min=1, max=9999),
            end_complemento=fake.secondary_address(),
            end_bairro=fake.city_suffix(),
            end_cidade=fake.city(),
            end_estado=fake.state(),
            end_pais=fake.country(),
            end_cep=fake.postcode(),
            end_uf=fake.state_abbr()
        )

        # Criar Pessoa Física
        pessoa_fisica = PessoaFisica.objects.create(
            pf_nome=fake.name(),
            pf_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=80),
            pf_cpf=fake.ssn(),
            pf_genero=random.choice([1, 2, 3])  # Masculino, Feminino, Outro
        )

        # Criar Pessoa Jurídica
        pessoa_juridica = PessoaJuridica.objects.create(
            pj_razao_social=fake.company(),
            pj_nome_fantasia=fake.company_suffix(),
            pj_cnpj=fake.ssn(),
            pj_representante=fake.name(),
            pj_data_constituicao=fake.date_this_century()
        )

        # Criar Pessoa
        pessoa = Pessoa.objects.create(
            pes_end=endereco,
            pes_tipo=random.choice([1, 2]),  # Física ou Jurídica
            pes_telefone=fake.phone_number(),
            pes_email=fake.email(),
            pes_data_cadastro=fake.date_this_year(),
            pes_pf=pessoa_fisica if random.choice([True, False]) else None,
            pes_pj=pessoa_juridica if random.choice([True, False]) else None
        )

        # Criar Patrimônio
        patrimonio = Patrimonio.objects.create(
            pat_codigo=f"PAT{fake.random_int(min=1000, max=9999)}",
            pat_nome=fake.word(),
            pat_marca=fake.company(),
            pat_modelo=fake.word(),
            pat_nse=f"NSE{fake.random_int(min=1000, max=9999)}",
            pat_data_registrado=fake.date_this_year(),
            pat_data_aquisicao=fake.date_this_year(),
            pat_valor=fake.random_number(digits=5, fix_len=True),
            pat_descricao=fake.text(max_nb_chars=200),
            pat_categoria=fake.word(),
            pat_status=random.choice(['ativo', 'manutencao', 'baixado'])
        )

        # Criar Inventário
        inventario = Inventario.objects.create(
            inv_descricao=f"Inventário {fake.word()}",
            inv_data_criacao=fake.date_this_year()
        )

        # Criar Etiquetagem
        etiquetagem = Etiquetagem.objects.create(
            eti_descricao=f"Etiqueta {fake.word()}",
            eti_data_criacao=fake.date_this_year()
        )

        # Criar Ambiente
        ambiente = Ambiente.objects.create(
            amb_nome=fake.word(),
            amb_descricao=fake.text(max_nb_chars=100)
        )

        # Criar Empréstimo
        emprestimo = Emprestimo.objects.create(
            emp_pessoa=pessoa,
            emp_criado=fake.date_this_year(),
            emp_efetivado=fake.date_this_year(),
            emp_prazo=fake.random_int(min=1, max=365),
            emp_status=random.choice([1, 2, 3, 4]),  # Pendente, Efetivado, Devolvido, Cancelado
            emp_anotacao=fake.text(max_nb_chars=200)
        )

        # Criar Inventário-Patrimônio
        InventarioPatrimonio.objects.create(
            ip_pat=patrimonio,
            ip_inv=inventario,
            ip_status=random.choice([1, 2, 3, 4]),  # Em Estoque, Em Uso, Danificado, Descartado
            ip_descricao=fake.text(max_nb_chars=100)
        )

    print(f"{n} registros fictícios criados com sucesso!")

if __name__ == "__main__":
    populate(20)