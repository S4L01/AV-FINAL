from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro:str
    numero:str
    complemento:str


    def exibir_dados(self):
        return ("\nEndereço:"
                f"\nLogradouro:{self.logradouro}"                     
                f"\nNúmero:{self.numero}"                     
                f"\nComplemento:{self.complemento}"                     
        
        )