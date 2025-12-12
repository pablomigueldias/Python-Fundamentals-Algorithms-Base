''' Estruturas de Repetição (for) e Listas
Crie uma lista chamada numeros com pelo menos 5 números inteiros. Em seguida, use um loop for para:

Calcular e imprimir a soma de todos os números na lista.

Identificar e imprimir o maior número da lista.

Imprimir apenas os números pares da lista.'''

numeros = [10, 23, 5, 67, 34]

def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def encontrar_maior(lista):
    return max(lista)

def imprimir_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
            

soma_total = calcular_soma(numeros)
maior_numero = encontrar_maior(numeros)
pares = imprimir_pares(numeros)

print(f'A soma dos numeros é: {soma_total}')
print(f'O mairor numero é: {maior_numero}')
print(f'os numeros pares são: {pares}')
