from projeto.funcionario import Funcionario


class Engenheiro(Funcionario):
    crea:str

    def exibir(self):
        return super().exibir()