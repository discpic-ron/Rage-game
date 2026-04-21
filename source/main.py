import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

# constants
running = True
current_turn = "player"

# colors
black = (0,0,0)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  sreen.fill(black)
  pygame.display.flip()
pygame.quit()
