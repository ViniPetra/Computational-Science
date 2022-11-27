import simpy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

'''Descrição da atividade'''
CASO = "Pagamento de pedágio"
FILAS = "Carros para pagar"
SERVICO = "Cabines abertas"
INTEGRANTES = ["Julia mendes", "Vinicius Petratti", "Yuri Barbosa"]

'''Parâmetros dos testes'''
CARROS_POR_TEMPO = 2
TEMPO_PEDAGIO = 20
DESVIO_PADRAO_DO_TEMPO_PEDAGIO = 0.5
CABINES_ABERTAS = 10
TEMPO_DE_SIMULACAO = 200

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


def distribuicao_chegada_de_carros():
    tempo_do_proximo_carro = expon.rvs(scale=CARROS_POR_TEMPO, size=1)
    return tempo_do_proximo_carro


def calcula_tempo_no_sistema(enviroment, horario_chegada):
    horario_saida = enviroment.now
    saidas.append(horario_saida)
    tempo_total = horario_saida - horario_chegada
    in_system.append(tempo_total)


def chegada_dos_carros(enviroment):
    id_carro = 0
    while True:
        tempo_do_proximo_carro = distribuicao_chegada_de_carros()
        yield enviroment.timeout(tempo_do_proximo_carro)
        tempo_de_chegada = enviroment.now
        chegadas.append(tempo_de_chegada)
        id_carro += 1
        print('%3d chegou no pedágio em %.2f' % (id_carro, tempo_de_chegada))
        enviroment.process(cobranca(enviroment, id_carro, tempo_de_chegada))


def tempo_de_cobranca():
    return norm.rvs(loc=TEMPO_PEDAGIO, scale=DESVIO_PADRAO_DO_TEMPO_PEDAGIO, size=1)


def cobranca(enviroment, id_carro, horario_chegada):
    with pedagios.request() as req:
        print('%3d entrou na fila em %.2f' % (id_carro, env.now))
        horario_entrada_da_fila = log_info_fila(enviroment, pedagios)
        yield req

        print('%3d saiu da fila em %.2f' % (id_carro, enviroment.now))
        horario_saida_da_fila = log_info_fila(enviroment, pedagios)

        tempo_na_fila = horario_saida_da_fila - horario_entrada_da_fila
        in_queue.append(tempo_na_fila)

        tempo_pesagem = tempo_de_cobranca()
        yield enviroment.timeout(tempo_pesagem)
        print('%3d permaneceu no sistema por %.2f' % (id_carro, tempo_pesagem))

        calcula_tempo_no_sistema(enviroment, horario_chegada)


'''Configuração do ambiente'''
np.random.seed(seed=1)
env = sp.Environment()
pedagios = sp.Resource(env, capacity=CABINES_ABERTAS)
env.process(chegada_dos_carros(env))
env.run(until=TEMPO_DE_SIMULACAO)

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

'''Configuração de testes'''


class Testes:
    def __int__(self, CARROS_POR_TEMPO, TEMPO_PEDAGIO, DESVIO_PADRAO_DO_TEMPO_PEDAGIO, CABINES_ABERTAS,
                TEMPO_DE_SIMULACAO):
        self.CARROS_POR_TEMPO = CARROS_POR_TEMPO
        self.TEMPO_PEDAGIO = TEMPO_PEDAGIO
        self.DESVIO_PADRAO_DO_TEMPO_PEDAGIO = DESVIO_PADRAO_DO_TEMPO_PEDAGIO
        self.CABINES_ABERTAS = CABINES_ABERTAS
        self.TEMPO_DE_SIMULACAO = TEMPO_DE_SIMULACAO
