from abc import ABC, abstractmethod
from dataclasses import dataclass

from projeto.endereco import Endereco


@dataclass
class Funcionario(ABC):
    nome:str
    email:str
    salario:float
    endereco:Endereco
    
    def salario_final(self):
        return self.salario
    
    def exibir (self):
        return(f"\nnome:{self.nome}"
               f"\nEmail:{self.email}"
               f"\nSalario:{self.salario}"
               f"\nEndereco:{self.endereco}"
               )
        