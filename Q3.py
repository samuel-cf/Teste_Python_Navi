# Teste de Python - Summer Job Navi
# Candidato: Samuel Cruz Fernandes
# Questão 3

# Pegando as informações das notas
notas = list(range(5))
for item in range(5):
    notas[item] = input(f'Digite a nota do Aluno {item+1}: ')

# Adicionando as informações no dicionário
turma = dict(Aluno_1=notas[0], Aluno_2=notas[1], Aluno_3=notas[2], Aluno_4=notas[3], Aluno_5=notas[4])

# Procurando a maior nota
maior = 0.00
aluno = "Inicio"
for key in turma:
    aux = float(turma[key])
    if aux > maior:
        maior = aux
        aluno = key

print(f'O aluno com maior nota foi o {aluno} e sua nota foi {maior}.')
