
# Atividade de 'Aprendizagem de Máquina' - Análise de Dados Hospitalares
### Instruções
Considerando o conjunto de dados hospital apresentado na primeira aula (ver arquivo em anexo):

1. Calcular, para cada coluna desse conjunto de dados, as estatísticas univariadas pertinentes dentre frequências, moda, média, mediana, desvio-padrão, Q1, Q3, obliquidade e curtose.
2. Calcular estatísticas multivariadas de covariância e correção para os atributos quantitativos presentes.
3. Plotar boxplots dos atributos pertinentes e identificar a presença ou não de outliers.
4. Plotar histogramas dos atributos e interpretar sua distribuição, considerando as classes.

Recomenda-se o uso da linguagem Python e das biblioteca pandas, numpy e matplotlib para realização dos exercícios, mas não é obrigatório.


## Resumo
Este projeto realiza análise estatística de um conjunto de dados hospitalares usando Python. Inclui estatísticas descritivas, correlações, boxplots e histogramas com base no arquivo `hospital.xlsx`.

## ✅ Pré-requisitos

- Python 3.8+
- Git
---
## ⚙️ Passos para rodar o projeto

### 1. Clone o repositório (ou baixe os arquivos)
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
````

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

* **Windows**:

```bash
.venv\Scripts\activate
```

* **Linux/macOS**:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Coloque o arquivo `hospital.xlsx` na mesma pasta do script

### 6. Execute a análise

```bash
python app.py
```

---

## 📊 Resultado

O script exibirá:

* Estatísticas descritivas (média, mediana, moda, etc.)
* Matriz de covariância e correlação
* Boxplots para identificar outliers
* Histogramas separados por diagnóstico

---

## 📁 Estrutura do Projeto

```
.
├── .gitignore
├── README.md
├── requirements.txt
├── hospital.xlsx
└── analise_hospital.py
```