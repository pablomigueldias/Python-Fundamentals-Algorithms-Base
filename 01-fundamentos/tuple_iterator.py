'''Estruturas de Repetição (while) e Tuplas
Crie uma tupla de cores. Use um loop while para iterar sobre a tupla e imprimir cada cor. 
O loop deve parar de forma controlada (usando um índice ou condição de parada) após imprimir todos os elementos da tupla.'''

cores = ('vermelho', 'azul', 'verde', 'amarelo', 'roxo')

i = 0
while i < len(cores):
    print(cores[i])
    i += 1
