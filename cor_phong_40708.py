from cor_rgb_40708  import CorRGB
from imagem_40708 import Imagem
from vetor_40708      import Vetor3D
from luz_40708           import LuzPontual
from ponto_40708      import Ponto3D

class CorPhong:

    def __init__(self, k_ambiente, k_difusa, k_especular, brilho):

        self.k_ambiente = k_ambiente
        self.k_difusa = k_difusa
        self.k_especular = k_especular
        self.brilho = brilho


    def __repr__(self):

        return "CorPhong(" + str(self.k_ambiente) +", " + \
               str(self.k_difusa) + ", " + str(self.k_especular) + \
               ", " + str(self.brilho) + ")"


    def get_cor_rgb(self, luz, direcao_luz, normal, direcao_olho, sombra):


        cor_ambiente = self.k_ambiente * luz.get_intensidade_ambiente()
        if sombra == True:
            return cor_ambiente

        interno_l_n = direcao_luz.interno(normal)
        if interno_l_n < 0.0:
            return cor_ambiente


        cor_difusa = self.k_difusa * luz.get_intensidade_difusa() \
                     * interno_l_n
        # foi feita a funçao que opera vetor * float, não ao contrário
        proj = normal * interno_l_n
        r = (direcao_luz * (-1.0)) + (proj * 2.0)
        interno_r_direcao_olho = r.interno(direcao_olho)


        cor_especular = self.k_especular * luz.get_intensidade_especular() \
                     * (interno_r_direcao_olho)**self.brilho


        cor = cor_ambiente + cor_difusa + cor_especular
        
        return cor
    

if __name__ == "__main__":

    # teste ao construtor
    print("teste ao construtor")
    material_k_ambiente = CorRGB(0.0, 0.0, 0.1)
    material_k_difusa = CorRGB(0.0, 0.0, 0.9)
    material_k_especular = CorRGB(1.0, 1.0, 1.0)
    material_brilho = 100.0
    material_cor = CorPhong(material_k_ambiente, material_k_difusa, \
                            material_k_especular, material_brilho)


    # teste a __repr__
    print("teste a __repr__")
    print(material_cor)

    # teste a get_cor_rgb
    print("teste a get_cor_rgb")
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_intensidade_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_intensidade_ambiente, \
                     luz_intensidade_difusa, luz_intensidade_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    n_pontos = 100
    imagem = Imagem(100, 100)
    incremento = 0.02 # 2.0/100.0
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(100): # índice de linhas
        for n in range(100): # índice de colunas
            ponto = Ponto3D(-1.0 + n*incremento, 1.0 - m*incremento, 0)
            #print("\nponto: " + str(ponto))
            direcao_luz = (luz.get_posicao() - ponto).versor()
            #print("\ndirecao_luz: " + str(direcao_luz))
            direcao_olho = (olho - ponto).versor()
            #print("\ndirecao_olho: " + str(direcao_olho))
            cor = material_cor.get_cor_rgb(luz, direcao_luz, normal, \
                                           direcao_olho, sombra)
            #print("\ndcor: " + str(cor))
            imagem.set_cor(m+1, n+1, cor)
            #print()
            
    imagem.guardar_como_ppm("cor_phong.ppm")

