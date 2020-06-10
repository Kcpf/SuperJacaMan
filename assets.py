import pygame
from variable import *
from funcoes import *

PLAYER1_IMG = 'player1_img'
PLAYER2_IMG = 'player2_img'
PLAYER3_IMG = 'player3_img'
PLAYER4_IMG = 'player4_img'
SQUARE_IMG = 'square_img'
JACA_FECHADA_IMG = "jaca_fechada_img"
JACA_ABERTA1_IMG = "jaca_aberta1_img"
JACA_ABERTA2_IMG = "jaca_aberta2_img"
JACA_ABERTA3_IMG = "jaca_aberta3_img"
EXPLOJACA1_IMG = "explojaca1_img"
EXPLOJACA2_IMG = "explojaca2_img"
EXPLOJACA3_IMG = "explojaca3_img"
EXPLOJACA4_IMG = "explojaca4_img"
EXPLOSION_SOUNDS = "explosion_sound"
EXPLOSAO = 'explojaca'
TIJOLO = "tijolo"
TELAINI = 'pejacks'
TELAFIM1 = 'pe_na_jaca1'
TELAFIM2 = 'pe_na_jaca2'


def load_assets():
    jaca_load = pygame.image.load("img/jaca_sprite2.0.png")
    jacas = load_spritesheet(jaca_load, 2, 2)

    explo_load = pygame.image.load("img/explojaca (1).png")
    explo_load = pygame.transform.scale(
        explo_load, 
        (WIDTH_SQUARE*3*2, HEIGHT_SQUARE*3*2)
    )

    explojaca = load_spritesheet(explo_load, 2, 2)

    assets = {}
    assets[PLAYER1_IMG] = pygame.image.load('img/teste.png').convert_alpha()

    assets[PLAYER2_IMG] = pygame.image.load('img/zelda_sprites.png').convert_alpha()

    assets[PLAYER3_IMG] = pygame.image.load('img/ghost_sprites.png').convert_alpha()

    assets[PLAYER4_IMG] = pygame.image.load('img/bomberman_sprites.png').convert_alpha()

    assets[SQUARE_IMG] = pygame.image.load('img/bloco.png').convert_alpha()
    assets[SQUARE_IMG] = pygame.transform.scale(assets['square_img'], SQUARE_DIMENSIONS)

    assets[TIJOLO] = pygame.image.load('img/tijolo.png').convert_alpha()
    assets[TIJOLO] = pygame.transform.scale(assets['tijolo'], SQUARE_DIMENSIONS)

    assets[JACA_FECHADA_IMG] = jacas[0]
    assets[JACA_ABERTA1_IMG] = jacas[1]
    assets[JACA_ABERTA2_IMG] = jacas[2]
    assets[JACA_ABERTA3_IMG] = jacas[3]

    assets[EXPLOJACA1_IMG] = explojaca[0]
    assets[EXPLOJACA2_IMG] = explojaca[1]
    assets[EXPLOJACA3_IMG] = explojaca[2]
    assets[EXPLOJACA4_IMG] = explojaca[3]

    assets[TELAINI] = pygame.image.load('img/PeNaJaca.png').convert_alpha()
    assets[TELAINI] = pygame.transform.scale(assets['pejacks'], RESOLUTION)

    assets[TELAFIM1] = pygame.image.load('img/PeNaJacafinalP1.png').convert_alpha()
    assets[TELAFIM1] = pygame.transform.scale(assets['pe_na_jaca1'], RESOLUTION)

    assets[TELAFIM2] = pygame.image.load('img/PeNaJacafinalP2.png').convert_alpha()
    assets[TELAFIM2] = pygame.transform.scale(assets['pe_na_jaca2'], RESOLUTION)

    # Load Game sounds
    pygame.mixer.music.load('sounds/Mr._Blue_8bit.mp3')
    pygame.mixer.music.set_volume(1)
    # assets[EXPLOSION_SOUNDS] = pygame.mixer.Sound(r'sounds/explosao_8bit.mp3')

    return assets
