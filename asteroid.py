import pygame
import random

class Asteroid(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('asteroid2.png')
    self.image = pygame.transform.smoothscale(self.image, (random.randint(20, 70), random.randint(20, 70)))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(10, 890), random.randint(10, 590))