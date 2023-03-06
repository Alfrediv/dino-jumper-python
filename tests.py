import pygame

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,0,0))

    pygame.display.flip()
