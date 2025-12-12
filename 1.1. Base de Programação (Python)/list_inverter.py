'''Defina uma função chamada inverter_lista que recebe uma lista como parâmetro. 
A função deve retornar uma nova lista contendo os elementos da lista original em ordem inversa. 
Teste a função passando uma lista de letras ou números e imprima a lista original e a lista invertida.'''

def inverter_lista(lista):
    return lista[::-1]

lista_original = [1, 2, 3, 4, 5]
lista_invertida = inverter_lista(lista_original)

print(f'Lista Original: {lista_original}')
print(f'Lista Invertida: {lista_invertida}')