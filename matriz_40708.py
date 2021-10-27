class Matriz:

    def __init__(self, numero_linhas, numero_colunas):

        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        
        self.linhas = []

        for linha in range(numero_linhas):
            nova_linha = []
            for coluna in range(numero_colunas):
                nova_linha.append(0.0)
            self.linhas.append(nova_linha)
                
                
    def __repr__(self):
        resultado = "Matriz(" + str(self.numero_linhas) + ", " + str(self.numero_colunas) + ")\n"

        for linha in range(self.numero_linhas):
            for coluna in range(self.numero_colunas):
                resultado = resultado + str(self.linhas[linha][coluna]) + " "
            resultado = resultado  + "\n"

        return resultado


    def set_entrada(self, linha, coluna, valor):

        self.linhas[linha - 1][coluna - 1] = valor


    def get_entrada(self, linha, coluna):

        return self.linhas[linha - 1][coluna - 1]


    def adiciona(self, outra_matriz):

        resultado = Matriz(self.numero_linhas, self.numero_colunas)

        for linha in range(self.numero_linhas):
            for coluna in range(self.numero_colunas):
                soma = self.linhas[linha][coluna] + \
                       outra_matriz.linhas[linha][coluna]
                resultado.linhas[linha][coluna] = soma
                
        return resultado

    def __add__(self, outra_matriz):
        
        return self.adiciona(outra_matriz)

    def multiplica(self, outra_matriz):
        
        nlinhas = self.numero_linhas
        ncolunas = outra_matriz.numero_colunas
        resultado = Matriz(nlinhas, ncolunas)

        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                soma = 0.0
                for i in range(self.numero_colunas):
                     soma = soma + self.linhas[linha][i] \
                            * outra_matriz.linhas[i][coluna]
                resultado.linhas[linha][coluna] = soma
        
        return resultado

    def multiplica_escalar(self, escalar):

        nlinhas = self.numero_linhas
        ncolunas = self.numero_colunas
        resultado = Matriz(nlinhas, ncolunas)

        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                entrada = escalar * self.linhas[linha][coluna]
                resultado.linhas[linha][coluna] = entrada
        
        return resultado

    def __mul__(self, valor):
        
        if isinstance(valor, Matriz):
            return self.multiplica(valor)
        else:
            return self.multiplica_escalar(valor)

        
    def det_2x2(self):

        # A = [a b]
        #         [c d]
        #det(A) = a*d - c*b
        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[1][0]
        d = self.linhas[1][1]
        
        return a*d - c*b

    def det_3x3(self):

        # A = [a b c] a b
        #         [d e f] d e
        #         [g h i] g h
        #det(A) = a*e*i + b*f*a + c*d*h - g*e*c - h*f*a - i*d*b
        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[0][2]
        d = self.linhas[1][0]
        e = self.linhas[1][1]
        f = self.linhas[1][2]
        g = self.linhas[2][0]
        h = self.linhas[2][1]
        i = self.linhas[2][2]
        
        return a*e*i + b*f*g + c*d*h - g*e*c - h*f*a - i*d*b

    def sub_matriz(self, linha_a_remover, coluna_a_remover):

        nlinhas = self.numero_linhas - 1
        ncolunas = self.numero_colunas - 1
        resultado = Matriz(nlinhas, ncolunas)

        linha_a_remover = linha_a_remover - 1
        coluna_a_remover = coluna_a_remover - 1

        # percorrer as entradas da matriz resultado
        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                indice_linha= linha
                indice_coluna= coluna
                
                if linha >= linha_a_remover:
                    indice_linha = indice_linha + 1
                if coluna >= coluna_a_remover:
                    indice_coluna = indice_coluna + 1
                resultado.linhas[linha][coluna] = self.linhas[indice_linha][indice_coluna]
        return resultado

    def det(self):

        if self.numero_linhas == 1:
            return self.linhas[0][0]
        elif self.numero_linhas == 2:
            return self.det_2x2()
        elif self.numero_linhas == 3:
            return self.det_3x3()
        else:
            resultado = 0.0
            for i in range(self.numero_linhas):
                resultado = resultado + ((-1.0)**(1+(i+1)))*self.linhas[0][i] * self.sub_matriz(1, i+1).det()
            return resultado
        

    def transposta(self):

        nlinhas = self.numero_linhas 
        ncolunas = self.numero_colunas 
        resultado = Matriz(ncolunas, nlinhas)

        for coluna in range(ncolunas):
            for linha in range(nlinhas):
                resultado.linhas[coluna][linha] = self.linhas[linha][coluna]
                
        return resultado

    def copia(self):

        nlinhas = self.numero_linhas
        ncolunas = self.numero_colunas
        resultado = Matriz(nlinhas, ncolunas)

        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                resultado.linhas[linha][coluna] = self.linhas[linha][coluna]

        return resultado 

    def set_linha(self, linha, uma_lista):

        for lista in range(self.numero_colunas):
            self.linhas[linha - 1][lista] = uma_lista[lista]


    def set_coluna(self, coluna, uma_lista):

        for lista in range(self.numero_linhas):
            self.linhas[lista][coluna - 1] = uma_lista[lista]

