import pygame
from random import choice

def game():
    global dot, pos
    new_dot = ((pos[0][0]+pos[1][0])//2, (pos[0][1]+pos[1][1])//2)
    rand_dot = choice(dot)
    pos = (new_dot, rand_dot)
    pygame.draw.rect(screen, white, (pos[0][0], pos[0][1], dot_size, dot_size))


white     = (255, 255, 255)
black     = (0, 0, 0)
red       = (255, 0, 0)
green     = (0, 255, 0)
blue      = (0, 0, 255)

width = 820
height = 600
dot_size = 1
fps = 60
dot = []

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(black)
pygame.display.set_caption('Game of Chaos')
clock = pygame.time.Clock()

play = False
run = True
while run:
    clock.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if len(dot) < 3:
                pygame.draw.rect(screen, white, (mouse_pos[0], mouse_pos[1], dot_size, dot_size))
                dot.append(mouse_pos)
    if len(dot) == 2:
        start = dot[0]
        rand_dot = dot[1]
        pos = (start, rand_dot)
    if len(dot) == 3:
        play = True
    if play:
        game()
    pygame.display.update()

pygame.quit()
