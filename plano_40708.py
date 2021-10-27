from ponto_40708  import Ponto3D
from matriz_40708 import Matriz
from reta_40708   import Reta

TOLERANCIA_ZERO = 10.0**(-10)

class ErroPontosColineares(Exception):
    """Excepcao lancada com erro quando os pontos sao colineares"""


class Plano:
    """classe que representa o plano"""

    def __init__(self, ponto1, ponto2, ponto3):
        """cira um plano definido por tres pontos"""

        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        v12 = ponto2 - ponto1
        v13 = ponto3 - ponto1


        normal = v12.externo(v13)

        if normal.comprimento() < TOLERANCIA_ZERO:
            raise ErroPontosColineares

        self.normal = normal.versor()

    def __repr__(self):

        return "Plano(" + str(self.ponto1) + ", " + str(self.ponto2) + ", " \
               + str(self.ponto3) + ", " + str(self.normal) + ")"

    def interceta_triangulo(self, reta):

        ax = self.ponto1.x
        ay = self.ponto1.y
        az = self.ponto1.z

        bx = self.ponto2.x
        by = self.ponto2.y
        bz = self.ponto2.z

        cx = self.ponto3.x
        cy = self.ponto3.y
        cz = self.ponto3.z

        px = reta.origem.x
        py = reta.origem.x
        pz = reta.origem.x
        
        vx = reta.vetor_diretor.x
        vy = reta.vetor_diretor.x
        vz = reta.vetor_diretor.x

        M = Matriz(3, 3)
        M.set_linha(1, [ax - bx, ax - cx, vx])
        M.set_linha(2, [ay - by, ay - cy, vy])
        M.set_linha(3, [az - bz, az - cz, vz])

        detM = M.det()

        if abs(detM) < TOLERANCIA_ZERO:

            return [False, None, None]

        # Incógnita t - terceira

        M3 = M.copia()
        M3.set_coluna(3, [ax - px, ay - py, az - pz])

        t = M3.det() / detM

        if t < TOLERANCIA_ZERO:

            return [False, None, None]
        # Incógnita tB - primeira
        
        M1 = M.copia()
        M1.set_coluna(1, [ax - px, ay - py, az - pz])

        tB = M1.det() / detM

        if tB < 0.0 or tB > 1.0:

            return [False, None, None]
        
        # Incógnita tC - segunda
        
        M2 = M.copia()
        M2.set_coluna(2, [ax - px, ay - py, az - pz])

        tC = M2.det() / detM

        if tC < 0.0 or tC > 1.0:

            return [False, None, None]

        tA = 1.0 - tB - tC

        if tA < 0.0 or tA > 1.0:

            return [False, None, None]

        #ponto de interseção
        
        A = self.ponto1
        B = self.ponto2
        C = self.ponto3
        
        ponto_intersecao = A + (B - A) * tB + (C - A) * tC

        return [True, ponto_intersecao, t]
        


if __name__ == "__main__":

    print("\nteste ao construtor")
    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(2.0, 0.0, 0.0)
    c = Ponto3D(0.0, 2.0, 0.0)
    plano1 = Plano(a, b, c)
    print("Até aqui não foram lançadas exceções.")
    # teste a TOLERANCIA_ZERO
    print("TOLERANCIA_ZERO = " + str(TOLERANCIA_ZERO))
    # teste à exceção ErroPontosColineares
    try:
        plano2 = Plano(a, b, b)
    except ErroPontosColineares:
        print("Ao tentar definir-se o plano plano2 = Plano(a, b, b)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("A execução foi interrompida. plano2 não ficou definida.")


    print("\nteste a __repr__")
    # teste a __repr__
    # a normal tem que apontar no sentido do eixo dos z’s
    # e tem que ter comprimento 1
    print(plano1)


    print("\nteste a interseta_triangulo")
    # testes a interceta_triangulo
    p1 = Ponto3D(1.0, 1.0, 10.0)
    p2 = Ponto3D(1.0, 1.0, 5.0)
    r1 = Reta(p1, p2)
    trio = plano1.interceta_triangulo(r1)
    if trio[0] == True:
        print("r1 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
        print("interceção calculada com a equação da reta e t.")
        print("(tem que dar o mesmo que trio[1])")
        t = trio[2]
        #pi = r1.get_origem() + (r1.get_vetor_diretor() * t)
        pi = r1.origem + (r1.vetor_diretor * t)
        print(pi)
    else:
        print("r1 NÃO interceta plano1.")
    p3 = Ponto3D(2.0, 2.0, 10.0)
    r2 = Reta(p1, p3)
    trio = plano1.interceta_triangulo(r2)
    if trio[0] == True:
        print("r2 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
    else:
        print("r2 NÃO interceta plano1.")        

        
        
        
        
        
        
        

        

        

        
        

        

    
