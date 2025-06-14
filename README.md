# 📊 UPE Analytics Sandbox

Este repositório contém **datasets simulados** com o objetivo de apoiar a criação de dashboards, visualizações e análises exploratórias de dados em projetos da Universidade de Pernambuco (UPE).

Os dados foram gerados com base em dois cenários institucionais importantes:

- **Serviços Tecnológicos Prestados pela UPE**
- **Folha de Pagamento Trimestral da UPE**

Nenhum dado real foi utilizado — todos os registros são sintéticos e servem exclusivamente para fins educacionais, acadêmicos e de prototipagem analítica.

---

## 📁 Estrutura dos Arquivos

```
📦 upe-analytics-sandbox
├── servicos_tecnologicos_upe.json
└── folha_pagamento_trimestral_upe.json
```

- `servicos_tecnologicos_upe.json`  
  Dataset com 1000 registros simulando serviços tecnológicos realizados por institutos da UPE, com informações como tipo de serviço, valor contratado, tecnologia usada, impacto social e mais.

- `folha_pagamento_trimestral_upe.json`  
  Dataset com 1000 registros representando folhas de pagamento trimestrais da UPE, incluindo dados financeiros detalhados como salário base, encargos, descontos, valor líquido e tipo de vínculo do servidor.

---

## 📊 Possibilidades de Análise

Você pode utilizar os dados para responder perguntas como:

### Serviços Tecnológicos
- Quais institutos prestaram mais serviços tecnológicos?
- Qual foi o valor total contratado por campus?
- Quais tecnologias foram mais utilizadas?
- Qual o impacto social médio por tipo de serviço?

### Folha de Pagamento
- Qual o custo total da folha em cada trimestre?
- Qual o valor médio líquido recebido por tipo de vínculo?
- Como se distribuem os custos por cargo ou instituto?
- Qual o peso dos encargos no custo total para a UPE?

---

## 🚀 Como Usar

Você pode importar os arquivos `.json` diretamente em ferramentas como:

- Python (pandas, plotly, seaborn)
- Power BI (usando conector JSON)
- Excel (com Power Query)
- Tableau
- SQL (convertendo para .csv)

### Exemplo em Python

```python
import pandas as pd

df_servicos = pd.read_json("servicos_tecnologicos_upe.json")
df_folha = pd.read_json("folha_pagamento_trimestral_upe.json")

print(df_folha.head())
```

---

## 🔐 Aviso Legal

> Estes dados são **totalmente fictícios** e foram gerados para fins de aprendizado e simulação de análises. Nenhum vínculo real com pessoas, servidores ou instituições foi mantido.

---

## ✨ Autor

Desenvolvido por **Gabriel Lopes de Albuquerque**  
📚 Software Engineer Student (UPE) & Data Analysis | Python | MySQL | Power BI  
🔗 [LinkedIn](https://www.linkedin.com/in/gabriel-lopes-de-albuquerque-658a8317b/)

---

## 💡 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
