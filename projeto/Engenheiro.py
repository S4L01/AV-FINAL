from dataclasses import dataclass
from projeto.Funcionario import Funcionario


@dataclass
class Engenheiro(Funcionario):
    crea:str