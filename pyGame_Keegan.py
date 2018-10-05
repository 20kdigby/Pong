import pygame as pygame
import sys

def moveBall():
    global white, location, radius, thickness, black, screen_size, speedx, speedy, ballRect

    if location[0] + radius >= screen_size[0] or location[0] - radius <= 0:
        speedx = -speedx

    if location[1] + radius >= screen_size[1] or location[1] - radius <= 0:
        speedy= -speedy
   
    location[0] = location[0] + speedx
    ballRect = ballRect.move(speedx, 0)
    location[1] = location[1] + speedy
    ballRect = ballRect.move(0, speedy)

    pygame.draw.circle(window, red, location, radius, thickness)
    pygame.display.flip()

def movePaddle():
    global blue, padA, screen_size, aSpeed, padB, bSpeed
    if padA.bottom >= screen_size[1] and aSpeed > 0:
        aSpeed = 0
    if padA.top <= 0 and aSpeed <0:
        aSpeed = 0
    padA = padA.move(0, aSpeed)
    pygame.draw.rect(window, blue, padA)

    if padB.bottom >= screen_size[1] and bSpeed > 0:
        bSpeed = 0
    if padB.top <= 0 and bSpeed <0:
        bSpeed = 0
    padA = padB.move(0, bSpeed)
    pygame.draw.rect(window, blue, padB)
    

def collide(rect1, rect2):
    if rect1.colliderect(rect2):
        print("Collide")
    if rect2.colliderect(rect2):
        print("Collide")

speedx = 3
speedy = 3
screen_size = (1000, 600)
black = (0, 0, 0)
thickness = 0
red = (255, 0, 0)
orange = (255, 165, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
timer = pygame.time.Clock()
location = [500, 300]
radius = 20
padA = pygame.Rect((0, 0), (20, 100))
padB = pygame.Rect((1000, 0), (20, 100))
ballRect= pygame.Rect((location[0]-radius, location[1]-radius), (radius *2, radius*2))
window = pygame.display.set_mode(screen_size)
fps = 60
aSpeed = 0
bSpeed = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                aSpeed = -2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                aSpeed = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                aSpeed= 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                bSpeed = -2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                bSpeed = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_8 or event.key == pygame.K_2:
                bSpeed= 0


    movePaddle()
    moveBall()
    window.fill(orange)
    timer.tick(fps)
    collide(ballRect, padA)