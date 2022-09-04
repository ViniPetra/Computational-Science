from cProfile import label
from turtle import shapetransform
import matplotlib.pyplot as plt
import numpy as np

mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 1 - Total de produtos Vendidos por mês - Linha
# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras
# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)
# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto

#1
ArraysSum = creme_facial + limpeza_facial + pasta_dentaria + sabonete + shampoo + hidratante
Ex1_fig, Ex1_x = plt.subplots()
Ex1_x.plot(mes, ArraysSum, color="blue", )

Ex1_x.set_xlabel("Mês") 
Ex1_x.set_ylabel("Unidades vendidas")
Ex1_fig.set_size_inches(15 ,5)
Ex1_x.set_xticks(mes)

#plt.show()

#2
Ex2_fig, Ex2_x = plt.subplots()
Ex2_x.plot(mes, creme_facial, label="Creme facial")
Ex2_x.plot(mes, limpeza_facial, label="Limpeza facial")
Ex2_x.plot(mes, pasta_dentaria, label="Pasta dentária")
Ex2_x.plot(mes, sabonete, label="Sabonete")
Ex2_x.plot(mes, shampoo, label="Shampoo")
Ex2_x.plot(mes, hidratante, label="Hdratante")

Ex2_x.set_xlabel("Mês")
Ex2_x.set_ylabel("Unidades vendidas")
Ex2_fig.set_size_inches(15 ,5)
Ex2_fig.legend()
Ex2_x.set_xticks(mes)

#plt.show()

#3
Ex3_fig, Ex3_x = plt.subplots()

barsize = 0.3

Ex3_x.bar(mes - barsize/2, creme_facial, barsize, label="Creme Facial")
Ex3_x.bar(mes + barsize/2, limpeza_facial, barsize, label="Limpeza Facial")

Ex3_fig.legend()
Ex3_x.set_xticks(mes)

#plt.show()

#4
# Ex4_fig, Ex4_x = plt.subplots()

# AllArrays = [creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante]

# Ex4_x.hist(AllArrays, bins=1000)

# plt.show()

#5
Ex5_fig, Ex5_x = plt.subplots()

sums = [np.sum(creme_facial), np.sum(limpeza_facial), np.sum(pasta_dentaria), np.sum(sabonete), np.sum(shampoo), np.sum(hidratante)]
total = np.sum(sums)
values = []

labels = ["Creme facial", "Limpeza facial", "Pasta dentária", "Sabonete", "Shampoo", "Hidratante"]

for indexes in sums:
    values.append(round(((indexes*100)/total), 2))

Ex5_x.pie(values, labels=labels, shadow=True, autopct='%1.1f%%')

plt.show()