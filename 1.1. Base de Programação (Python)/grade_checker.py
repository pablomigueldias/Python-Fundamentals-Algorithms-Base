'''Condicionais (if/elif/else) e Operadores
Escreva um script que solicite ao usuário a nota de um aluno (entre 0 e 100) e imprima o conceito de acordo com as seguintes regras:

Aprovado com Distinção: Nota maior ou igual a 90.

Aprovado: Nota entre 70 e 89 (inclusive).

Recuperação: Nota entre 50 e 69 (inclusive).

Reprovado: Nota abaixo de 50.'''

usuario = int(input("Digite a nota do aluno (0-100): "))
if usuario >= 90:
    print('Aprovado com Distinção')
elif 70 <= usuario <= 89:
    print('Aprovado')
elif 50 <= usuario <= 69:
    print('Recuperação')
else:
    print('Reprovado')