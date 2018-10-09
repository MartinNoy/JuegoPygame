import pygame #importa la libreria de pygame!!!


def main():#Definicion de funcion principal
    pygame.init()
    win = pygame.display.set_mode([300, 300])#definicion de la ventana y tamaño
    pygame.display.set_caption("Primer Juego")#nombre a la ventana
    salir = True#variable para bucle principal
    reloj1 = pygame.time.Clock()#reloj para refrescamiento de pantalla

    #colores
    blanco = (255, 255, 255)#determina un color en RGB
    rojo = (255, 0, 0)#determina un color en RGB
    verde = (0, 255, 0)#determina un color en RGB

    #superficies
    s1 = pygame.Surface((100, 150))#determina el tamaño de la superficie 
    s1.fill(rojo)#rellena una superficie con un color determinado
    s2 = pygame.Surface((25, 25))
    s2.fill((0,255,0))#se pueden pasar directamente valores en RGB

    #bucle principal
    while salir != False:  # Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#evento de cerrar ventana
                salir = False

        win.fill(blanco)#pinta la ventana de blanco
        win.blit(s1, (50, 70))#mostrar una superficie predefinida en la ventana
        win.blit(s2, (50, 70))#mostrar una superficie predefinida en la ventana

        reloj1.tick(20)#setea para refrescar a 20fps
        pygame.display.update()#funcion para refrescar la ventana

    pygame.quit()#cierra la ventana al finalizar el bucle con el ecento QUIT


main()
