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
    azul = (0, 0, 255)

    #superficies
    s1 = pygame.Surface((100, 150))#determina el tamaño de la superficie 
    s1.fill(rojo)#rellena una superficie con un color determinado
    s2 = pygame.Surface((25, 25))
    s2.fill((0,255,0))#se pueden pasar directamente valores en RGB

    #rectangulos
    r1 = pygame.Rect(50,50,45,45)
    r2 = pygame.Rect(50,50,25,25)
    #bucle principal
    while salir != False:  # Loop Principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#evento de cerrar ventana
                salir = False
            #if event.type == pygame.MOUSEBUTTONDOWN:evento para presion del boton
                #r1.move_ip(10, 10)#mueve el rectangulo 10px cada vez que se presiona el boton
            if event.type == pygame.KEYDOWN:#revisa si hay teclase precionadas
                if event.key == pygame.K_LEFT:#si se preciono la flecha izuierda realiza el movimiento
                    r2.move_ip(-10, 0)#determina la cantidad de px que se mueve (x,y)
                if event.key == pygame.K_RIGHT:#se mueve hacia la derecha con la fecha derecha
                    r2.move_ip(10, 0)#determina la cantidad de px que se mueve (x,y)
                if event.key == pygame.K_UP:#se mueve hacia arriba con la fecha arriba
                    r2.move_ip(0,-10)#determina la cantidad de px que se mueve (x,y)
                if event.key == pygame.K_DOWN:#se mueve hacia abajo con la fecha abajo
                    r2.move_ip(0, 10)#determina la cantidad de px que se mueve (x,y)
                    
        win.fill(blanco)#pinta la ventana de blanco
        win.blit(s1, (50, 70))#mostrar una superficie predefinida en la ventana
        win.blit(s2, (10, 10))#mostrar una superficie predefinida en la ventana

        pygame.draw.rect(win,azul,r1)
        pygame.draw.rect(win, verde, r2)

        reloj1.tick(20)#setea para refrescar a 20fps
        pygame.display.update()#funcion para refrescar la ventana

    pygame.quit()#cierra la ventana al finalizar el bucle con el ecento QUIT


main()
