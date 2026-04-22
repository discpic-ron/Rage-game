import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

# constants
running = True

# colors
black = (0,0,0)

# functions

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(black)
  pygame.display.flip()
pygame.quit()
