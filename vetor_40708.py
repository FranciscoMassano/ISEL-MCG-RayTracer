class Vetor3D:

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

        resultado = "Vetor3D(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

        return resultado


    def adiciona(self, outro_vetor):

        resultado = Vetor3D(self.x + outro_vetor.x, self.y + outro_vetor.y,  self.z + outro_vetor.z)
        return resultado


    def __add__(self, outro_vetor):
        
        return self.adiciona(outro_vetor)


    def multiplica_escalar(self, escalar):
        
        resultado = Vetor3D(self.x*escalar, self.y*escalar, self.z*escalar)

        return resultado


    def __mul__(self, escalar):
        
        return self.multiplica_escalar(escalar)


    def comprimento(self):
        
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)


    def versor(self):

        resultado = 1.0 / self.comprimento()
        
        return self * resultado


    def interno(self, outro_vetor):
        
        return self.x*outro_vetor.x + self.y*outro_vetor.y + \
               self.z*outro_vetor.z


    def externo(self, outro_vetor):

        return Vetor3D(self.y * outro_vetor.z - outro_vetor.y * self.z, \
                       -(self.x * outro_vetor.z - outro_vetor.x * self.z), \
                       self.x * outro_vetor.y - outro_vetor.x * self.y)



if __name__ == "__main__":
    print()
    # teste ao construtor
    print("teste ao construtor")
    v1 = Vetor3D(1.0, 2.0, 3.0)


    print()
    # teste a get_x
    print("teste a get_x")
    print("coordenada x de v1 = " + str(v1.get_x()))

    print()
    # teste a get_y
    print("teste a get_y")
    print("coordenada y de v1 = " + str(v1.get_y()))
    
    print()
    # teste a get_z
    print("teste a get_z")
    print("coordenada z de v1 = " + str(v1.get_z()))

    print()
    # teste a __repr__
    print("teste a __repr__")
    print("v1 = " + str(v1))


    print()
    # teste a adiciona
    print("teste a adiciona")
    v2 = Vetor3D(10.0, 20.0, 30.0)
    v3 = v1.adiciona(v2)
    print("v1 = " + str(v1))
    print("v2 = " + str(v2))
    print("v3 = " + str(v3))

    print()
    # teste a + (add)
    print("teste a +")
    v4 = v1 + v2
    print("v4 = " + str(v4))

    print()
    # teste a multiplica_escalar
    print("teste a multiplica_escalar")
    a = 2.0
    v5 = v1.multiplica_escalar(a)
    print("v5 = " + str(v5))

    print()
    # teste a * (mul)
    print("teste a *")
    v6 = v1 * a
    print("v6 = " + str(v6))

    print()
    # teste a comprimento
    print("teste a comprimento")
    v7 = Vetor3D(3.0, 0.0, 4.0)
    cv7 = v7.comprimento()
    print("v7 = " + str(v7))
    print("comprimento de v7 = " + str(cv7)
)

    print()
    # teste a versor
    print("teste a versor")
    vv7 = v7.versor()
    cvv7 = vv7.comprimento()
    print("vv7 = " + str(vv7))
    print("comprimento de vv7 = " + str(cvv7)
)

    print()
    # teste a interno
    print("teste a interno")
    print("v1 = " + str(v1))
    print("v7 = " + str(v7))
    iv1v7 = v1.interno(v7)
    print("v1 interno v7 = " + str(iv1v7))
    
    print()
    # teste a externo
    print("teste a externo")
    e = v1.externo(v7)
    print("e = v1 externo v7 = " + str(e))
    print("v1 interno e = " + str(v1.interno(e)))
    print("v7 interno e = " + str(v7.interno(e)))

    
