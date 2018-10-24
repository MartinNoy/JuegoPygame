import pygame, sys
from pygame.locals import *
import proyectil
ancho_ventana = 900
alto_ventana = 480


class naveEspacial(pygame.sprite.Sprite):
    """clase para naves"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load('imagenes/Nave.png')
        self.rect = self.imagenNave.get_rect()
        self.rect.centerx = 456
        self.rect.centery = alto_ventana-30
        
        self.listaDisparo = []
        self.Vida = True
        
        self.velocidad= 20
        
        
    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 900:
                self.rect.right = 900
        
    def disparar(self, x, y):
        miProyectil = proyectil.proyectil(x,y)
        self.listaDisparo.append(miProyectil)
    
    def dibujar(self, superficie):
        superficie.blit(self.imagenNave, self.rect)
