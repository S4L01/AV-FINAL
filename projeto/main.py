from projeto.Engenheiro import Engenheiro


engenheiro = Engenheiro()
print("\nDados do Engenheiro:")
engenheiro.nome = input("Digite seu nome:")
engenheiro.email = input("Digite seu email:")
engenheiro.salario = input("Digite seu salário:")
engenheiro.crea = input("Digite seu crea:")
print("\nEndereço do Engenheiro:")
engenheiro.endereco.logradouro = input("Digite o logradouro:")
engenheiro.endereco.numero = input("Digite o número:")
engenheiro.endereco.complemento = input("Digite o complemento:")

engenheiro.exibir_dados()
