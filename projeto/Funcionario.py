from abc import ABC, abstractmethod
from dataclasses import dataclass

from projeto.Endereco import Endereco

@dataclass
class Funcionario(ABC):
    nome:str
    email:str
    salario:float
    endereco:Endereco

    @abstractmethod
    def salario_final(self):
        return self.salario
    
    def exibir_dados(self):
        return (f"\nNome:{self.nome}"
                f"\nE-mail:{self.email}"
                f"\nSalario:{self.salario}"
                f"\nSalario Final:{self.salario_final}"
                f"\nEndereco:{self.endereco.exibir_dados}"

                )
                
