from projeto.endereco import Endereco
from projeto.engenheiro import Engenheiro
from projeto.nutricionista import Nutricionista


nutricionista = Nutricionista(
    nome="fran",
    email="fran@gmail",
    salario= 1.599,
    endereco=Endereco("Rua", 12, "ao lado da sorveteria"),

)

engenheiro = Engenheiro(
    nome="SALO",
    email="salo@gmail",
    salario= 1.499,
    endereco=Endereco("Rua", 13, "ao lado DO BAR"),

)

nutricionista.exibir()
engenheiro.exibir()