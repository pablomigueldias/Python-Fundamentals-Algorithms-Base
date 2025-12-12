'''Classes com Métodos
Estenda a classe Pessoa do script anterior.

Adicione um método chamado calcular_idade que não recebe parâmetros extras além do self.

Este método deve calcular a idade da pessoa subtraindo o ano_nascimento do ano atual (considere o ano atual como 2025 para simplificação).

Chame o método calcular_idade no objeto que você criou e imprima a idade resultante.'''

from person_class import Pessoa
import datetime

class PessoaComIdade(Pessoa):
    def calcular_idade(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.ano_nascimento
    
p1 = PessoaComIdade('Pablo', 1997)
    
print(f'Idade: {p1.calcular_idade()} anos')