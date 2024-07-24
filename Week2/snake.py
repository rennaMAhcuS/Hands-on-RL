import pygame

Running: bool = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False


pygame.quit()
