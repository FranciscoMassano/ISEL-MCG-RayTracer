from vetor_40708 import Vetor3D

class Ponto3D:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        
        return self.x

    
    def get_y(self):
        
        return self.y


    def get_z(self):
        
        return self.z


    def __repr__(self):

        return "Ponto3D(" + str(self.x) + ", " + str(self.y) + ", " + \
               str(self.z) + ")"


    def adiciona_vetor(self, um_vetor):

##        resultado = Ponto3D(self.x + um_vetor.x, self.y + um_vetor.y, \
##                            self.z + um_vetor.z)
##        return resultado
        novo_x = self.x + um_vetor.x
        novo_y = self.y + um_vetor.y
        novo_z = self.z + um_vetor.z

        novo_ponto = Ponto3D(novo_x, novo_y, novo_z)

        return novo_ponto


    def __add__(self, outro_vetor):
        
        return self.adiciona_vetor(outro_vetor)


    def subtrai_ponto(self, ponto_inicial):

        resultado = Vetor3D(self.x - ponto_inicial.x, \
                            self.y - ponto_inicial.y, \
                            self.z - ponto_inicial.z)

        return resultado


    def __sub__(self, ponto_inicial):

        return self.subtrai_ponto(ponto_inicial)
    

if __name__ == "__main__":

    print()
    # teste ao construtor
    print("teste ao construtor")
    p1 = Ponto3D(1.0, 2.0, 3.0)


    print()
    # teste a get_x
    print("teste a get_x")
    print("coordenada x de p1 = " + str(p1.get_x()))

    print()
    # teste a get_y
    print("teste a get_y")
    print("coordenada x de p1 = " + str(p1.get_y()))

    print()
    # teste a get_z
    print("teste a get_z")
    print("coordenada x de p1 = " + str(p1.get_z()))
    
    print()
    # teste a __repr__
    print("teste a __repr__")
    print("p1 = " + str(p1))


    print()
    # teste a adiciona_vetor
    print("teste a adiciona_vetor")
    v1 = Vetor3D(10.0, 20.0, 30.0)
    p2 = p1.adiciona_vetor(v1)
    print("v1 = " + str(v1))
    print("p2 = " + str(p2))

    print()
    # teste a add
    print(" teste a  add")
    p3 = p1 + v1
    print("p3 = p1 + v1 = " + str(p3))

    print()
    # teste a subtrai_ponto
    print("teste a subtrai_ponto")
    v2 = p2.subtrai_ponto(p1)
    print("v2 = " + str(v2))

    print()
    # teste a sub
    print("teste a sub")
    v3 = p2 - p1
    print("v3 = " + str(v3))

