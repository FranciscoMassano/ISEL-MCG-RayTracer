from ponto_40708 import Ponto3D
from vetor_40708 import Vetor3D
from matriz_40708 import Matriz


""" Resolucao vai ser 2.0 x 2.0, 5 pixeis para o y e x, logo um total de 25"""

class Camara:

    def __init__(self, posicao, olhar_para, vertical,
                 distancia_olho_plano_projecao, largura_retangulo_projecao,
                 altura_retangulo_projecao, resolucao_horizontal,
                 resolucao_vertical):

        self.posicao = posicao
        self.olhar_para = olhar_para
        self.vertical = vertical
        self.distancia_olho_plano_projecao = distancia_olho_plano_projecao
        self.largura_retangulo_projecao = largura_retangulo_projecao
        self.altura_retangulo_projecao = altura_retangulo_projecao
        self.resolucao_horizontal = resolucao_horizontal
        self.resolucao_vertical = resolucao_vertical

        eixo_z = (olhar_para - posicao).versor()
        eixo_y = (vertical + eixo_z * (-1.0 * vertical.interno(eixo_z))).versor()
        eixo_x = eixo_z.externo(eixo_y)

        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.eixo_z = eixo_z

        incremento_horizontal = largura_retangulo_projecao/ resolucao_horizontal
        incremento_vertical = altura_retangulo_projecao / resolucao_vertical

        self.incremento_horizontal = incremento_horizontal
        self.incremento_vertical = incremento_vertical

        canto_superior_esquerdo_x = - largura_retangulo_projecao / 2.0 + \
                                    incremento_horizontal / 2.0

        canto_superior_esquerdo_y = altura_retangulo_projecao / 2.0 - \
                                    incremento_vertical / 2.0
        canto_superior_esquerdo_z = distancia_olho_plano_projecao


        self.canto_superior_esquerdo_x = canto_superior_esquerdo_x
        self.canto_superior_esquerdo_y = canto_superior_esquerdo_y
        self.canto_superior_esquerdo_z = canto_superior_esquerdo_z

        matriz = Matriz(4,4)

        matriz.set_coluna(1, [eixo_x.get_x(), eixo_x.get_y(), eixo_x.get_z(), 0.0])
        matriz.set_coluna(2, [eixo_y.get_x(), eixo_y.get_y(), eixo_y.get_z(), 0.0])
        matriz.set_coluna(3, [eixo_z.get_x(), eixo_z.get_y(), eixo_z.get_z(), 0.0])
        matriz.set_coluna(4, [posicao.get_x(), posicao.get_y(), \
                              posicao.get_z(), 1.0])

        self.matriz = matriz

    def __repr__(self):

        return "Camara(" \
                 + str(self.posicao) + ", \n" \
                 + str(self.olhar_para) + ", \n" \
                 + str(self.vertical) + ", \n" \
                 + str(self.distancia_olho_plano_projecao) + ", \n" \
                 + str(self.largura_retangulo_projecao) + ", \n" \
                 + str(self.altura_retangulo_projecao) + ", \n" \
                 + str(self.resolucao_horizontal) + ", \n" \
                 + str(self.resolucao_vertical) + ", \n" \
                 + str(self.eixo_x) + ", \n" \
                 + str(self.eixo_y) + ", \n" \
                 + str(self.eixo_z) + ", \n" \
                 + str(self.incremento_horizontal) + ", \n" \
                 + str(self.incremento_vertical) + ", \n" \
                 + str(self.canto_superior_esquerdo_x) + ", \n" \
                 + str(self.canto_superior_esquerdo_y) + ", \n" \
                 + str(self.canto_superior_esquerdo_z) + ", \n" \
                 + str(self.matriz) + ", \n" \
                 + ")"
                 

    def get_posicao(self):
        
        return self.posicao

    def get_resolucao_horizontal(self):
        
        return self.resolucao_horizontal
    
    def get_resolucao_vertical(self):
        
        return self.resolucao_vertical
    
    def get_pixel_local(self, linha, coluna):

        pixel_x = self.canto_superior_esquerdo_x + \
                  (coluna - 1) * self.incremento_horizontal
        pixel_y = self.canto_superior_esquerdo_y - \
                  (linha - 1) * self.incremento_vertical
        pixel_z = self.canto_superior_esquerdo_z

        return Ponto3D(pixel_x, pixel_y, pixel_z)
               

    def local_para_global(self, ponto):

        mponto = Matriz(4,1)
        mponto.set_coluna(1, [ponto.get_x(), ponto.get_y(), ponto.get_z(), 1.0])

        mresultado = self.matriz * mponto

        # coordenadas do ponto no referencial do mundo (global)
        x = mresultado.get_entrada(1, 1)
        y = mresultado.get_entrada(2, 1)
        z = mresultado.get_entrada(3, 1)

        resultado = Ponto3D(x, y ,z)

        return resultado

    def get_pixel_global(self, linha, coluna):

        pixel_local = self.get_pixel_local(linha, coluna)
        pixel_global = self.local_para_global(pixel_local)

        return pixel_global



