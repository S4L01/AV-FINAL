from projeto.endereco import Endereco
from projeto.funcionario import Funcionario


class Nutricionista(Funcionario):
    crn:str

    def exibir(self):
        return super().exibir()