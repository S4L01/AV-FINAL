from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro:str
    numero:str
    complemento:str

    def exibir (self):
        return(f"\nLogradouro:{self.logradouro}"
               f"\nNumero:{self.numero}"
               f"\nComplemento:{self.complemento}"
               )