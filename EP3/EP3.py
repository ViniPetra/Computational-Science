"""
Descrição da atividade
CASO = "Pagamento de pedágio"
FILAS = "Carros para pagar"
SERVICO = "Cabines abertas"
INTEGRANTES = ["Julia mendes", "Vinicius Petratti", "Yuri Barbosa"]
"""

import simpy as sp
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from scipy.stats import norm, expon


class Testes:
    def __init__(self, carros_por_tempo, tempo_pedagio, desvio_tempo_pedagio, cabines_abertas,
                 tempo_simulacao):
        self.carros_por_tempo = carros_por_tempo
        self.tempo_pedagio = tempo_pedagio
        self.desvio_tempo_pedagio = desvio_tempo_pedagio
        self.cabines_abertas = cabines_abertas
        self.tempo_simulacao = tempo_simulacao

        np.random.seed(seed=1)
        env = sp.Environment()
        self.pedagios = sp.Resource(env, capacity=self.cabines_abertas)
        env.process(chegada_dos_carros(self))
        self.env = env

    def __str__(self):
        serie = {
            "carros_por_tempo": self.carros_por_tempo,
            "tempo_pedagio": self.tempo_pedagio,
            "desvio_tempo_pedagio": self.desvio_tempo_pedagio,
            "cabines_abertas": self.cabines_abertas,
            "tempo_simulacao": self.tempo_simulacao
        }
        serie_json = json.dumps(serie)
        return serie_json

    def run_env(self):
        self.env.run(until=self.tempo_simulacao)


'''Listas de dados'''
chegadas, saidas = [], []
in_queue, in_system = [], []
horarios_nas_filas, tamanho_da_fila = [], []


def log_info_fila(enviroment, pedagio):
    agora = enviroment.now
    tamanho_da_fila_agora = len(pedagio.queue)
    horarios_nas_filas.append(agora)
    tamanho_da_fila.append(tamanho_da_fila_agora)
    return agora


def distribuicao_chegada_de_carros(teste: Testes):
    tempo_do_proximo_carro = expon.rvs(scale=teste.carros_por_tempo, size=1)
    return tempo_do_proximo_carro


def calcula_tempo_no_sistema(enviroment, horario_chegada):
    horario_saida = enviroment.now
    saidas.append(horario_saida)
    tempo_total = horario_saida - horario_chegada
    in_system.append(tempo_total)


def chegada_dos_carros(teste: Testes):
    id_carro = 0
    while True:
        tempo_do_proximo_carro = distribuicao_chegada_de_carros(teste)
        yield teste.env.timeout(tempo_do_proximo_carro)
        tempo_de_chegada = teste.env.now
        chegadas.append(tempo_de_chegada)
        id_carro += 1
        print('%3d chegou no pedágio em %.2f' % (id_carro, tempo_de_chegada))
        teste.env.process(cobranca(id_carro, tempo_de_chegada, teste))


def tempo_de_cobranca(teste: Testes):
    return norm.rvs(loc=teste.tempo_pedagio, scale=teste.desvio_tempo_pedagio, size=1)


def cobranca(id_carro, horario_chegada, teste: Testes):
    with teste.pedagios.request() as req:
        print('%3d entrou na fila em %.2f' % (id_carro, teste.env.now))
        horario_entrada_da_fila = log_info_fila(teste.env, teste.pedagios)
        yield req

        print('%3d saiu da fila em %.2f' % (id_carro, teste.env.now))
        horario_saida_da_fila = log_info_fila(teste.env, teste.pedagios)

        tempo_na_fila = horario_saida_da_fila - horario_entrada_da_fila
        in_queue.append(tempo_na_fila)

        tempo_pesagem = tempo_de_cobranca(teste)
        yield teste.env.timeout(tempo_pesagem)
        print('%3d permaneceu no sistema por %.2f' % (id_carro, tempo_pesagem))

        calcula_tempo_no_sistema(teste.env, horario_chegada)


teste1 = Testes(2, 20, 0.5, 10, 200)
print(teste1)
teste1.run_env()


'''Criação dos dataframes'''
df1 = pd.DataFrame(horarios_nas_filas, columns=['horario'])
df2 = pd.DataFrame(tamanho_da_fila, columns=['tamanho'])
df3 = pd.DataFrame(chegadas, columns=['chegadas'])
df4 = pd.DataFrame(saidas, columns=['partidas'])
df_tamanho_da_fila = pd.concat([df1, df2], axis=1)
df_entrada_saida = pd.concat([df3, df4], axis=1)

'''Cofiguração dos plots'''
fig, ax = plt.subplots()
fig.set_size_inches(10, 5.4)

x1, y1 = list(df_entrada_saida['chegadas'].keys()), df_entrada_saida['chegadas']
x2, y2 = list(df_entrada_saida['partidas'].keys()), df_entrada_saida['partidas']

ax.plot(x1, y1, color='blue', marker="o", linewidth=0, label="Chegada")
ax.plot(x2, y2, color='red', marker="o", linewidth=0, label="Saída")
ax.set_xlabel('Tempo')
ax.set_ylabel('ID Carro')
ax.set_title("Chegadas & Saídas nos Pedágios")
ax.legend()

fig2, ax2 = plt.subplots()
fig2.set_size_inches(10, 5.4)

ax2.plot(df_tamanho_da_fila['horario'], df_tamanho_da_fila['tamanho'], color='blue', linewidth=1)
ax2.set_xlabel('Tempo')
ax2.set_ylabel('No Carros')
ax2.set_title('Número de carros na fila')
ax2.grid()

# fig.show()
# fig2.show()
