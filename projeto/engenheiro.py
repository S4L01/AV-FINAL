from dataclasses import dataclass
from projeto.funcionario import Funcionario

@dataclass
class Engenheiro(Funcionario):
    crea:str

    def exibir(self):
        return super().exibir()