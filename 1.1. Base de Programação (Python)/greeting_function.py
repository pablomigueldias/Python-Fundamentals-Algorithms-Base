'''Funções com Parâmetros Opcionais (Default)
Defina uma função chamada saudar que aceita dois parâmetros: nome (obrigatório) e prefixo (opcional, com valor default definido como "Olá"). A função deve retornar uma string de saudação no formato: "[Prefixo], [Nome]!". Teste a função chamando-a de duas maneiras:

Apenas com o nome.

Com o nome e o prefixo diferente (ex: "Bom dia").'''

def saudar(nome, prefixo='Olá'):
    return f'{prefixo}, {nome}!'

print(saudar('Pablo'))