import pygame as pygame

def moveBall():
    global white, location, radius, thickness, black, screen_size, speedx, speedy

    if location[0] + radius >= screen_size[0] or location[0] - radius <= 0:
        speedx = -speedx

    if location[1] + radius >= screen_size[1] or location[1] - radius <= 0:
        speedy= -speedy
   
    location[0] = location[0] + speedx
    location[1] = location[1] + speedy
    

    pygame.draw.circle(window, red, location, radius, thickness)
    pygame.display.flip()

def movePaddle():
    global blue, padA, screen_size
    if padA.bottom >= screen_size[1]: 
        padA = padA.move(0, 1)
    pygame.draw.rect(window, blue, padA)


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
window = pygame.display.set_mode(screen_size)
radius = 20
fps = 60
padA= pygame.Rect((0,0), (20, 100))

while True:
    movePaddle()
    moveBall()
    window.fill(orange)
    timer.tick(fps)
    