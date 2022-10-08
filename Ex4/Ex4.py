import pandas as pd
import numpy as np

raw = pd.read_csv("https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv", header=None, index_col=None)

frame = pd.DataFrame(raw)

#Remover as colunas do final

frame.drop(columns = [6, 7, 8], axis = 1, inplace=True)

#Adicionar os cabeçalhos

frame.columns = ["Área A", "Perímetro P", "Extensão do núcleo", "Largura", "Coeficiente de Assimetria", "Extensão do sulgo do núcleo"]

#Remover linhas com valores nulos

frame.dropna(axis=0, how="any", inplace=True)

#Adicionar um campo Compactação cujo o cálculo é C = 4*pi*A/P^2

frame["Campo calculado"] = 4 * np.pi * frame["Área A"]/frame["Perímetro P"]**2

#Exportar em csv

frame.to_csv("D:\Repositórios\PI4-Computacao-Cientifica\Ex4\Ex4_export.csv")

#print

print(frame)
