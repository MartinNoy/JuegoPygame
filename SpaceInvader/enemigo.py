import pygame, sys
from pygame.locals import *
ancho_ventana = 900
alto_ventana = 480


class naveEnemiga(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigo = pygame.image.load('imagenes/enemigo1.png')
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = 456
        self.rect.centery = 30
        
        
        
    def dibujar(self, superficie):
        superficie.blit(self.imagenEnemigo, self.rect)