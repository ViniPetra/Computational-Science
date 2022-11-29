<h2>Ex 1</h2>
Fazer um módulo que converte: <br />
Pé -> Metros -> Pé: Entrada do usuário que define a conversão<br />
1 pé = 0,3048 metros<br />
1 metro = 3,281 pés<br />
Entregar 1 código por grupo de 2<br />

<h2>Ex 2</h2>
Dado os arquivos em anexo:<br />
anos.txt ⇒ ano de nascimento das pessoas em ordem<br />
altura ⇒ alturas das pessoas em ordem<br />
Importe os 2 arquivos e descubra a média de altura de quem nasceu entre 1998 e 2005.<br />

<h2>Ex 3</h2>
Gerar o seguintes gráficos:<br />
Gráfico 1 - Total de produtos Vendidos por mês - Linha<br />
Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha<br />
Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras<br />
Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)<br />
Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto<br />

<h2>Ex 4</h2>

1. importar os dados de CSV do dataset de seeds: https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv<br /> 
2.  colocar as linhas de cabeçalho:<br /> 
    a. Área A,<br />
    b. Perímetro P,<br />
    c. Extensão do núcleo,<br />
    d. Largura,<br />
    e. Coeficiente de Assimetria<br />
    f. Extensão do sulgo do núcleo.<br />
1. remover colunas extras no final<br />
2. remover as linhas com valores nulos<br />
3. Adicionar um campo Compactação cujo o cálculo é C = 4*pi*A/P^2<br />
4. Exportar para CSV o valor final<br />

<h2>Ex 5</h2>
Fazer uma regressão linear para o data set: https://www.kaggle.com/datasets/shivam2503/diamonds<br />
A partir das variáveis, calcular o preço estimado do diamante.

Usar:
- Dataset treinamento/testes
- Limpeza dos dados
- Seleção de dados de entrada que maximizam o resultado
- Calcular R2 do modelo

<h2>EP 2 - Regressão Logística</h2>

1) Fazer a função sigmoide<br />
O valor a é o peso da variável x1<br />
O valor b é o peso da variável x2<br />
O valor c é o peso do víes

1) Desenvolver a função de perda<br />
Fazer a função de perda de Cross Entropy comparando valor de $Y$ (valor de entrada) com o valor de $f(x).$<br />

1) Decida no gradiente<br />
Desenvolva a descida do gradiente usando a função sigmoide $f(x)$ e a função de perda $L(f,y)$.<br />

1) Plotagem com valores de hiperparâmetros diferentes<br />
Tesar o algoritmo com variações do valores de hiperparâmetros: $\alpha$ (taxa de aprendizado),  número de $N$ interações, e $\varepsilon$ (diferença da função de perda)<br />

1) Análises<br />
Checar $\alpha$ com ordens de grandezas: 0.1, 0.01, 0.001<br />
Quanto melhor o N, melhor. <br />
$\varepsilon$ entre $10^{-3}$ e $10^{-6}$<br />
Verificar qual é a melhor configuração para o aprendizado baseado na medida de acurácia.

<h2>EP 3 - Simulações</h2>
Sobre a modelagem, vamos usar filas do tipo M/M/c , ou seja, com chegada e tratamento sem memória e com uma distribuição de probabilidade determinada. Cada problema têm distribuições de probabilidade diferentes para chegada e tempo do serviço.<br />
<br />

Simplificações e premissas:

- FIFO nas filas, não há prioridade
- Os usuários chegam um por vez, não chegam em grupos ou lotes
- Será apenas uma fila para 1 ou c serviços.

Tente pensar situações comuns para cada problema. Os valores devem mudar de problema a problema:

- O tempo de serviço pode variar.  No problema de pesagem de caminhões, a balança pode demorar para pesar mais uns caminhões do que outros por alguma distribuição de probabilidade
- A chegada de usuário pode mudar pelo tempo. Por exemplo, um serviço bancário pode ter picos em alguns horários
- Desistência de usuários se a fila está muito grande. No caso de fila de compra de ingressos, alguém pode desistir quando o tamanho da fila está grande

O que deverá ser medido:

- Tempos que os usuários demorar no sistema e nas filas
- Tamanho das filas e variações pelo tempo
- Desistências ou Tempos críticos na fila

<h3>A Entrega</h3>

Sobre as filas e o sistema: <br/>
1) Escolher uma função de probabilidade para a chegada dos usuários
2) Escolher uma função de probabilidade para o tempo do serviços de cada usuários
3) Faça desistência ou marcações críticas de acordo de um tamanho 
4) Tamanho do tempo da simulações
5) Quantidade de serviços ao mesmo tempo ou variações da quantidade pelo tempo

Fazer várias simulações com parâmetros e funções de distribuições diferentes e plotar:
- Tempo de entrada e saída dos usuários na fila
- Tamanho das filas pelo tempo