##TESTES
if __name__ == "__main__":

    # teste ao construtor
    print("\nteste ao construtor")
    posicao = Ponto3D(0.0, 0.0, 3.0)
    olhar_para = Ponto3D(0.0, 0.0, 0.0)
    vertical = Vetor3D(0.0, 1.0, 0.0)
    distancia_olho_plano_projecao = 2.0
    largura_retangulo_projecao = 2.0
    altura_retangulo_projecao = 2.0
    resolucao_horizontal = 5
    resolucao_vertical = 5
    camara = Camara(posicao, olhar_para, vertical, distancia_olho_plano_projecao,
    largura_retangulo_projecao, altura_retangulo_projecao,
    resolucao_horizontal, resolucao_vertical)


    #teste a __repr__
    print("\nteste a __repr__")
    print(camara)


    # teste a get_posicao
    print("\nteste a get_posicao")
    print(camara.get_posicao())

    
    # teste a get_resolucao_horizontal
    print("\nget_resolucao_horizontal")
    print(camara.get_resolucao_horizontal())

    
    # teste a get_resolucao_vertical
    print("\nteste a get_resolucao_vertical")
    print(camara.get_resolucao_vertical())


    # teste a get_pixel_local
    print("\nteste a get_pixel_local")
    print("sistema de coordenadas LOCAL")
    print("canto superior esquerdo = ")
    p1 = camara.get_pixel_local(1, 1)
    print(p1)
    print("canto superior direito = ")
    p2 = camara.get_pixel_local(1, 5)
    print(p2)
    print("canto inferior esquerdo = ")
    p3 = camara.get_pixel_local(5, 1)
    print(p3)
    print("canto inferioror direito = ")
    p4 = camara.get_pixel_local(5, 5)
    print(p4)


    # teste a local_para_global
    print("\nteste a local_para_global")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p1_global = camara.local_para_global(p1)
    print(p1_global)
    print("canto superior direito = ")
    p2_global = camara.local_para_global(p2)
    print(p2_global)
    print("canto inferior esquerdo = ")
    p3_global = camara.local_para_global(p3)
    print(p3_global)
    print("canto inferioror direito = ")
    p4_global = camara.local_para_global(p4)
    print(p4_global)


    # teste a get_pixel_global
    print("\nteste a get_pixel_global")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p5 = camara.get_pixel_global(1, 1)
    print(p5)
    print("canto superior direito = ")
    p6 = camara.get_pixel_global(1, 5)
    print(p6)
    print("canto inferior esquerdo = ")
    p7 = camara.get_pixel_global(5, 1)
    print(p7)
    print("canto inferioror direito = ")
    p8 = camara.get_pixel_global(5, 5)
    print(p8)
        

        

        
        
