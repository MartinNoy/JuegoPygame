import pygame,random

pygame.init()
win = pygame.display.set_mode((500, 500))
salir = False
reloj1 = pygame.time.Clock()
listarec = []#crea una lista vacia
for x in range(15):#rellenamos la lista con rectangulos random
    w= random.randrange(15,45)#generamos ancho al azar
    h= random.randrange(20,60)#generamos alto al azar
    x= random.randrange(400)#generamos posicion X al azar
    y= random.randrange(400)#generamos posicion Y al azar
    listarec.append(pygame.Rect(x,y,w,h))#rellenamos la lista con rectangulos con dichos valores al azar
    
while salir != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
    reloj1.tick(20)
    win.fill((0,0,0))
    
    for recs in listarec:
        pygame.draw.rect(win, (200,0,0), recs)
    
    
    
    
    pygame.display.update()
    
    
pygame.quit() 

