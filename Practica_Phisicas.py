from typing import Text
import pygame
from pygame.locals import *
import math

AllJugador = pygame.sprite.Group()

def cargar_imagen(filename):
    im = pygame.image.load(filename)        
    im = im.convert()    
    return im

class El_Personaje(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.v = pygame.Vector2()
        self.v.xy = 0,-5
        self.angle = 0.0
        self.image = cargar_imagen("C:\Programas de Pyhon\Juegos\JuegosJuegos.com\Salto\Player.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 550
    def update(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_LEFT] and self.rect.left>0:
            self.rect.left -= 3
        if tecla[pygame.K_RIGHT] and self.rect.right<800:
            self.rect.right += 3
        self.rect.y -= math.sin(math.radians(self.angle))*20
        print(math.sin(self.angle))
        if self.angle > 0 :
            self.angle += 0.01
        if self.angle > math.pi//2 :
            self.angle = 0.0





pygame.init()
size = 800,600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
PlayerOne = El_Personaje()
AllJugador.add(PlayerOne)
run = True
Background = pygame
while run:
    clock.tick(60)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                PlayerOne.angle = 0.001

    AllJugador.update()
    AllJugador.draw(screen)
    pygame.display.flip()
pygame.quit()
