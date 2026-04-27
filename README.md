# 📊 Análise de Produtos — DummyJSON API

> Projeto de análise exploratória de dados utilizando Python, pandas e matplotlib, desenvolvido como parte do portfólio pessoal.

---

## 🎯 Objetivo

Explorar dados de produtos obtidos via API pública para identificar padrões de faturamento, desconto e avaliação por categoria — simulando um cenário real de análise de negócio em e-commerce.

---

## 📁 Estrutura do Projeto

```
├── main.py           # Script principal de análise
├── API.py            # Módulo de conexão e coleta da API
├── notebook.ipynb    # Análise exploratória documentada (Jupyter)
└── README.md
```

---

## 🔍 Perguntas respondidas pela análise

- Quais categorias têm maior **faturamento bruto potencial**?
- Como os **descontos** impactam o faturamento líquido por categoria?
- Quais categorias possuem os produtos com melhor **avaliação média**?
- Existe relação entre desconto médio e desempenho de faturamento?

---

## 📈 Análises realizadas

| Análise | Descrição |
|---|---|
| Faturamento Bruto | `price × stock` por categoria |
| Faturamento Líquido | Faturamento bruto ajustado pelo desconto |
| Avaliação Média | Média de `rating` por categoria |
| Desconto Médio | Média de `discountPercentage` por categoria |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.11.9**
- **pandas** — manipulação e análise de dados
- **numpy** — operações numéricas
- **matplotlib** — visualização de dados

---

## ▶️ Como executar
C:\Users\User\Desktop\Analise-de-dados-pandas-numpy
1. Clone o repositório:
```bash
git clone https://github.com/User/Analise-de-dados-pandas-numpy.git
cd Analise-de-dados-pandas-numpy
```

2. Instale as dependências:
```bash
pip install pandas numpy matplotlib
```

3. Execute a análise:
```bash
python main.py
```

Ou abra o `notebook.ipynb` no Jupyter para a versão documentada.

---

## 💡 Principais insights

- A categoria com maior faturamento bruto nem sempre é a com maior faturamento líquido — descontos elevados invertem o ranking.
- Categorias com melhor avaliação média não são necessariamente as com maior desconto, sugerindo que qualidade percebida e promoção são estratégias distintas.

---

## 👤 Autor

**Tiago Augusto Fonseca**
[LinkedIn](www.linkedin.com/in/tiago-augusto-fonseca-ab67b6371) • [GitHub](https://github.com/seu-usuario)