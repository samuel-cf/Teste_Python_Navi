# Teste de Python - Summer Job Navi
# Candidato: Samuel Cruz Fernandes
# Questão 1

# Definições iniciais
contador = 0
maximo = 5000001
aux = 2*37*49
# Números divisíveis por 2,37 e 49 -> múltiplos do produto entre eles

# Contando os múltiplos dentro do intervalo pedido
while aux < maximo:
    aux = aux + 2*37*49
    contador = contador + 1
else:
    print(f'Existem {contador} números divisíveis por 2, 37 e 49 simultaneamente entre 1 e 5000000.')
