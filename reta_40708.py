from ponto_40708 import Ponto3D

TOLERANCIA_ZERO = 10**(-10) 

class ErroPontosCoincidentes(Exception):
    """Esta é a classe do erro de pontos coincidentes."""
    

class Reta:

    def __init__(self, origem, destino):

        self.origem = origem
        self.destino = destino

        vetor = destino - origem
        norma = vetor.comprimento()
        if norma < TOLERANCIA_ZERO:
            # lançar a exceção ErroPontosCoincidentes
            raise ErroPontosCoincidentes
        
        self.vetor_diretor = vetor.versor()

    def __repr__(self):

        return "Reta(" + str(self.origem) + ", " + str(self.destino) + \
               ", " + str(self.vetor_diretor) + ")"

    def get_origem(self):
        
        return self.origem

    def get_destino(self):

        return self.destino

    def get_vetor_diretor(self):

        return self.vetor_diretor


if __name__ == "__main__":

    print("\nteste ao construtor")
    # teste ao construtor
    p1 = Ponto3D(0.0, 0.0, 0.0)
    p2 = Ponto3D(1.0, 2.0, 3.0)

    r1 = Reta(p1, p2)

    # intersetar excepçoes
    try:               
        r2 = Reta(p1, p1)
##    except Exception:
##        """Excepções por fazer"""
##        pass
    except ErroPontosCoincidentes:
        print("Foi definida uma reta só com um ponto")

    print("\nteste a __repr__")
    print(r1)

    print("\nteste aos gets")
    print("Origem de r1 = " + str(r1.get_origem()))
    print("Destino de r1 = " + str(r1.get_destino()))
    print("Vetor diretor de r1 = " + str(r1.get_vetor_diretor()))




    



