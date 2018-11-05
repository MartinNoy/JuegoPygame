import pygame, sys
from pygame.locals import *
from time import sleep
ancho_ventana = 900
alto_ventana = 480


class naveEnemiga(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigo = pygame.image.load('imagenes/enemigo1.png')
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = 456
        self.rect.centery = 30
        
        self.Vida = True
        
        self.mover = True
        self.velocidad = 5
        
        
        
    def dibujar(self, superficie):
        superficie.blit(self.imagenEnemigo, self.rect)
        
        
    def movimiento(self):
        
        if self.mover == True:
            self.rect.centerx -= self.velocidad
            if self.rect.left <= 0:
                self.mover = False 

        if self.mover == False:
            self.rect.centerx += self.velocidad
            if self.rect.right >= 900:
                self.mover = True 