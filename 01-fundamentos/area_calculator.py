'''Funções Simples (Definição e Chamada)Enunciado: Defina uma função chamada calcular_area_circulo que recebe um parâmetro raio (float). 
A função deve calcular a área do círculo e retornar o resultado. 
Chame a função com um valor de raio de 5.0 e imprima o resultado com uma mensagem clara. '''

import math

def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

raio = 5.0
area = calcular_area_circulo(raio)

print(f'A área do círculo com raio {raio} é {area:.2f}')