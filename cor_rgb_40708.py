from colorsys import hsv_to_rgb

class CorRGB:

    def __init__ (self, red, green, blue):
        
        self.r = min(1.0, max(0.0, red))
        self.g = min(1.0, max(0.0, green))
        self.b = min(1.0, max(0.0, blue))

    def __repr__ (self):
        
        rInt = int(self.r * 255.0)
        gInt = int(self.g * 255.0)
        bInt = int(self.b * 255.0)

        resultado = str(rInt) + " " + str(gInt) + " " + str(bInt)
        return resultado

    def soma (self, outra_cor):

        novo_r = self.r + outra_cor.r
        novo_g = self.g + outra_cor.g
        novo_b = self.b + outra_cor.b

        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor

    def __add__ (self, outra_cor):
        
        return self.soma(outra_cor)

    def set_hsv(self, hue, saturation, value):

        (r, g, b) = hsv_to_rgb(hue / 360.0, saturation, value)

        self.r   = r
        self.g = g
        self.b  = b

        return self

    def multiplica(self, outra_cor):
        
        novo_r = self.r * outra_cor.r
        novo_g = self.g * outra_cor.g
        novo_b = self.b * outra_cor.b

        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor

    def multiplica_escalar(self, escalar):
        """
        Docstring
        """

        novo_r = self.r * escalar
        novo_g = self.g * escalar
        novo_b = self.b * escalar

        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor

    def __mul__(self, valor):
        if isinstance(valor, float):
            return self.multiplica_escalar(valor)
        else:
            return self.multiplica(valor)
    


###TESTES#######
    
# testes ao construtor
print("testes ao construtor")
print()
c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
c2 = CorRGB(0.0, 1.0, 0.0) # verde
c3 = CorRGB(0.0, 0.0, 1.0) # azul
c4 = CorRGB(1.0, 1.0, 1.0) # branco
c5 = CorRGB(0.0, 0.0, 0.0) # preto
print()



if __name__ == "__main__":
    # testes ao método __repr__
    print("testes ao repr")
    print()
    c1 = CorRGB(1.0, 0.0, 0.0)
    print(c1)
    print("c1 = " + str(c1))
    print()
    # mais testes ao construtor
    print("mais testes ao construtor")
    print()
    c2 = CorRGB(-0.1, 0.1, 1.1)
    print(c2)
    print()
    # mais testes ao método __repr__
    print("mais testes ao repr")
    print()
    lista = [c1, c2]
    print(lista)
    print()

    # testes ao método soma
    print("testes ao soma")
    print()
    c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
    c2 = CorRGB(0.0, 1.0, 0.0) # verde
    c3 = CorRGB(1.0, 1.0, 1.0) # branco
    c4 = c1.soma(c2)
    c5 = c1.soma(c3)
    print(c4)
    print(c5)
    print()

    # testes ao operador +
    print("testes ao add")
    print()
    c1 = CorRGB(1.0, 0.0, 0.0) # vermelho
    c2 = CorRGB(0.0, 1.0, 0.0) # verde
    c3 = CorRGB(1.0, 1.0, 1.0) # branco
    c4 = c1 + c2
    c5 = c1 + c3
    print(c4)
    print(c5)
    print()


    # testes ao método set_hsv
    print("testes ao set_hsv")
    print()
    c1 = CorRGB(0.0, 0.0, 0.0)
    c1.set_hsv(360.0, 1.0, 1.0)
    print(c1)
    print()

    # testes ao método multiplica
    print("testes ao multiplica")
    print()
    c1 = CorRGB(1.0, 0.0, 0.0)
    c2 = CorRGB(1.0, 1.0, 1.0)
    c3 = CorRGB(0.0, 0.0, 0.0)
    c4 = c1.multiplica(c2)
    c5 = c1.multiplica(c3)
    print(c4)
    print(c5)
    print()

    # testes ao método multiplica_escalar
    print("testes ao muktiplica escalar")
    print()
    c1 = CorRGB(1.0, 1.0, 1.0)
    e1 = 0.0
    e2 = 0.5
    e3 = 1.0
    e4 = 2.0
    c2 = c1.multiplica_escalar(e1)
    c3 = c1.multiplica_escalar(e2)
    c4 = c1.multiplica_escalar(e3)
    c5 = c1.multiplica_escalar(e4)
    print(c2)
    print(c3)
    print(c4)
    print(c5)
    print()

    # testes ao operador * (mul)
    print("testes ao mul")
    print()
    c1 = CorRGB(1.0, 1.0, 1.0)
    c2 = CorRGB(0.0, 0.5, 1.0)
    e1 = 0.5
    c3 = c1 * c2# segundo operando do tipo CorRGB
    c4 = c1 * e1# segundo operando do tipo float (um escalar)
    print(c3)
    print(c4)
    print()


