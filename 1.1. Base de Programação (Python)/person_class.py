'''Classes Iniciais (Atributos e Método Construtor)
Crie uma classe chamada Pessoa.

Defina o método construtor (__init__) para que ele receba e inicialize dois atributos: nome (string) e ano_nascimento (inteiro).

Crie um objeto (instância) dessa classe, por exemplo, p1, com seu nome e ano de nascimento.

Imprima os atributos nome e ano_nascimento do objeto criado.'''

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

p1 = Pessoa('Pablo', 1997)

print(f'Nome: {p1.nome}')
print(f'Ano de Nascimento: {p1.ano_nascimento}')