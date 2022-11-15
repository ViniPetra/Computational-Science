import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

notas = pd.read_csv("https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/notas-estudantes.csv")

print(notas)

x1 = notas["nota_1"]
x2 = notas["nota_2"]
y = notas["resultado"]


def plotData(data, label_x, label_y, label_pos, label_neg, axes=None):
    neg = (notas['resultado'] == 0)
    pos = (notas['resultado'] == 1)

    if axes == None:
        axes = plt.gca()
        axes.scatter(data[pos][["nota_1"]], data[pos][["nota_2"]], marker='+', c='k', s=60, linewidth=2,
                     label=label_pos)
        axes.scatter(data[neg][["nota_1"]], data[neg][["nota_2"]], c='y', s=60, label=label_neg)
        axes.set_xlabel(label_x)
        axes.set_ylabel(label_y)
        axes.legend(frameon=True, fancybox=True)
    # plt.show()


plotData(notas, 'Nota 1', 'Nota 2', 'Aprovado', 'Reprovado')


def sigmoide(x1, x2, a, b, c):
    return 1 / (1 + np.e ** -(a * x1 + b * x2 + c))


def cross_entropy(n, p, y):
    return (1 / n) * (np.sum(-y * np.log(p)) - np.sum((1 - y) * np.log(1 - p)))


def descida_gradiente(x1, x2, y, iteracao=10000, alfa=1e-6, limite_parada=1e-6):
    a = 0.02
    b = 0.03
    c = 4
    n = float(len(x1))

    perdas = []
    variacao_a = []
    variacao_b = []
    perda_anterior = float('inf')

    for i in range(iteracao):
        p = sigmoide(x1, x2, a, b, c)

        perda_atual = cross_entropy(n, p, y)

        if abs(perda_anterior - perda_atual) <= limite_parada:
            return a, b, c, perdas, variacao_a, variacao_b

        perda_anterior = perda_atual

        perdas.append(perda_atual)
        variacao_a.append(a)
        variacao_b.append(b)

        derivada_a = (1 / n) * np.sum(x1 * (p - y))
        derivada_b = (1 / n) * np.sum(x2 * (p - y))
        derivada_c = (1 / n) * np.sum(p - y)

        a = a - (alfa * derivada_a)
        b = b - (alfa * derivada_b)
        c = c - (alfa * derivada_c)
    return a, b, c, perdas, variacao_a, variacao_b


t_perdas = []
t_variacao_a = []
t_variacao_b = []
t_perdaConfig = []
t_alfa = []
t_iteracoes = []

iteracoes = [10000, 20000, 30000]
alfas = [0.1, 0.01, 0.001]
perdas2 = [1e-6, 1e-3]


def teste(x1, x2, y, iteracoes, alfas, perdas2):
    for p in perdas2:
        for alfa in alfas:
            for i in iteracoes:
                print(p, alfa, i)
                a, b, c, perdas, variacao_a, variacao_b = descida_gradiente(x1, x2, y, iteracao=i, alfa=alfa, limite_parada=p)
                for item1 in variacao_a:
                    t_variacao_a.append(item1)
                    t_perdaConfig.append(p)
                    t_alfa.append(alfa)
                    t_iteracoes.append(i)
                for item2 in variacao_b:
                    t_variacao_b.append(item2)
                for item3 in perdas:
                    t_perdas.append(item3)


print("Inciando testes")

teste(x1, x2, y, iteracoes, alfas, perdas2)

a, b, c, perdas, variacao_a, variacao_b = descida_gradiente(x1, x2, y, iteracao=10000, alfa=1e-6, limite_parada=1e-6)
print(f"A: {a}\nB: {b}\nC: {c}")

print("Teste finalizado")

fig, graph = plt.subplots()
index = np.arange(len(perdas))
graph.plot(index, perdas)
graph.set_xlabel(" Iterações ")
graph.set_ylabel(" Erro ")
fig.show()

testeFrame = pd.DataFrame({
    "Config Perda" : t_perdaConfig,
    "Alfa" : t_alfa,
    "Iterações" : t_iteracoes,
    "Perdas" : t_perdas,
    "Variação A" : t_variacao_a,
    "Variação B" : t_variacao_b
})

print(testeFrame)
print(testeFrame[testeFrame.Perdas == testeFrame.Perdas.min()])

#testeFrame.to_csv("D:/Repositórios/PI4-Computacao-Cientifica/teste/testeres.csv")
