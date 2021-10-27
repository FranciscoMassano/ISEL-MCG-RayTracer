from ponto_40708 import Ponto3D
from cor_rgb_40708 import CorRGB
from cor_phong_40708 import CorPhong
from face_40708  import FaceTriangular
from luz_40708  import LuzPontual
from vetor_40708 import Vetor3D
from camara_40708 import Camara
from reta_40708 import Reta
from imagem_40708  import Imagem

class RayTracer:

    def __init__(self, lista_faces, lista_luzes, camara, cor_fundo):

        self.lista_faces = lista_faces
        self.lista_luzes = lista_luzes
        self.camara = camara
        self.cor_fundo = cor_fundo

    def __str__(self):

        lista1 = self.lista_faces
        lista2 = self.lista_luzes
        
        return('RayTracer(' + str(lista1) \
               + '\n, \n' + str(lista2)+ '\n, \n' \
               + str(camara)+ '\n, \n' \
               + str(cor_fundo) + '\n)')

    def renderiza(self):

        #variaveis linhas e colunas
        linhas = camara.resolucao_vertical
        colunas = camara.resolucao_horizontal

        imagem = Imagem(linhas, colunas) #imagem com resolucao igual a da camara

        for linha in range(linhas):
            # Print da linha a ser processada
            #print ('linha = ' + str(l+1) + ' de ' + str(linhas))

            for coluna in range(colunas):
                # Obter posicao camara
                posicao = camara.posicao
                # Obter posicao ponto no sistema de coordenadas global
                ponto = camara.get_pixel_global(linha, coluna)
                # Obter recta com origem na posicao da camara
                recta = Reta(posicao, ponto)
                # Obter a cor vista pelo raio de visao definido pela recta criada
                cor = ray_tracer.get_cor_vista_por_raio(recta)
                # Armazenar a cor na imagem criada inicialmente
                imagem.set_cor(linha, coluna, cor)

        return imagem

    def get_face_intercetada_mais_proxima(self, raio):

        # Lista para valores de t e lista para as faces intersetadas
        interseccao = True
        valores_t = []
        faces = []
        
        # Corre a lista de faces para encontrar a intersecao com cada face
        for b in range(len(lista_faces)):
            face_momentanea = lista_faces[b]
            caracteristicas = face_momentanea.interceta_triangulo(raio)
            interseccao = caracteristicas[0]
            ponto_interseccao = caracteristicas[1]
            t_momentaneo = caracteristicas[2]

            # Caso a reta raio intersete alguma das faces da cena preenche as
            # listas com a face e o t
            if(interseccao == True):
                valores_t.append(t_momentaneo)
                faces.append(face_momentanea)


        # Obtem o menor valor t
        if (len(valores_t) != 0):
            t_minimo = min(valores_t)


        # Se a lista de faces conter alguma face para cada uma o seu valor t
        if (len(faces) != 0):   
            for b in range(len(faces)):
                face_momentanea = faces[b]
                caracteristicas = face_momentanea.interceta_triangulo(raio)
                ponto_interseccao = caracteristicas[1]
                t_momentaneo = caracteristicas[2]

                # caso o parametro t seja igual ao t minimo retorna uma lista
                # com todos os valores
                if (t_minimo == t_momentaneo):
                    interseccao = True
                    ponto_intercecao = ponto_interseccao
                    t = t_momentaneo
                    face = face_momentanea

        # Se nao intercetar nenhuma face retorna [False, None, None, None]
        else:
            interseccao = False
            ponto_intercecao = None
            t = None
            face = None

        return ([interseccao, ponto_intercecao, t, face])
            
            
    def get_cor_face(self, face, ponto_intersecao, direcao_olho):

         black = CorRGB(0.0, 0.0, 0.0)
         for r in range(len(lista_luzes)):
            luz_momentanea = lista_luzes[r]
            recta1 = Reta(ponto_intercecao, luz_momentanea.posicao)
            direcao_luz = (luz_momentanea.posicao - ponto_intercecao).versor()

            # Pontos
            ponto1 = face.ponto1
            ponto2 = face.ponto2
            ponto3 = face.ponto3

            # Vectores            
            vector1 = ponto2 - ponto1
            vector2 = ponto3 - ponto1

            # Vector Normal
            normal = vector1.externo(vector2).versor()

            interseccao_face = ray_tracer.get_face_intercetada_mais_proxima(recta1)[0]

            # Condicao para verificar se a recta interseta alguma face caso nao

            # caso nao intersete obter cor Phong
            if (interseccao_face == False):
                sombra = False
                cor = face.cor_phong.get_cor_rgb(luz_momentanea, direcao_luz,
                                                      normal, direcao_olho, sombra)
                black = black.soma(cor)
                
            # caso intersete obter a cor Phong em sombra  
            else:
                sombra = True
                cor = face.cor_phong.get_cor_rgb(luz_momentanea, direcao_luz,
                                                      normal,  direcao_olho, sombra)

                black = black.soma(cor)

            return (black)

    def get_cor_vista_por_raio(self, raio):
         
         face_intercetada = ray_tracer.get_face_intercetada_mais_proxima(raio)
         interceta = face_intercetada[0]
         ponto_intercecao = face_intercetada[1]
         face = face_intercetada[3]

         if(interceta == False):
             cor_face = cor_fundo

        else:
            direcao_olho = (camara.posicao-ponto_intersecao.versor()
            cor_face = ray_tracer.get_cor_face(face, ponto_intercecao, direcao_olho)

        return(cor_face)
            
    
    

# testes
if __name__ == "__main__":
    # teste ao construtor
    vermelho = CorRGB(1.0, 0.0, 0.0)
    branco = CorRGB(1.0, 1.0, 1.0)
    preto = CorRGB(0.0, 0.0, 0.0)
    cinzento = CorRGB(0.25, 0.25, 0.25)
    brilho = 100.0
    cor_letras = CorPhong(vermelho*0.1, vermelho*0.5, vermelho*0.5, brilho)
    cor_chao = CorPhong(cinzento, cinzento, cinzento, brilho)
    
    # letra L - triângulo 1
    # prefixos l v
    # prefixo l: da letra L; prefixo v: de vértice
    l1_v1 = Ponto3D(-4.25, 0.0, 0.0)
    l1_v2 = Ponto3D(-3.25, 0.0, 0.0)
    l1_v3 = Ponto3D(-4.25, 3.0, 0.0)
    l1 = FaceTriangular(l1_v1, l1_v2, l1_v3, cor_letras)
    # letra L - triângulo 2
    l2_v1 = Ponto3D(-4.25, 0.0, 0.0)
    l2_v2 = Ponto3D(-2.25, 0.0, 0.0)
    l2_v3 = Ponto3D(-4.25, 1.5, 0.0)
    l2 = FaceTriangular(l2_v1, l2_v2, l2_v3, cor_letras)
    # letra E - triângulo 1
    e1_v1 = Ponto3D(-1.75, 1.0, 0.0)
    e1_v2 = Ponto3D(0.25, 3.0, 0.0)
    e1_v3 = Ponto3D(-1.75, 3.0, 0.0)
    e1 = FaceTriangular(e1_v1, e1_v2, e1_v3, cor_letras)
    # letra E - triângulo 2
    e2_v1 = Ponto3D(-1.75, 0.0, 0.0)
    e2_v2 = Ponto3D(0.25, 2.0, 0.0)
    e2_v3 = Ponto3D(-1.75, 2.0, 0.0)
    e2 = FaceTriangular(e2_v1, e2_v2, e2_v3, cor_letras)
    # letra E - triângulo 3
    e3_v1 = Ponto3D(-1.75, 0.0, 0.0)
    e3_v2 = Ponto3D(0.25, 0.0, 0.0)
    e3_v3 = Ponto3D(-1.75, 2.0, 0.0)
    e3 = FaceTriangular(e3_v1, e3_v2, e3_v3, cor_letras)
    # letra I - triângulo 1
    i1_v1 = Ponto3D(0.75, 0.0, 0.0)
    i1_v2 = Ponto3D(1.75, 0.0, 0.0)
    i1_v3 = Ponto3D(1.25, 3.0, 0.0)
    i1 = FaceTriangular(i1_v1, i1_v2, i1_v3, cor_letras)
    # letra M - triângulo 1
    m1_v1 = Ponto3D(2.25, 0.0, 0.0)
    m1_v2 = Ponto3D(3.25, 0.0, 0.0)
    m1_v3 = Ponto3D(3.25, 3.0, 0.0)
    m1 = FaceTriangular(m1_v1, m1_v2, m1_v3, cor_letras)
    # letra M - triângulo 2
    m2_v1 = Ponto3D(3.75, 1.0, 0.0)
    m2_v2 = Ponto3D(4.25, 3.0, 0.0)
    m2_v3 = Ponto3D(3.25, 3.0, 0.0)
    m2 = FaceTriangular(m2_v1, m2_v2, m2_v3, cor_letras)
    # letra M - triângulo 1
    m3_v1 = Ponto3D(4.25, 0.0, 0.0)
    m3_v2 = Ponto3D(5.25, 0.0, 0.0)
    m3_v3 = Ponto3D(4.25, 3.0, 0.0)
    m3 = FaceTriangular(m3_v1, m3_v2, m3_v3, cor_letras)

    # parede de fundo
    fundo_v1 = Ponto3D(-10.0, -2.0, -2.0)
    fundo_v2 = Ponto3D(10.0, -2.0, -2.0)
    fundo_v3 = Ponto3D(-10.0, 6.0, -2.0)
    fundo = FaceTriangular(fundo_v1, fundo_v2, fundo_v3, cor_chao)

    # chão
    chao_v1 = Ponto3D(-12.0, -2.0, 0.0)
    chao_v2 = Ponto3D(12.0, -2.0, 0.0)
    chao_v3 = Ponto3D(0.0, -2.0, 1.0*10**4)
    chao = FaceTriangular(chao_v1, chao_v2, chao_v3, cor_chao)

    lista_faces = [l1, l2, e1, e2, e3, i1, m1, m2, m3, fundo, chao]
    # lista de luzes
    luz1_posicao = Ponto3D(-5.0, 4.0, 5.0)
    luz2_posicao = Ponto3D( 5.0, 4.0, 5.0)
    luz1 = LuzPontual(luz1_posicao, branco, branco, branco)
    luz2 = LuzPontual(luz2_posicao, branco, branco, branco)
    lista_luzes = [luz1, luz2]

    # a câmara
    camara_posicao = Ponto3D(0.0, 0.0, 10.0)
    camara_olhar_para = Ponto3D(0.0, 0.0, 0.0)
    camara_vertical = Vetor3D(0.0, 1.0, 0.0)
    camara_distancia_olho_plano_projecao = 5.0
    camara_largura_retangulo_projecao = 10.0
    camara_altura_retangulo_projecao = 8.0
    camara_resolucao_horizontal = 300
    camara_resolucao_vertical = 240
    # usar resoluções mais baixas para testes (para ser mais rápido)
    # por exemplo 30x24
    #camara_resolucao_horizontal = 30
    #camara_resolucao_vertical = 24
    
    camara = Camara(camara_posicao, camara_olhar_para, camara_vertical, camara_distancia_olho_plano_projecao, camara_largura_retangulo_projecao, camara_altura_retangulo_projecao, camara_resolucao_horizontal, camara_resolucao_vertical)
    cor_fundo = preto
    ray_tracer = RayTracer(lista_faces, lista_luzes, camara, cor_fundo)



    # teste a __repr__
    print(ray_tracer)

    # teste a renderiza
    imagem = ray_tracer.renderiza()
    imagem.guardar_como_ppm("projeto_imagem1.ppm")


    
























    

