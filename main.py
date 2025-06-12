
import pygame
import tkinter as tk

pygame.init()

fundoJogo = pygame.image.load("imagens/fundoJogo.jpg")
nave = pygame.image.load("imagens/nave.png")
icone = pygame.image.load("imagens/icone.png")
asteroide = pygame.image.load("imagens/asteroide.png")
pygame.display.set_caption("Space Looker")
relogio = pygame.time.Clock()
pygame.display.set_icon(icone)
Tela = (1000, 700)
tamanhoTela = pygame.display.set_mode((1000, 700))
preto = (0,0,0)
branco = (255, 255, 255)
posicaoXNave = 40
posicaoYNave = 350
movimentoXNave = 0
movimentoYNave = 0
pausado = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE :
            pausado = not pausado
        elif not pausado:
            if evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                movimentoYNave = 20
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoYNave = 20
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                movimentoYNave = -20
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYNave = -20
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXNave = 20
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXNave = 20
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXNave = -20
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXNave = -20
            

        if posicaoXNave <= 20:
            posicaoXNave = 20
        elif posicaoXNave >= 855:
            posicaoXNave = 855

        if posicaoYNave <= 0:
            posicaoYNave = 0
        elif posicaoYNave >= 580:
            posicaoYNave = 580

        if not pausado:
            posicaoXNave = posicaoXNave + movimentoXNave
            posicaoYNave = posicaoYNave + movimentoYNave

    tamanhoTela.blit(fundoJogo, (-120,10))
    tamanhoTela.blit(nave, (posicaoXNave, posicaoYNave))

    if pausado:
        fonte = pygame.font.Font(None, 74)
        fonte2 = pygame.font.Font(None, 50)
        tamanhoTela.fill(preto)
        texto = fonte.render("PAUSE", True, (255, 0, 0))
        texto2 = fonte2.render("Pressione espaço para retomar", True, (255, 0, 0))
        tamanhoTela.blit(texto, (350, 250))
        tamanhoTela.blit(texto2, (220, 320))

    pygame.display.update()
    relogio.tick(60)  






