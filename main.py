import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# | Importando os dados da API |
from API import data

# | Funções para análise de dados |
def criar_grafico(dados, tipo='bar', titulo='', xlabel='', ylabel='', figsize=(10, 6)):
    fig, ax = plt.subplots(figsize=figsize)  # controle de tamanho

    if tipo == 'pie':
        dados.plot(kind=tipo, autopct='%1.1f%%', ax=ax)
        ax.set_ylabel('')  # pie chart não precisa de ylabel
    else:
        dados.plot(kind=tipo, ax=ax)

    ax.set_title(titulo, fontsize=14, pad=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.tight_layout()  # evita legendas e labels cortadas
    plt.show()

# | Leitura do arquivo json da API e criação do DataFrame |
df = pd.DataFrame(data['products'])

# Verificando se há valores nulos
print(df.isnull().sum())

# | Entendendo os dados |
df.info()
df.describe()
print(df.columns)
print(df)

# | Dados essenciais para Análise |
# // title, price, reviews, category , rating.
df_essencial = df[['title', 'price', 'reviews', 'category', 'rating']]
print(df_essencial.head())

# | Dados úteis para análise |
# // discountPercentage, stock.
df_uteis = df[['discountPercentage', 'stock']]
print(df_uteis)

# | Criação de colunas úteis |

# Potencial Bruto
df['potencialBruto'] = df['price'] * df['stock']
print(df['potencialBruto'].dtype)     # -- Verificando o tipo de dado da coluna potencialBruto -- 
print(f"Faturamento Potencial Bruto: ${df['potencialBruto'].sum():.2f}")

# Gráfico Faturamento Bruto por Categoria
Faturamento_bruto = df.groupby(df['category'])['potencialBruto'].sum().sort_values(ascending=False)
criar_grafico(Faturamento_bruto, tipo='pie', titulo='Faturamento Bruto por Categoria', xlabel='', ylabel='')

# Potencial líquido
df['potencialLiquido'] = df['potencialBruto'] * (1 - df['discountPercentage'] / 100)
print(df['potencialLiquido'].dtype)     # -- Verificando o tipo de dado da coluna potencialLiquido -
print(f"Faturamento Potencial Líquido: ${df['potencialLiquido'].sum():.2f}")

# Gráfico Faturamento Líquido por Categoria
Faturamento_liquido = df.groupby(df['category'])['potencialLiquido'].sum().sort_values(ascending=False)
criar_grafico(Faturamento_liquido, tipo='pie', titulo='Faturamento Líquido por Categoria', xlabel='', ylabel=' ') 

# Rating Reviews
Rating_Reviews_faturamento = df.groupby(df['category'])['rating'].mean().sort_values(ascending=False)
criar_grafico(Rating_Reviews_faturamento, tipo='bar', titulo='Média de Avaliações por Categoria', xlabel='Categoria', ylabel='Média de Avaliações')

# Desconto médio por categoria
Desconto_medio = df.groupby(df['category'])['discountPercentage'].mean().sort_values(ascending=False)
criar_grafico(Desconto_medio, tipo='bar', titulo='Desconto Médio por Categoria', xlabel='Categoria', ylabel='Desconto Médio (%)')
