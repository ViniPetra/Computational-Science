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

        self.chegadas = []
        self.saidas = []
        self.in_queue = []
        self.in_system = []
        self.horarios_nas_filas = []
        self.tamanho_da_fila = []

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

    def config(self):
        serie = {
            "carros_por_tempo": self.carros_por_tempo,
            "tempo_pedagio": self.tempo_pedagio,
            "desvio_tempo_pedagio": self.desvio_tempo_pedagio,
            "cabines_abertas": self.cabines_abertas,
            "tempo_simulacao": self.tempo_simulacao
        }
        return serie

    def log_info_fila(self):
        agora = self.env.now
        tamanho_da_fila_agora = len(self.pedagios.queue)
        self.horarios_nas_filas.append(agora)
        self.tamanho_da_fila.append(tamanho_da_fila_agora)
        return agora

    def calcula_tempo_no_sistema(self, horario_chegada):
        horario_saida = self.env.now
        self.saidas.append(horario_saida)
        tempo_total = horario_saida - horario_chegada
        self.in_system.append(tempo_total)

    def frame(self):
        """
        df = pd.DataFrame({
            "Horário": self.horarios_nas_filas,
            "Tamanho": self.tamanho_da_fila,
            "Chegadas": self.chegadas,
            "Partidas": self.saidas
        })
        return df
        """
        df1 = pd.DataFrame(self.horarios_nas_filas, columns=['Horário'])
        df2 = pd.DataFrame(self.tamanho_da_fila, columns=['Tamanho'])
        df3 = pd.DataFrame(self.chegadas, columns=['Chegadas'])
        df4 = pd.DataFrame(self.saidas, columns=['Partidas'])
        df = pd.concat([df1, df2, df3, df4], axis=1)
        return df

    def plot(self):
        df = self.frame()
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 5.4)

        x1, y1 = list(df['Chegadas'].keys()), df['Chegadas']
        x2, y2 = list(df['Partidas'].keys()), df['Partidas']

        ax.plot(x1, y1, color='blue', marker="o", linewidth=0, label="Chegada")
        ax.plot(x2, y2, color='red', marker="o", linewidth=0, label="Saída")
        ax.set_xlabel('Tempo')
        ax.set_ylabel('ID Carro')
        ax.set_title("Chegadas & Saídas nos Pedágios")
        ax.legend()

        fig2, ax2 = plt.subplots()
        fig2.set_size_inches(10, 5.4)

        ax2.plot(df['Horário'], df['Horário'], color='blue', linewidth=1)
        ax2.set_xlabel('Tempo')
        ax2.set_ylabel('No Carros')
        ax2.set_title('Número de carros na fila')
        ax2.grid()

        fig.show()
        fig2.show()

    def master(self):
        self.run_env()
        self.frame()
        self.plot()


def distribuicao_chegada_de_carros(teste: Testes):
    tempo_do_proximo_carro = expon.rvs(scale=teste.carros_por_tempo, size=1)
    return tempo_do_proximo_carro


def chegada_dos_carros(teste: Testes):
    id_carro = 0
    while True:
        tempo_do_proximo_carro = distribuicao_chegada_de_carros(teste)
        yield teste.env.timeout(tempo_do_proximo_carro)
        tempo_de_chegada = teste.env.now
        teste.chegadas.append(tempo_de_chegada)
        id_carro += 1
        print('%3d chegou no pedágio em %.2f' % (id_carro, tempo_de_chegada))
        teste.env.process(cobranca(id_carro, tempo_de_chegada, teste))


def tempo_de_cobranca(teste: Testes):
    return norm.rvs(loc=teste.tempo_pedagio, scale=teste.desvio_tempo_pedagio, size=1)


def cobranca(id_carro, horario_chegada, teste: Testes):
    with teste.pedagios.request() as req:
        print('%3d entrou na fila em %.2f' % (id_carro, teste.env.now))
        horario_entrada_da_fila = teste.log_info_fila()
        yield req

        print('%3d saiu da fila em %.2f' % (id_carro, teste.env.now))
        horario_saida_da_fila = teste.log_info_fila()

        tempo_na_fila = horario_saida_da_fila - horario_entrada_da_fila
        teste.in_queue.append(tempo_na_fila)

        tempo_pesagem = tempo_de_cobranca(teste)
        yield teste.env.timeout(tempo_pesagem)
        print('%3d permaneceu no sistema por %.2f' % (id_carro, tempo_pesagem))

        teste.calcula_tempo_no_sistema(horario_chegada)


teste1 = Testes(2, 20, 0.5, 10, 200)
print(teste1)
print(teste1.config())
teste1.run_env()
teste1.plot()
