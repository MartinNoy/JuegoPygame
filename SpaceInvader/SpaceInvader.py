import pygame, sys
from pygame.locals import *
import enemigo
import naveEspacial
import proyectil
#variables globales
ancho_ventana = 900
alto_ventana = 480


def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Space Invader")
    
    imagenFondo = pygame.image.load('imagenes/fondo.png')
    
    jugador = naveEspacial.naveEspacial()
    
    enemigo1 = enemigo.naveEnemiga()
    
    demoproyectil = proyectil.proyectil(456, 30)
    
    enJuego = True
    
    
    while True:
        
        jugador.movimiento()
        
        demoproyectil.trayectoria()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
                
            if enJuego== True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    
                    elif event.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad 
                        
                    elif event.key == K_z:
                        x,y = jugador.rect.center
                        jugador.disparar(x, y)
                        
        ventana.blit(imagenFondo, (0,0))
        
        demoproyectil.dibujar(ventana)
        
        jugador.dibujar(ventana)
        
        enemigo1.dibujar(ventana)
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                
                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                    
        
        pygame.display.update()
        
SpaceInvader()