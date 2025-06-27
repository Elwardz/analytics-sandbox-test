import pandas as pd
import random
from faker import Faker
from datetime import datetime

# Inicializa o gerador de dados
fake = Faker('pt_BR')

# Lista dos anos desejados
anos_desejados = [2021, 2022, 2023, 2024, 2025]

# Lista dos meses
meses = [
    ("Janeiro", 1), ("Fevereiro", 2), ("Março", 3),
    ("Abril", 4), ("Maio", 5), ("Junho", 6),
    ("Julho", 7), ("Agosto", 8), ("Setembro", 9),
    ("Outubro", 10), ("Novembro", 11), ("Dezembro", 12)
]

# Nomes das colunas
colunas = [
    "Projeto", "Ano", "Mês", "Número do mês", "Trimestre",
    "Status", "Valor da folha", "Recurso", "SEI mãe", "SEI",
    "Data limite para empenho", "Data limite para liquidação", "Data limite de PD",
    "Empenhada em", "Liquidada em", "OB emitida em", "Dias em atraso", "Sub-issues progress"
]

# Função para gerar uma linha
def gerar_linha(ano, mes_nome, mes_num):
    data_base = datetime(ano, mes_num, random.randint(1, 28))
    return [
        "PROPEGI Financeiro",
        ano,
        mes_nome,
        mes_num,
        f"Q{((mes_num - 1) // 3) + 1}",
        random.choice(["Aberto", "Em andamento", "Concluído"]),
        round(random.uniform(10000, 100000), 2),
        random.choice(["Fundo Estadual", "Tesouro", "Transferência Voluntária"]),
        f"{random.randint(1000000,9999999)}-{random.randint(0,9)}",
        f"{random.randint(1000000,9999999)}-{random.randint(0,9)}",
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        fake.date_between_dates(date_start=data_base, date_end=data_base).strftime('%Y-%m-%d'),
        random.randint(0, 60),
        round(random.uniform(0, 1), 2)  # valor entre 0.0 e 1.0
    ]

# Gerar dados: 12 meses por ano × 5 anos = 60 registros
dados = []
for ano in anos_desejados:
    for mes_nome, mes_num in meses:
        dados.append(gerar_linha(ano, mes_nome, mes_num))

# Criar DataFrame
df = pd.DataFrame(dados, columns=colunas)

# Exportar como JSON
df.to_json("propegi_financeiro_trimestres.json", orient="records", force_ascii=False, indent=4)

# Exportar como CSV
df.to_csv("propegi_financeiro_trimestres.csv", index=False)
