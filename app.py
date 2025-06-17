import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import os

# Carregar o arquivo Excel
df = pd.read_excel("hospital.xlsx")

# Selecionar colunas numéricas
quant_cols = ['IDADE', 'PESO', 'TEMP.', '#INT.']

print("=== ESTATÍSTICAS UNIVARIADAS ===")
for col in quant_cols:
    print(f"\nColuna: {col}")
    print(f"  Média: {df[col].mean():.2f}")
    print(f"  Mediana: {df[col].median():.2f}")
    print(f"  Moda: {df[col].mode()[0]}")
    print(f"  Desvio-Padrão: {df[col].std():.2f}")
    print(f"  Q1: {df[col].quantile(0.25):.2f}")
    print(f"  Q3: {df[col].quantile(0.75):.2f}")
    print(f"  Obliquidade: {skew(df[col]):.2f}")
    print(f"  Curtose: {kurtosis(df[col]):.2f}")

print("\n=== COVARIÂNCIA ===")
print(df[quant_cols].cov().round(2))

print("\n=== CORRELAÇÃO DE PEARSON ===")
print(df[quant_cols].corr().round(2))

# BOXPLOTS
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
for i, col in enumerate(quant_cols):
    plt.subplot(2, 2, i+1)
    sns.boxplot(y=df[col])
    plt.title(f"Boxplot: {col}")
plt.tight_layout()
plt.savefig("boxplots.png")
print("📦 Boxplots salvos em 'boxplots.png'")

# HISTOGRAMAS
plt.figure(figsize=(14, 10))
for i, col in enumerate(quant_cols):
    plt.subplot(2, 2, i+1)
    sns.histplot(data=df, x=col, hue="DIAGNÓSTICO", kde=True, palette="Set2")
    plt.title(f"Histograma de {col} por Diagnóstico")
plt.tight_layout()
plt.savefig("histogramas.png")
print("📦 Histogramas salvos em 'histogramas.png'")