# o exemplo adicional verifica os metodos feitos por nós

if __name__ == "__main__":
    print()
    # teste ao construtor
    print("teste ao construtor")
    m1 = Matriz(3, 4)


    print()
    # teste a __repr__
    print("teste a __repr__")
    print(m1)


    print()
    # teste a set_entrada
    print("teste a set_entrada")
    m1.set_entrada(1, 2, 1.0)
    m1.set_entrada(2, 2, 2.0)
    m1.set_entrada(3, 2, 3.0)
    print(m1)

    print()
    # teste a get_entrada
    print("teste a get_entrada")
    print("m1 entrada (3,1) = " + str(m1.get_entrada(3, 1)))
    print("m1 entrada (3,2) = " + str(m1.get_entrada(3, 2)))


    print()
    # teste a adiciona
    print("--> teste a adiciona")
    m2 = m1.adiciona(m1)
    print(m2)

    print()
    # teste a + (__add__) --> usar o operador '+' ao invés de '.adiciona()'
    print("teste a + (__add__)")
    m3 = m1 + m1
    print(m3)

    print()
    # teste a multiplica
    print("teste a multiplica")
    m4 = Matriz(4, 3)
    m4.set_entrada(2, 1, 1.0)
    m4.set_entrada(2, 2, 2.0)
    m4.set_entrada(2, 3, 3.0)

    print(m1)
    print(m4)
    
    m5 = m1.multiplica(m4)
    print(m5)
    

    print()
    # teste a multiplica_escalar
    print("teste a multiplica_escalar")
    m5a = m5.multiplica_escalar(-1.0)
    print(m5a)


    print()
    # teste a *
    print("teste a * (__mul__)")
    m6 = m1 * m4
    print(m6)
    m6a = m1 * 2.0
    print(m6a)

    # m7 = 2.0 * m1 dá erro

    print()
    # teste a det_2x2
    print("teste a det_2x2")
    m7 = Matriz(2, 2)
    m7.set_entrada(1, 1, 1.0)
    m7.set_entrada(1, 2, 2.0)
    m7.set_entrada(2, 1, 3.0)
    m7.set_entrada(2, 2, 4.0)
    print(m7)
    print("det(m7) = " + str(m7.det_2x2()))


    print()
    # teste a det_3x3
    print("Teste a det_3x3")
    print(m6)
    print("det(m6) = " + str(m6.det_3x3()))


    print()
    # teste a sub_matriz
    print("este a sub_matriz")
    m8 = m6.sub_matriz(2, 2)
    print(m8)


    print()
    # testes a det
    print("testes a det")
    print(m7.det())
    print(m6.det())
    m9 = Matriz(5, 5)
    m9.set_entrada(1, 1, 2.0)
    m9.set_entrada(2, 2, 2.0)
    m9.set_entrada(3, 3, 2.0)
    m9.set_entrada(4, 4, 2.0)
    m9.set_entrada(5, 5, 2.0)
    print(m9)
    print("det = " + str(m9.det()))

    print()
    # teste a transposta
    print("teste a transposta")
    print(m1)
    print()
    m1t = m1.transposta()
    print(m1t)

    print()
    # testes a copia
    print("teste a copia")
    m10 = m8.copia()
    m10.set_entrada(1, 1, -2.0)
    print(m8)
    print(m10)


    print()
    # teste a set_linha
    print("teste a set_linha")
    m9.set_linha(5, [1.0, 2.0, 3.0, 4.0, 5.0])
    print(m9)


    print()
    # teste a set_coluna
    print("teste a set_coluna")
    m9.set_coluna(3, [10.0, 20.0, 30.0, 40.0, 50.0])
    print(m9)

