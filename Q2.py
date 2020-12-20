# Teste de Python - Summer Job Navi
# Candidato: Samuel Cruz Fernandes
# Questão 2

# Importando modulos necessários
import math
import statistics

# Definições iniciais
tamanho = 10
x = list(range(tamanho))
aux = 0
pos_maior = 0

# Alimentando o vetor x
for i in range(tamanho):
    if i % 2 == 0:
        x[i] = math.pow(3, i) + 7*math.factorial(i)
    else:
        x[i] = math.pow(2, i) + 4*math.log(i)

# Calculo da média do vetor x
media_x = round(statistics.mean(x), 2)

# Encontrando a posicao do maior elemento
for i in range(tamanho):
    if x[i] > aux:
        aux = x[i]
        pos_maior = i

print(f'O maior valor está na posição {pos_maior} e a média dos valores vale {media_x}')
