# 📈 Análise de Dados Hospitalares - Aprendizagem de Máquina

Projeto da disciplina de **Aprendizagem de Máquina** focado em análise estatística de um conjunto de dados hospitalares.

---

## 🌟 Objetivo

Realizar uma análise exploratória dos dados, extraindo estatísticas descritivas, medidas de correlação, além de identificar padrões e possíveis outliers por meio de visualizações gráficas.

O conjunto de dados utilizado é o **`hospital.xlsx`**, fornecido na primeira aula.

---

## 📋 Atividades Propostas

1. **Estatísticas Univariadas**
   Para cada coluna do conjunto de dados:

   * Frequências
   * Moda
   * Média
   * Mediana
   * Desvio-padrão
   * Quartis (Q1, Q3)
   * Obliquidade (Skewness)
   * Curtose (Kurtosis)

2. **Estatísticas Multivariadas**

   * Cálculo da matriz de covariância
   * Cálculo da matriz de correlação
     *(Aplicável aos atributos quantitativos)*

3. **Análise de Outliers**

   * Geração de **boxplots** para os atributos pertinentes
   * Identificação visual de outliers

4. **Distribuição de Dados**

   * Geração de **histogramas** dos atributos
   * Interpretação das distribuições considerando as classes (ex.: diagnóstico)

---

## 🛠️ Tecnologias Recomendadas

* Python 3.8+
* Bibliotecas:

  * `pandas`
  * `numpy`
  * `matplotlib`

---

## ✅ Pré-requisitos

* Ter o Python instalado
* Git (opcional, caso queira clonar o repositório)

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório ou baixe os arquivos

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie o ambiente virtual (recomendado)

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

### 5. Adicione o arquivo de dados

Coloque o arquivo **`hospital.xlsx`** na raiz do projeto (mesma pasta do script).

### 6. Execute a análise

```bash
python analise_hospital.py
```

---

## 📊 Resultados Esperados

Ao rodar o script, o programa irá gerar:

* Estatísticas descritivas (média, mediana, moda, etc.)
* Matrizes de **covariância** e **correlação**
* **Boxplots** para visualização de outliers
* **Histogramas** por classe (ex.: por diagnóstico)

---

## 📁 Estrutura do Projeto

``` bash
.
├── .gitignore
├── README.md
├── requirements.txt
├── hospital.xlsx
└── analise_hospital.py
```

---

## 📌 Observações Finais

> Este projeto é de caráter educacional e tem como foco a prática de técnicas de análise de dados, estatística descritiva e visualização com Python.
