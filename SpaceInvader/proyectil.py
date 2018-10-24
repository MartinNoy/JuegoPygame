import pygame, sys
from pygame.locals import *
ancho_ventana = 900
alto_ventana = 480

class proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenProyectil = pygame.image.load('imagenes/disparoa.png')
        
        self.rect = self.imagenProyectil.get_rect()
        
        self.velocidadDisparo = 5
        
        self.rect.top = posy
        self.rect.left = posx
        
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo
    
    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)
