import pandas as pd
import random
from faker import Faker
import numpy as np
from datetime import datetime

fake = Faker('pt_BR')
anos_desejados = [2021, 2022, 2023, 2024, 2025]

colunas = [
    "Status", "Sub-issues progress", "Interveniência com o IA-UPE", "Convênio ou acordo",
    "Edital", "Acordo/convênio n.º", "Aditivo n.º", "Tipo de aditivo", "Empresa", "CNPJ",
    "Coordenador", "E-mail", "Telefone", "Início", "Término", "SEI", "Valor pactuado",
    "Valor repassado", "Valor executado", "Valor contrapartida", "Valor agência",
    "Valor unidade", "Valor IA-UPE", "Data publicação", "Publicação",
    "Link de acesso ao PTA", "Segmento"
]

def gerar_linha(ano_publicacao):
    data_pub = fake.date_between_dates(
        date_start=datetime(ano_publicacao, 1, 1),
        date_end=datetime(ano_publicacao, 12, 31)
    )
    return [
        random.choice(["Aberto", "Em andamento", "Concluído"]),
        f"{random.randint(0,100)}%",
        random.choice(["Sim", "Não"]),
        random.choice(["Convênio", "Acordo"]),
        f"Edital {random.randint(100,999)}/20{random.randint(20,24)}",
        f"{random.randint(1000,9999)}/{random.randint(2018,2025)}",
        f"{random.randint(1,5)}",
        random.choice(["Prorrogação", "Reajuste", "Outros"]),
        fake.company(),
        fake.cnpj(),
        fake.name(),
        fake.email(),
        fake.phone_number(),
        fake.date_between(start_date=datetime(ano_publicacao-2,1,1), end_date=datetime(ano_publicacao-1,12,31)),
        fake.date_between(start_date=datetime(ano_publicacao,1,1), end_date=datetime(ano_publicacao,12,31)),
        f"{random.randint(1000000,9999999)}-{random.randint(0,9)}",
        round(random.uniform(10000, 500000), 2),
        round(random.uniform(5000, 400000), 2),
        round(random.uniform(5000, 450000), 2),
        round(random.uniform(1000, 30000), 2),
        round(random.uniform(1000, 20000), 2),
        round(random.uniform(500, 15000), 2),
        round(random.uniform(1000, 50000), 2),
        str(data_pub),
        fake.text(max_nb_chars=30),
        fake.url(),
        random.choice(["Educação", "Saúde", "Segurança", "Tecnologia", "Meio Ambiente"])
    ]

dados = []
for ano in anos_desejados:
    for _ in range(20):
        dados.append(gerar_linha(ano))

df = pd.DataFrame(dados, columns=colunas)

df.to_json("dados_projetos_tecnologicos.json", orient="records", force_ascii=False, indent=4)
