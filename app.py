"""
Docstring do módulo 'app.py'
"""


# Classes

class Astride:

    def __init__(self,qualidade):
        self._qualidade = qualidade
    
    @property
    def qualidade(self):
        return self._qualidade
    
    @qualidade.setter
    def qualidade(self,valor):
        if isinstance(valor,str):
            self._qualidade = valor
        else:
            raise ValueError(f"\nO valor atribuido tem que ser uma String!")
    
    def mostra_qualidade(self):
        return f"A Astride é {self._qualidade}"
    

# Função Main

def main():

    a = Astride("Gostosa")
    print(a.mostra_qualidade())

    a.qualidade = "Tesuda"
    print(a.mostra_qualidade())


if __name__ == "__main__":
    main()