from dataclasses import dataclass
from projeto.endereco import Endereco
from projeto.funcionario import Funcionario

@dataclass
class Nutricionista(Funcionario):
    crn:str

    def exibir(self):
        return super().exibir()