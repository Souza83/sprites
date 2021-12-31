import pygame  # Importa a biblioteca
from pygame.locals import *  # Importa tudo do módulo locals
from sys import exit  # Importa função para fechar o jogo

pygame.init()  # Inicia método pygame

largura = 640  # Define largura para tela
altura = 480  # Define altura para tela
preto = (0, 0, 0)  # Define cor preto, podendo ser usado no jogo, inclusive para tela

tela = pygame.display.set_mode((largura, altura)) #  Cria tela do jogo
pygame.display.set_caption("Sprites")  #  Nome tela

class Sapo(pygame.sprite.Sprite):  # Cria classe chamada sapo que herda atributos e métodos da classe sprite de pygame
    def __init__(self):  # Cria método construtor
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe
        self.sprites = []  # Cria lista
        self.sprites.append(pygame.image.load('sprites/attack_1.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_2.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_3.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_4.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_5.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_6.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_7.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_8.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_9.png'))  # Adiciona na lista a imagem (sprite)
        self.sprites.append(pygame.image.load('sprites/attack_10.png'))  # Adiciona na lista a imagem (sprite)
        self.atual = 0  # Define posição da imagem atual
        self.image = self.sprites[self.atual]  # Define a imagem, que contêm a sprite atual
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))  # Tranforma a escala da imagem em 3 x.

        self.rect = self.image.get_rect()  # O 'rect' pega o retangulo onde fica a imagem na tela
        self.rect.topleft = 100, 100  #  Define a posição que será exibido a imagem contida no retângulo.

        self.animar = False  # Atributo da classe Sapo que começa com valor falso

    def atacar(self):  # Método atacar
        self.animar = True  # Altera variável para verdadeiro

    def update(self):  # Cria animação das sprites
        if self.animar == True:  # Se animar for verdadeiro executa abaixo
            self.atual = self.atual + 0.35  # A variável receberá a posição + valor (ajuda controlar velocidade das sprites)
            if self.atual >= len(self.sprites):  # Se posição atual for maior que tamnho da quantidade de sprites
                self.atual = 0  # Se condição verdadeira, variável recebe 07
                self.animar = False  # Variável animar recebe falso após execução das sprites
            self.image = self.sprites[int(self.atual)]#  Cria o indice das sprites
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))  # Tranforma a escala da imagem em 3 x.

todas_as_sprites = pygame.sprite.Group()  # Cria um objeto que recebe um grupo para armazenar sprites que serão instanciadas
sapo = Sapo()  # Cria um objeto a partir da classe Sapo para desenha sapo na tela
todas_as_sprites.add(sapo)  # Adiciona o sapo no grupo todas_as_sprites

relogio = pygame.time.Clock()  # Define o tempo para controlar taxa de frame do jogo

while True:  #  Cria o loop principal, onde fica todas as ações do jogo
    relogio.tick(30)  # Define taxa de frame do jogo
    tela.fill(preto)  # Pinta tela toda de preto
    for event in pygame.event.get(): #  Cria loop dos eventos capturados
        if event.type == QUIT:  # Se o tipo do evento for sair
            pygame.quit()  #  Chama a função para sair do pygame
            exit()  # Executa função para fechar janela
        if event.type == KEYDOWN:  # Se precionar qualquer tecla do teclado
            sapo.atacar()  #  Chama um método do objeto sapo (definido como atacar)
    todas_as_sprites.draw(tela)  # Desenha o objeto sapo na tela
    todas_as_sprites.update()  # Faz o update das sprites
    pygame.display.flip()  # Atualiza a tela
