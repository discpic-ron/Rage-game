import pygame
from dealer import Dealer
from player import Player 
from card import Card

pygame.init()
screen = pygame.display.set_mode((800,600))

# constants
running = True
current_turn = "player"
dealer = Dealer()

# colors
black = (0,0,0)

def hand_value(hand):
  value = 0
  for card in hand:
    value += card.get_value()
  return value
      
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(black)
  pygame.display.flip()
pygame.quit()
